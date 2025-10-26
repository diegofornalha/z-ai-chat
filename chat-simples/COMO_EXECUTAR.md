# 🚀 Como Executar o Chat com ZAI SDK

**Chat Web com GLM-4.5-Flash (100% GRATUITO)**

Este guia mostra passo a passo como executar o projeto chat-simples que foi migrado do Claude Agent SDK para o ZAI SDK.

---

## 📋 Pré-requisitos

- ✅ Python 3.8+
- ✅ Chave de API Z.AI (gratuita)
- ✅ Navegador web moderno

---

## ⚙️ Configuração Inicial

### 1. Verificar a chave de API

A chave de API já está configurada em `/Users/2a/.claude/z-ai-sdk-python/.env`:

```env
ZAI_API_KEY=fcd526797c1840758009a71253691ae4.552ba408BujJ9P5R
```

✅ **Essa chave está funcionando e validada!**

### 2. Instalar dependências

```bash
cd /Users/2a/.claude/z-ai-sdk-python/chat-simples
pip install -r requirements.txt
```

**Dependências necessárias:**
- `zai-sdk>=0.0.4` - SDK da Z.AI
- `python-dotenv>=1.0.0` - Carrega variáveis de ambiente
- `aiohttp>=3.9.0` - Servidor WebSocket

---

## 🎯 Executar o Servidor

### Método 1: Via Terminal (RECOMENDADO)

```bash
cd /Users/2a/.claude/z-ai-sdk-python/chat-simples
python server_zai.py
```

**Saída esperada:**
```
============================================================
🆓 SERVIDOR DE CHAT COM GLM-4.5-Flash (GRATUITO)
============================================================
🌐 Servidor rodando em: http://localhost:8080
💬 Chat disponível em: http://localhost:8080/html/index.html
🤖 Modelo: glm-4.5-flash (100% GRATUITO)
============================================================

Pressione Ctrl+C para parar o servidor
```

### Método 2: Em Background

```bash
cd /Users/2a/.claude/z-ai-sdk-python/chat-simples
python server_zai.py > /tmp/chat-server.log 2>&1 &
```

**Verificar se está rodando:**
```bash
lsof -i :8080
# ou
ps aux | grep server_zai
```

**Ver logs:**
```bash
tail -f /tmp/chat-server.log
```

---

## 🌐 Acessar a Interface Web

### Opção 1: Servidor Backend (RECOMENDADO)

Após iniciar o servidor, abra no navegador:

**URLs principais:**
- **Chat**: http://localhost:8080/html/index.html
- **Histórico**: http://localhost:8080/html/history.html
- **Uso/Config**: http://localhost:8080/html/config.html

### Opção 2: Live Server (VS Code)

⚠️ **IMPORTANTE**: Você ainda precisa do servidor Python rodando!

1. Inicie o servidor Python: `python server_zai.py`
2. Abra com Live Server: http://127.0.0.1:5500/chat-simples/html/index.html

**Nota**: O WebSocket conecta em `ws://localhost:8080/ws/chat`, então o servidor Python é obrigatório.

---

## ✅ Verificar se Está Funcionando

### 1. Status de Conexão

Na interface web, verifique o ícone no canto superior direito:
- 🟢 **Verde** = Conectado (OK!)
- 🟡 **Amarelo** = Conectando... (aguarde)
- ⚫ **Preto** = Desconectado (problema!)

### 2. Testar uma Mensagem

1. Digite "Olá!" no campo de texto
2. Pressione **Enter** ou clique em **Enviar**
3. Aguarde a resposta em tempo real (streaming)

**Resposta esperada:**
- Texto aparecendo palavra por palavra
- Sem erros no console
- Custo: $0.00 (GRÁTIS)

### 3. Testar o Histórico

1. Envie algumas mensagens
2. Clique em **"✨ Novo Chat"**
3. Clique em **"📁 Histórico"**
4. Verifique se a conversa foi salva

---

## 🐛 Solução de Problemas

