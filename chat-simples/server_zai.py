#!/usr/bin/env python3
"""
🆓 Servidor WebSocket para Chat com GLM-4.5-Flash (GRATUITO)

Substituição do Claude Agent SDK pelo ZAI SDK
Modelo usado: GLM-4.5-Flash (100% GRATUITO)

Funcionalidades:
- Streaming em tempo real
- Histórico de conversação
- WebSocket para comunicação com frontend
- Markdown suportado
"""
import asyncio
import json
import logging
import os
from datetime import datetime
from typing import List, Dict

from dotenv import load_dotenv
from zai import ZaiClient
from aiohttp import web

# Carrega .env
load_dotenv()

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Modelo GRATUITO
MODEL = "glm-4.5-flash"

# Cliente ZAI
client = ZaiClient()

# Armazena conversações ativas
active_conversations: Dict[str, List[Dict]] = {}


class ChatHandler:
    """Handler para gerenciar chats com GLM-4.5-Flash"""

    def __init__(self, ws: web.WebSocketResponse):
        self.ws = ws
        self.conversation_id = None
        self.messages: List[Dict] = []

    async def send_json(self, data: dict):
        """Envia mensagem JSON para o cliente"""
        try:
            await self.ws.send_str(json.dumps(data))
        except Exception as e:
            logger.error(f"Erro ao enviar mensagem: {e}")

    async def send_status(self, status: str, message: str = ""):
        """Envia status para o cliente"""
        await self.send_json({
            'type': 'status',
            'status': status,
            'message': message
        })

    async def send_error(self, error_message: str):
        """Envia erro para o cliente"""
        await self.send_json({
            'type': 'error',
            'content': error_message
        })

    async def send_text_delta(self, content: str):
        """Envia delta de texto (streaming)"""
        await self.send_json({
            'type': 'content_block_delta',
            'delta': {
                'type': 'text_delta',
                'text': content
            }
        })

    async def send_message_start(self):
        """Envia início de mensagem"""
        await self.send_json({
            'type': 'message_start',
            'message': {
                'role': 'assistant',
                'model': MODEL
            }
        })

    async def send_message_stop(self, usage: dict):
        """Envia fim de mensagem com estatísticas"""
        await self.send_json({
            'type': 'message_stop',
            'usage': usage
        })

    async def handle_user_message(self, user_message: str, config: dict = None):
        """Processa mensagem do usuário e gera resposta"""
        try:
            # Configurações padrão
            if config is None:
                config = {
                    'model': MODEL,
                    'temperature': 0.7,
                    'maxTokens': 2000,
                    'webSearchEnabled': False,
                    'roleplayEnabled': False,
                    'roleplay': {}
                }

            model = config.get('model', MODEL)
            temperature = config.get('temperature', 0.7)
            max_tokens = config.get('maxTokens', 2000)
            web_search_enabled = config.get('webSearchEnabled', False)
            roleplay_enabled = config.get('roleplayEnabled', False)
            roleplay_config = config.get('roleplay', {})

            # Adiciona mensagem do usuário ao histórico
            self.messages.append({
                'role': 'user',
                'content': user_message
            })

            # Envia início da resposta
            await self.send_message_start()
            await self.send_status('streaming', 'Gerando resposta...')

            # Chama API do ZAI com streaming
            full_response = ""
            start_time = datetime.now()

            logger.info(f"🚀 Enviando para {model}: {user_message[:50]}...")

            # Prepara parâmetros da API
            api_params = {
                'model': model,
                'messages': self.messages,
                'stream': True,
                'temperature': temperature,
                'max_tokens': max_tokens
            }

            # Adiciona Web Search se habilitado
            if web_search_enabled:
                api_params['tools'] = [{
                    'type': 'web_search',
                    'web_search': {
                        'search_query': user_message,
                        'search_result': True
                    }
                }]
                logger.info("🔍 Web Search habilitado")

            # Adiciona Role-play se habilitado
            if roleplay_enabled and roleplay_config:
                api_params['meta'] = {
                    'bot_name': roleplay_config.get('botName', 'Assistente'),
                    'bot_info': roleplay_config.get('botInfo', 'Você é um assistente útil.'),
                    'user_name': roleplay_config.get('userName', 'Usuário')
                }
                logger.info(f"🎭 Role-play habilitado: {roleplay_config.get('botName')}")

            stream = client.chat.completions.create(**api_params)

            # Processa stream
            for chunk in stream:
                if chunk.choices and len(chunk.choices) > 0:
                    delta = chunk.choices[0].delta

                    if hasattr(delta, 'content') and delta.content:
                        content = delta.content
                        full_response += content

                        # Envia delta para o cliente
                        await self.send_text_delta(content)

            # Calcula tempo de resposta
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()

            # Adiciona resposta ao histórico
            self.messages.append({
                'role': 'assistant',
                'content': full_response
            })

            # Calcula tokens aproximados (1 token ≈ 4 chars)
            input_tokens = sum(len(m['content']) for m in self.messages[:-1]) // 4
            output_tokens = len(full_response) // 4
            total_tokens = input_tokens + output_tokens

            # Envia fim da mensagem
            usage = {
                'input_tokens': input_tokens,
                'output_tokens': output_tokens,
                'total_tokens': total_tokens,
                'cost': 0.00,  # GRATUITO!
                'duration_seconds': round(duration, 2)
            }

            await self.send_message_stop(usage)
            await self.send_status('completed', f'Resposta gerada em {duration:.2f}s')

            logger.info(f"✅ Resposta gerada - {total_tokens} tokens (GRÁTIS) em {duration:.2f}s")

        except Exception as e:
            logger.error(f"❌ Erro ao processar mensagem: {e}")
            await self.send_error(f"Erro ao gerar resposta: {str(e)}")
            await self.send_status('error', str(e))

    async def handle_new_conversation(self):
        """Inicia nova conversação"""
        import uuid
        self.conversation_id = str(uuid.uuid4())
        self.messages = []

        # Mensagem do sistema (opcional)
        self.messages.append({
            'role': 'system',
            'content': 'Você é um assistente útil e amigável. Responda de forma clara e concisa.'
        })

        logger.info(f"Nova conversação iniciada: {self.conversation_id}")

        await self.send_json({
            'type': 'conversation_created',
            'conversation_id': self.conversation_id
        })


