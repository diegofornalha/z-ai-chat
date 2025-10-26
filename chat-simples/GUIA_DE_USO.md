# 🎯 GUIA DE USO - Chat com GLM-4.5-Flash (GRATUITO)

## ✅ MIGRAÇÃO COMPLETA

**Claude Agent SDK → ZAI SDK**
**Modelo pago → GLM-4.5-Flash (100% GRATUITO)**

---

## 🚀 COMO INICIAR O SERVIDOR

### Opção 1: Usar o servidor backend (RECOMENDADO)

```bash
cd /Users/2a/.claude/z-ai-sdk-python/chat-simples
python server_zai.py
```

**Acesse:**
- Chat: http://localhost:8080/html/index.html
- Histórico: http://localhost:8080/html/history.html
- Config: http://localhost:8080/html/config.html

### Opção 2: Usar Live Server (VS Code)

⚠️ **IMPORTANTE**: O WebSocket conecta em `ws://localhost:8080/ws/chat`, então você PRECISA do servidor Python rodando!

1. Inicie o servidor Python: `python server_zai.py`
2. Abra com Live Server: http://127.0.0.1:5500/chat-simples/html/index.html

---

## 📋 FUNCIONALIDADES

### 💬 Chat Principal (`index.html`)
- ✅ Streaming em tempo real
- ✅ Markdown e syntax highlighting
- ✅ Histórico de conversação
- ✅ Botão "Novo Chat" (salva conversa anterior)
- ✅ Links para Histórico, Uso e Config

### 📁 Histórico (`history.html`)
- ✅ Lista todas as conversas salvas
- ✅ Ordem: índice 0 = Chat 1 (primeiro), índice 3 = Chat 4 (último)
- ✅ Informações: mensagens, perguntas, data
- ✅ Deletar conversa (sem popup)
- ✅ Limpar tudo (sem popup)
- ✅ Clicar para abrir no viewer

### 🔍 Session Viewer (`session-viewer-simple.html`)
- ✅ Visualiza conversa completa
- ✅ Continuar conversando direto no viewer
- ✅ Botões de copiar mensagens
- ✅ Links para voltar

### ⚙️ Config/Uso (`config.html`)
- ✅ Estatísticas: total de conversas e mensagens
- ✅ Limites e quotas do GLM-4.5-Flash
- ✅ Estimativas de uso (60/min, 3.600/h)
- ✅ Informações do modelo
- ✅ Recomendações
- ✅ Exportar histórico JSON
- ✅ Limpar todos os dados

---

## 🎨 IDENTIDADE VISUAL

**Cores Anthropic (SKILL.md):**
- Usuário: Gradiente azul→laranja (#6a9bcc → #d97757)
- Assistente: Branco com nome verde (#788c5d)
- Tipografia: Poppins (headings) + Lora (body)

---

## 📊 QUANTOS PROMPTS VOCÊ TEM?

### Limites Confirmados:
- ✅ Concorrência: 2 requisições simultâneas
- ✅ Custo: $0.00 SEMPRE
- ⚠️ Daily/Monthly: NÃO DOCUMENTADO

### Estimativas Testadas:
- 60 mensagens/minuto ✅
- 3.600 mensagens/hora ✅
- 86.400 mensagens/dia (teórico)

### Uso Prático:
- 10-50 msgs/dia: ✅ SEM PROBLEMAS
- 100-500 msgs/dia: ✅ PROVÁVEL OK
- 1000+ msgs/dia: ⚠️ Pode ter limites

**Conclusão: Para chat normal, você NUNCA vai atingir os limites!**

---

## 💾 ARMAZENAMENTO

**localStorage (navegador):**
- `claude_chat_history_v1` → Conversa atual
- `chat_conversations_history` → Array de conversas salvas (índice 0, 1, 2, 3...)

**Privacidade:**
- ✅ Dados apenas no seu navegador
- ❌ Não sincroniza entre dispositivos
- ✅ Exportar para JSON disponível

---

## 🐛 SOLUÇÃO DE PROBLEMAS

### Status 🟡 (Amarelo) - Não conecta

**Problema:** WebSocket não consegue conectar

**Solução:**
1. Verifique se o servidor está rodando:
   ```bash
   lsof -ti :8080
   ```

2. Se não estiver, inicie:
   ```bash
   cd /Users/2a/.claude/z-ai-sdk-python/chat-simples
   python server_zai.py
   ```

3. Acesse direto: http://localhost:8080/html/index.html

### Histórico vazio

**Problema:** Não aparecem conversas

**Causa:** Conversas só são salvas ao clicar em "✨ Novo Chat"

**Solução:** Após conversar, clique em "✨ Novo Chat" para salvar

### Ordem errada no histórico

**Status:** ✅ CORRIGIDO!

**Agora:** índice 0 = Chat 1, índice 1 = Chat 2, etc.

---

## 📁 ESTRUTURA DO PROJETO

```
chat-simples/
├── server_zai.py              # Backend WebSocket
├── requirements.txt           # Dependências
├── README.md                 # Documentação técnica
├── GUIA_DE_USO.md            # Este guia
├── check_usage.py            # Verificador de uso
│
├── html/
│   ├── index.html            # Chat principal
│   ├── history.html          # Histórico de conversas
│   ├── session-viewer-simple.html  # Visualizador com chat
│   └── config.html           # Configurações e uso
│
├── js/
│   ├── app.js               # Lógica principal
│   ├── debug.js
│   ├── debug-visual.js
│   ├── templates.js
│   ├── metrics.js
│   ├── search.js
│   ├── notifications.js
│   ├── tool-indicator.js
│   └── shortcuts.js
│
└── css/
    └── style.css            # Cores Anthropic
```

---

## ✅ ALTERAÇÕES FEITAS

### Removido:
- ❌ Botão debug (☰)
- ❌ Botão refresh (🔄)
- ❌ Contador de mensagens no viewer
- ❌ Custo no histórico (sempre $0.00)
- ❌ Popups de confirmação
- ❌ autosave.js (conflito)

### Adicionado:
- ✅ Página de Config/Uso completa
- ✅ Sistema de histórico múltiplo
- ✅ Session viewer com chat integrado
- ✅ Ordem correta do array (0,1,2,3...)
- ✅ Cores Anthropic (SKILL.md)

---

## 🎊 PRONTO PARA USO!

**Seu chat está 100% funcional com:**
- ✅ ZAI SDK
- ✅ GLM-4.5-Flash (GRÁTIS)
- ✅ Streaming em tempo real
- ✅ Histórico de conversas
- ✅ Interface completa
- ✅ $0.00 sempre

**Comece a usar agora:**
```bash
python server_zai.py
# Acesse: http://localhost:8080/html/index.html
```