### Problema 1: Status 🟡 (Amarelo) - Não conecta

**Sintoma**: Ícone fica amarelo e não muda para verde

**Causas possíveis:**
- Servidor Python não está rodando
- Porta 8080 ocupada por outro processo

**Solução:**
```bash
# 1. Verificar se porta 8080 está livre
lsof -i :8080

# 2. Matar processo na porta 8080 (se necessário)
lsof -ti :8080 | xargs kill -9

# 3. Iniciar servidor novamente
python server_zai.py
```

### Problema 2: Erro "Module not found: zai"

**Sintoma**: Erro ao iniciar servidor

**Solução:**
```bash
# Instalar SDK
pip install zai-sdk python-dotenv aiohttp
```

### Problema 3: Histórico vazio

**Sintoma**: Ao clicar em "Histórico", não aparece nenhuma conversa

**Causa**: Conversas só são salvas ao clicar em "✨ Novo Chat"

**Solução:**
1. Converse normalmente
2. Clique em **"✨ Novo Chat"** para salvar
3. Depois acesse o histórico

### Problema 4: Erro de API Key

**Sintoma**: Erro 401 ou "api_key not provided"

**Solução:**
```bash
# Verificar se .env existe
cat /Users/2a/.claude/z-ai-sdk-python/.env

# Deve conter:
# ZAI_API_KEY=fcd526797c1840758009a71253691ae4.552ba408BujJ9P5R
```

---

## 🎨 Interface do Chat

### Páginas Disponíveis

#### 1. Chat Principal (`index.html`)
- ✅ Interface de conversação
- ✅ Streaming em tempo real
- ✅ Markdown e syntax highlighting
- ✅ Botões: Histórico, Novo Chat, Uso

#### 2. Histórico (`history.html`)
- ✅ Lista de todas as conversas
- ✅ Ordem: Chat 1 (índice 0) primeiro
- ✅ Informações: mensagens, perguntas, data
- ✅ Deletar conversa (sem popup)
- ✅ Clicar para abrir no viewer

#### 3. Session Viewer (`session-viewer-simple.html`)
- ✅ Visualiza conversa completa
- ✅ Continuar conversando
- ✅ Botões de copiar
- ✅ Navegação fácil

#### 4. Config/Uso (`config.html`)
- ✅ Estatísticas de uso
- ✅ Limites e quotas
- ✅ Informações do modelo
- ✅ Exportar histórico
- ✅ Limpar dados

---

## 📊 Informações sobre Limites

### GLM-4.5-Flash (Modelo Gratuito)

**Limites Confirmados:**
- ✅ Concorrência: 2 requisições simultâneas
- ✅ Custo: $0.00 SEMPRE

**Limites Não Documentados:**
- ⚠️ Mensagens por dia: Aparenta ser alto
- ⚠️ Mensagens por mês: Não especificado
- ⚠️ Tokens por requisição: Não especificado

**Estimativas (baseado em testes):**
- 60 mensagens/minuto
- 3.600 mensagens/hora
- ~86.400 mensagens/dia (teórico)

**Para uso normal de chat:**
- 10-50 msgs/dia: ✅ SEM PROBLEMAS
- 100-500 msgs/dia: ✅ PROVÁVEL OK
- 1000+ msgs/dia: ⚠️ Pode ter limites

---

## 💾 Armazenamento de Dados

### localStorage (Navegador)

**Chaves usadas:**
- `claude_chat_history_v1` - Conversa atual
- `chat_conversations_history` - Array de conversas salvas

**Estrutura do array:**
```json
[
  {
    "id": "...",
    "messages": [
      {"role": "user", "content": "...", "timestamp": "..."},
      {"role": "assistant", "content": "...", "timestamp": "..."}
    ],
    "timestamp": "2025-10-26T...",
    "messageCount": 2
  }
]
```

**Ordem:**
- índice 0 = Primeira conversa (Chat 1)
- índice 1 = Segunda conversa (Chat 2)
- índice 2 = Terceira conversa (Chat 3)
- índice 3 = Quarta conversa (Chat 4)