async def websocket_handler(request):
    """Handler principal do WebSocket"""
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    handler = ChatHandler(ws)

    logger.info("🔌 Cliente conectado")

    # Envia status inicial
    await handler.send_status('connected', 'Conectado ao servidor ZAI')

    try:
        async for msg in ws:
            if msg.type == web.WSMsgType.TEXT:
                try:
                    data = json.loads(msg.data)
                    action = data.get('action')

                    if action == 'new_conversation':
                        await handler.handle_new_conversation()

                    elif action == 'send_message':
                        message = data.get('message', '')
                        config = data.get('config', None)
                        if message.strip():
                            await handler.handle_user_message(message, config)

                    else:
                        logger.warning(f"Ação desconhecida: {action}")

                except json.JSONDecodeError as e:
                    logger.error(f"Erro ao decodificar JSON: {e}")
                    await handler.send_error(f"JSON inválido: {str(e)}")

            elif msg.type == web.WSMsgType.ERROR:
                logger.error(f"WebSocket erro: {ws.exception()}")

    except Exception as e:
        logger.error(f"Erro no WebSocket: {e}")

    finally:
        logger.info("🔌 Cliente desconectado")

    return ws


async def index_handler(request):
    """Redireciona para a página HTML"""
    return web.FileResponse('./html/index.html')


async def cors_middleware(app, handler):
    """Middleware para permitir CORS"""
    async def middleware_handler(request):
        if request.method == 'OPTIONS':
            # Preflight request
            response = web.Response()
        else:
            response = await handler(request)

        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = '*'
        return response
    return middleware_handler


def main():
    """Inicia o servidor"""
    app = web.Application(middlewares=[cors_middleware])

    # Rotas
    app.router.add_get('/ws/chat', websocket_handler)
    app.router.add_get('/', index_handler)

    # Arquivos estáticos
    app.router.add_static('/css', './css')
    app.router.add_static('/js', './js')
    app.router.add_static('/html', './html')

    # Configuração
    host = '0.0.0.0'
    port = 8080

    print("\n" + "=" * 60)
    print("🆓 SERVIDOR DE CHAT COM GLM-4.5-Flash (GRATUITO)")
    print("=" * 60)
    print(f"🌐 Servidor rodando em: http://localhost:{port}")
    print(f"💬 Chat disponível em: http://localhost:{port}/html/index.html")
    print(f"🤖 Modelo: {MODEL} (100% GRATUITO)")
    print("=" * 60)
    print("\nPressione Ctrl+C para parar o servidor\n")

    # Inicia servidor
    web.run_app(app, host=host, port=port, print=None)


if __name__ == '__main__':
    main()
