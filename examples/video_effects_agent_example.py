#!/usr/bin/env python3
"""
🎬 Video Effects Agent Example - Special Effects Video Generation

Demonstra o uso do agente de geração de vídeo com efeitos especiais.
Usa templates pré-definidos como "french_kiss" para criar vídeos.

Agent ID: vidu_template_agent
Custo: $0.20 por vídeo
Tipo: Async (requer polling para resultado)
"""
from dotenv import load_dotenv
from zai import ZaiClient
import asyncio
import time

# Carrega variáveis de ambiente (.env)
load_dotenv()


async def generate_video_with_effects():
    """
    Exemplo assíncrono de geração de vídeo com efeitos especiais
    Inclui funcionalidade de polling para obter o resultado
    """
    print("=" * 60)
    print("🎬 GERAÇÃO DE VÍDEO COM EFEITOS ESPECIAIS")
    print("=" * 60)
    print()

    client = ZaiClient()

    # 1. Submeter tarefa assíncrona
    print("📤 Submetendo tarefa de geração de vídeo...")
    print("   • Template: french_kiss")
    print("   • Imagem de entrada fornecida")
    print()

    response = client.agents.invoke(
        agent_id="vidu_template_agent",
        custom_variables={
            "template": "french_kiss"
        },
        messages=[{
            "role": "user",
            "content": [{
                "type": "text",
                "text": "The two figures in the painting gradually approach each other, then kiss passionately, alternating with deep and firm intensity"
            }, {
                "type": "image_url",
                "image_url": "https://i0.sinaimg.cn/edu/2011/1125/U4999P42DT20111125164101.jpg"
            }]
        }]
    )

    print("✅ Tarefa submetida!")
    print(f"📋 Resposta: {response}")
    print()

    # 2. Obter ID da tarefa assíncrona
    async_id = response.async_id
    if not async_id:
        print("❌ Falha ao obter ID da tarefa assíncrona")
        return None

    print(f"🆔 Task ID: {async_id}")
    print()

    # 3. Fazer polling para obter resultado
    print("⏳ Aguardando conclusão do vídeo...")
    print("   (Isso pode levar alguns minutos)")
    print()

    max_wait_time = 300  # Tempo máximo: 5 minutos
    start_time = time.time()
    poll_count = 0

    while True:
        elapsed = int(time.time() - start_time)

        # Timeout
        if elapsed > max_wait_time:
            print("❌ Timeout: Tempo máximo de espera excedido")
            break

        poll_count += 1
        print(f"🔍 Consulta #{poll_count} - {elapsed}s decorridos... ", end="", flush=True)

        result = client.agents.async_result(
            agent_id="vidu_template_agent",
            async_id=async_id
        )

        # Verificar status
        status = result.status

        if status == "success":
            print("✅ SUCESSO!")
            print()
            print("=" * 60)
            print("🎉 VÍDEO GERADO COM SUCESSO!")
            print("=" * 60)
            print()
            print(f"📊 Resultado completo:")
            print(result)
            print()
            print(f"⏱️  Tempo total: {elapsed} segundos")
            return result

        elif status == "failed":
            print("❌ FALHOU!")
            print()
            print("⚠️  A geração do vídeo falhou")
            print(f"📋 Detalhes: {result}")
            return None

        elif status in ["pending", "processing", "queued"]:
            print(f"⏳ Em progresso ({status})")

        else:
            print(f"❓ Status desconhecido: {status}")

        # Aguardar 5 segundos antes de consultar novamente
        await asyncio.sleep(5)

    return None


async def generate_video_different_template():
    """Exemplo com template diferente"""
    print("=" * 60)
    print("🎬 GERAÇÃO COM TEMPLATE PERSONALIZADO")
    print("=" * 60)
    print()

    client = ZaiClient()

    # Exemplo com outro template (se disponível)
    response = client.agents.invoke(
        agent_id="vidu_template_agent",
        custom_variables={
            "template": "your_template_name"  # Substitua pelo template desejado
        },
        messages=[{
            "role": "user",
            "content": [{
                "type": "text",
                "text": "Descrição da cena desejada"
            }, {
                "type": "image_url",
                "image_url": "URL_DA_SUA_IMAGEM"
            }]
        }]
    )

    print(f"✅ Tarefa submetida: {response.async_id}")
    print()

    # Aqui você faria o mesmo polling do exemplo anterior
    # ...


async def main():
    """Executa todos os exemplos de vídeo"""
    print("\n")
    print("🎯 EXEMPLOS DO VIDEO EFFECTS AGENT")
    print("=" * 60)
    print()
    print("ℹ️  INFORMAÇÕES:")
    print("   • Agent ID: vidu_template_agent")
    print("   • Templates disponíveis: french_kiss, etc.")
    print("   • Tipo: Async (requer polling)")
    print("   • Custo: $0.20 por vídeo")
    print("   • Tempo médio: 2-5 minutos")
    print()

    # Exemplo principal
    result = await generate_video_with_effects()

    if result:
        print("=" * 60)
        print("✅ EXEMPLO COMPLETO!")
        print("=" * 60)
    else:
        print("=" * 60)
        print("⚠️  EXEMPLO NÃO COMPLETOU")
        print("=" * 60)

    print()
    print("💡 DICAS:")
    print("   • A geração de vídeo é assíncrona")
    print("   • Use async_result() para verificar status")
    print("   • Aguarde até status = 'success'")
    print("   • Tempo médio: 2-5 minutos")
    print()


if __name__ == "__main__":
    asyncio.run(main())