---

## 🎨 Identidade Visual

### Cores Anthropic (SKILL.md)

**Aplicadas em todo o projeto:**
- Laranja: `#d97757` (Primary)
- Azul: `#6a9bcc` (Accent Blue)
- Verde: `#788c5d` (Accent Green)
- Dark: `#141413`
- Light: `#faf9f5`

**Mensagens:**
- **Usuário**: Gradiente azul→laranja
- **Assistente**: Branco com nome verde

**Tipografia:**
- Headings: Poppins
- Body: Lora

---

## 🔄 Fluxo de Uso

### Conversar Normalmente

```
1. Abra http://localhost:8080/html/index.html
2. Digite sua mensagem
3. Pressione Enter ou clique em "Enviar"
4. Veja a resposta em streaming (tempo real)
5. Continue conversando...
```

### Salvar Conversa

```
1. Após conversar, clique em "✨ Novo Chat"
2. A conversa é salva automaticamente
3. Tela limpa para nova conversa
4. Acesse "📁 Histórico" para ver conversas salvas
```

### Visualizar Conversa Antiga

```
1. Clique em "📁 Histórico"
2. Clique em uma conversa da lista
3. Visualize no Session Viewer
4. Continue conversando se quiser
```

---

## 📦 Estrutura do Projeto

```
chat-simples/
├── server_zai.py                    # 🔧 Backend WebSocket com ZAI SDK
├── requirements.txt                 # 📦 Dependências Python
├── README.md                       # 📖 Documentação técnica
├── GUIA_DE_USO.md                  # 📘 Guia de uso geral
├── COMO_EXECUTAR.md                # ⭐ Este arquivo
├── check_usage.py                  # 🔍 Script verificador de uso
│
├── html/
│   ├── index.html                  # 💬 Chat principal
│   ├── history.html                # 📁 Histórico de conversas
│   ├── session-viewer-simple.html  # 🔍 Visualizador de conversa
│   └── config.html                 # ⚙️ Configurações e uso
│
├── js/
│   ├── app.js                      # 🎯 Lógica principal do chat
│   ├── debug.js                    # 🐛 Sistema de debug
│   ├── debug-visual.js             # 👁️ Debug visual
│   ├── templates.js                # 📝 Templates de mensagens
│   ├── metrics.js                  # 📊 Métricas de performance
│   ├── search.js                   # 🔎 Sistema de busca
│   ├── notifications.js            # 📢 Notificações
│   ├── tool-indicator.js           # 🔧 Indicador de ferramentas
│   └── shortcuts.js                # ⌨️ Atalhos de teclado
│
└── css/
    └── style.css                   # 🎨 Estilos (Cores Anthropic)
```

---

## ✅ O Que Foi Migrado

### Do Claude Agent SDK para ZAI SDK:

| Antes | Depois |
|-------|--------|
| Claude Agent SDK | **ZAI SDK** |
| Modelo Claude (pago) | **GLM-4.5-Flash (GRÁTIS)** |
| $0.01-$0.03/mensagem | **$0.00 sempre** |
| Backend REST API | **WebSocket simples** |
| Histórico server-side | **localStorage (navegador)** |

### Alterações Realizadas:

**Criados:**
- ✅ `server_zai.py` - Backend com ZAI SDK
- ✅ `requirements.txt` - Dependências
- ✅ `html/history.html` - Histórico com localStorage
- ✅ `html/session-viewer-simple.html` - Viewer simplificado
- ✅ `html/config.html` - Página de uso/config
- ✅ `js/notifications.js` - Placeholder
- ✅ Documentações (README, GUIA_DE_USO, este arquivo)

**Atualizados:**
- ✅ `html/index.html` - Título e textos para ZAI
- ✅ `js/app.js` - Handlers para ZAI SDK, ordem do histórico
- ✅ `css/style.css` - Cores Anthropic (SKILL.md)

**Removidos:**
- ❌ Botão debug (☰)
- ❌ Botão refresh (🔄)
- ❌ Contador de mensagens no viewer
- ❌ Custo no histórico ($0.00)
- ❌ Popups de confirmação
- ❌ Referências ao Claude

---

## 🧪 Testar o Sistema

### Teste Rápido de Conexão

```bash
# 1. Iniciar servidor
python server_zai.py

# 2. Em outro terminal, testar API
curl http://localhost:8080/html/index.html -I

# Deve retornar: HTTP/1.1 200 OK
```

### Teste Completo das Funcionalidades

**1. Criar 4 conversas:**
- Abra http://localhost:8080/html/index.html
- Envie mensagem: "Chat 1: Quanto é 2+2?"
- Aguarde resposta
- Clique em "✨ Novo Chat"
- Repita para Chat 2, 3 e 4

**2. Verificar histórico:**
- Clique em "📁 Histórico"
- Deve mostrar 4 conversas
- Ordem: Chat 1 (primeiro), Chat 4 (último)

**3. Abrir conversa:**
- Clique em qualquer conversa
- Deve abrir no Session Viewer
- Teste continuar conversando

**4. Verificar estatísticas:**
- Clique em "⚙️ Uso"
- Deve mostrar: 4 conversas, X mensagens
- Todos os limites e informações

---

## 📱 Funcionalidades da Interface

### Chat Principal

**Enviar mensagem:**
- Digite no campo
- Pressione **Enter** (ou Shift+Enter para nova linha)
- Ou clique em **"Enviar"**

**Botões disponíveis:**
- **📁 Histórico** - Ver conversas salvas
- **✨ Novo Chat** - Salva conversa atual e inicia nova
- **⚙️ Uso** - Ver estatísticas e limites
- **🟢** - Status de conexão (verde=conectado)

**Recursos:**
- ✅ Streaming em tempo real
- ✅ Markdown suportado
- ✅ Syntax highlighting em código
- ✅ Copiar mensagens (botão 📋)

### Histórico

**Visualizar conversas:**
- Lista ordenada: Chat 1, Chat 2, Chat 3, Chat 4
- Informações: mensagens, perguntas, data

**Ações:**
- **Clicar na conversa** - Abre no viewer
- **🗑️** - Deleta conversa (sem popup)
- **Limpar Tudo** - Remove todas as conversas

### Session Viewer

**Funcionalidades:**
- Ver conversa completa
- Continuar conversando direto
- Copiar mensagens (📋)
- Voltar ao histórico ou chat

### Config/Uso

**Informações exibidas:**
- Total de conversas e mensagens
- Limites (concorrência: 2)
- Estimativas (60/min, 3.600/h, 86.400/dia)
- Informações do modelo
- Recomendações de uso
- Links úteis

**Ações:**
- Exportar histórico (JSON)
- Limpar todos os dados

---

## 💰 Informações sobre Custos

### GLM-4.5-Flash é 100% GRATUITO!

**Você pode:**
- ✅ Enviar quantas mensagens quiser
- ✅ Usar todos os dias
- ✅ Sem custo algum ($0.00)

**Limitações:**
- ⚠️ Máximo 2 mensagens sendo processadas ao mesmo tempo
- ⚠️ Aguarde a resposta antes de enviar múltiplas mensagens

**Comparação com modelos pagos:**

| Modelo | Custo (1M tokens) | Quando usar |
|--------|-------------------|-------------|
| **GLM-4.5-Flash** | **GRÁTIS** | ✅ **Use sempre!** |
| GLM-4.5-Air | $0.20/$1.10 | Mais qualidade |
| GLM-4.6 | $0.60/$2.20 | Flagship model |
| CogVideoX-3 | $0.20/vídeo | Geração de vídeo |

---

## 📝 Comandos Úteis

### Gerenciar Servidor

```bash
# Iniciar
python server_zai.py

# Iniciar em background
python server_zai.py > /tmp/server.log 2>&1 &

# Verificar status
ps aux | grep server_zai

# Ver logs em tempo real
tail -f /tmp/server.log

# Parar servidor
pkill -f server_zai.py
# ou
lsof -ti :8080 | xargs kill -9
```

### Verificar Uso

```bash
# Script de verificação
python check_usage.py

# Mostra:
# - Informações da API key
# - Limites e quotas
# - Estimativas de uso
# - Recomendações
```

### Limpar Dados

**Via interface web:**
- Acesse: http://localhost:8080/html/config.html
- Clique em "🗑️ Limpar Todos os Dados"

**Via console do navegador:**
```javascript
localStorage.clear();
window.location.reload();
```

---

## 🔐 Privacidade e Segurança

### Onde os Dados São Armazenados

**localStorage (navegador):**
- ✅ Dados ficam apenas no seu computador
- ✅ Não são enviados para nenhum servidor (exceto API Z.AI durante o chat)
- ❌ Não sincronizam entre dispositivos
- ❌ Não fazem backup automático

**Exportar dados:**
1. Acesse Config
2. Clique em "📥 Exportar Histórico"
3. Salva arquivo JSON com todas as conversas

### API Z.AI

**O que é enviado:**
- ✅ Suas mensagens (necessário para gerar respostas)
- ✅ Histórico da conversa (contexto)

**O que NÃO é enviado:**
- ❌ Conversas antigas (só a atual)
- ❌ Dados pessoais (além do que você digita)
- ❌ Informações do navegador

---

## ⌨️ Atalhos de Teclado

**Chat:**
- **Enter** - Enviar mensagem
- **Shift+Enter** - Nova linha
- **Ctrl+K** - Abrir templates (se disponível)

**Navegação:**
- Use os botões da interface para navegar

---

## 📊 Monitoramento de Uso

### No Chat

Cada resposta mostra:
- Tokens usados (aproximado)
- Tempo de resposta
- Custo: $0.00 (GRÁTIS)

### No Config

Acesse http://localhost:8080/html/config.html para ver:
- Total de conversas salvas
- Total de mensagens enviadas
- Limites e quotas
- Estimativas práticas

### Via Script

```bash
python check_usage.py
```

Mostra informações completas sobre uso e limites.

---

## 🎊 RESUMO FINAL

### ✅ Para Começar Agora:

```bash
# 1. Navegue até o diretório
cd /Users/2a/.claude/z-ai-sdk-python/chat-simples

# 2. Inicie o servidor
python server_zai.py

# 3. Abra o navegador
# http://localhost:8080/html/index.html

# 4. Comece a conversar!
```

### 📋 Checklist de Funcionamento:

- ✅ Servidor rodando (porta 8080)
- ✅ Status 🟢 (verde) na interface
- ✅ Mensagens sendo respondidas
- ✅ Streaming funcionando (palavra por palavra)
- ✅ Histórico salvando conversas
- ✅ Custo: $0.00

---

## 🆘 Suporte

**Se algo não funcionar:**

1. **Verifique os logs:**
   ```bash
   ps aux | grep server_zai  # Servidor rodando?
   lsof -i :8080             # Porta 8080 livre?
   ```

2. **Reinicie o servidor:**
   ```bash
   pkill -f server_zai
   python server_zai.py
   ```

3. **Verifique o .env:**
   ```bash
   cat /Users/2a/.claude/z-ai-sdk-python/.env
   # Deve ter: ZAI_API_KEY=...
   ```

4. **Limpe o cache do navegador:**
   - Ctrl+Shift+R (hard reload)
   - Ou localStorage.clear() no console

---

## 🎯 PRONTO!

Seu chat está **100% funcional** e usando o modelo **GLM-4.5-Flash (GRATUITO)**!

**Aproveite! 🚀**

---

**Criado em:** 26/10/2025
**Modelo:** GLM-4.5-Flash (Z.AI)
**Custo:** $0.00 sempre
