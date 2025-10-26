#!/usr/bin/env python3
"""
🆓 EXEMPLOS PRÁTICOS COM GLM-4.5-Flash (MODELO GRATUITO)

Este modelo é 100% GRATUITO e você pode usar agora mesmo!
Limite: 2 requisições simultâneas

Casos de uso incluídos:
1. Chat simples
2. Tradução de texto
3. Resumo de textos
4. Geração de código
5. Análise de dados
6. Criação de conteúdo
7. Conversação com histórico
8. Streaming (resposta em tempo real)
"""
from dotenv import load_dotenv
from zai import ZaiClient

# Carrega .env
load_dotenv()
client = ZaiClient()

# Modelo GRATUITO
MODEL = "glm-4.5-flash"


def exemplo_1_chat_simples():
    """Exemplo 1: Chat simples e direto"""
    print("=" * 60)
    print("🆓 EXEMPLO 1: Chat Simples")
    print("=" * 60)
    print()

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": "Explique o que é inteligência artificial em 2 parágrafos"}
        ]
    )

    print("💬 Resposta:")
    print(response.choices[0].message.content)
    print()
    print(f"📊 Tokens usados (GRÁTIS): {response.usage.total_tokens}")
    print()


def exemplo_2_traducao():
    """Exemplo 2: Tradução de texto"""
    print("=" * 60)
    print("🆓 EXEMPLO 2: Tradução de Texto")
    print("=" * 60)
    print()

    texto_original = """
    Good morning! I hope you're having a wonderful day.
    Artificial intelligence is transforming the world.
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": f"Traduza o seguinte texto para português:\n\n{texto_original}"
            }
        ]
    )

    print("📝 Texto Original:")
    print(texto_original)
    print()
    print("🌍 Tradução:")
    print(response.choices[0].message.content)
    print()


def exemplo_3_resumo():
    """Exemplo 3: Resumir textos longos"""
    print("=" * 60)
    print("🆓 EXEMPLO 3: Resumo de Texto")
    print("=" * 60)
    print()

    texto_longo = """
    Inteligência artificial (IA) é um ramo da ciência da computação que se propõe
    a elaborar dispositivos que simulem a capacidade humana de raciocinar, perceber,
    tomar decisões e resolver problemas. A IA começou como um campo acadêmico em 1956
    e tem evoluído drasticamente desde então. Hoje, machine learning e deep learning
    são subcampos da IA que utilizam redes neurais para processar grandes quantidades
    de dados. Aplicações modernas incluem assistentes virtuais, carros autônomos,
    diagnósticos médicos, e muito mais. A IA está transformando indústrias inteiras
    e mudando a forma como vivemos e trabalhamos.
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": f"Resuma o seguinte texto em 3 pontos principais:\n\n{texto_longo}"
            }
        ]
    )

    print("📄 Resumo:")
    print(response.choices[0].message.content)
    print()


def exemplo_4_geracao_codigo():
    """Exemplo 4: Geração de código"""
    print("=" * 60)
    print("🆓 EXEMPLO 4: Geração de Código")
    print("=" * 60)
    print()

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": "Escreva uma função Python que verifica se um número é primo"
            }
        ]
    )

    print("💻 Código Gerado:")
    print(response.choices[0].message.content)
    print()


def exemplo_5_analise_dados():
    """Exemplo 5: Análise de dados"""
    print("=" * 60)
    print("🆓 EXEMPLO 5: Análise de Dados")
    print("=" * 60)
    print()

    dados = """
    Vendas Q1 2025:
    Janeiro: $50,000
    Fevereiro: $62,000
    Março: $58,000
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": f"Analise esses dados de vendas e forneça insights:\n\n{dados}"
            }
        ]
    )

    print("📊 Análise:")
    print(response.choices[0].message.content)
    print()


def exemplo_6_criacao_conteudo():
    """Exemplo 6: Criação de conteúdo"""
    print("=" * 60)
    print("🆓 EXEMPLO 6: Criação de Conteúdo")
    print("=" * 60)
    print()

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": "Escreva 3 ideias de posts para redes sociais sobre tecnologia"
            }
        ]
    )

    print("✍️ Ideias de Conteúdo:")
    print(response.choices[0].message.content)
    print()


def exemplo_7_conversacao_com_historico():
    """Exemplo 7: Conversação mantendo histórico"""
    print("=" * 60)
    print("🆓 EXEMPLO 7: Conversação com Histórico")
    print("=" * 60)
    print()

    # Histórico de mensagens
    messages = [
        {"role": "user", "content": "Olá! Meu nome é João e eu gosto de programação."},
    ]

    # Primeira interação
    response1 = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )
    print("👤 Você: Olá! Meu nome é João e eu gosto de programação.")
    print(f"🤖 GLM-4.5-Flash: {response1.choices[0].message.content}")
    print()

    # Adiciona resposta ao histórico
    messages.append({
        "role": "assistant",
        "content": response1.choices[0].message.content
    })

    # Segunda interação - teste de memória
    messages.append({
        "role": "user",
        "content": "Qual é o meu nome e o que eu gosto?"
    })

    response2 = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )
    print("👤 Você: Qual é o meu nome e o que eu gosto?")
    print(f"🤖 GLM-4.5-Flash: {response2.choices[0].message.content}")
    print()


def exemplo_8_streaming():
    """Exemplo 8: Streaming (resposta em tempo real)"""
    print("=" * 60)
    print("🆓 EXEMPLO 8: Streaming (Resposta em Tempo Real)")
    print("=" * 60)
    print()

    print("🤖 GLM-4.5-Flash (streaming): ", end="", flush=True)

    stream = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": "Conte uma história curta sobre um robô"}
        ],
        stream=True
    )

    for chunk in stream:
        if chunk.choices and len(chunk.choices) > 0:
            delta = chunk.choices[0].delta
            if hasattr(delta, 'content') and delta.content:
                print(delta.content, end="", flush=True)

    print("\n")


def exemplo_9_parametros_customizados():
    """Exemplo 9: Usando parâmetros customizados"""
    print("=" * 60)
    print("🆓 EXEMPLO 9: Parâmetros Customizados")
    print("=" * 60)
    print()

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": "Escreva um slogan criativo para uma empresa de tecnologia"}
        ],
        temperature=0.9,  # Mais criativo (0.0 = conservador, 1.0 = criativo)
        max_tokens=100,   # Limita tamanho da resposta
        top_p=0.9,        # Nucleus sampling
    )

    print("🎨 Resposta Criativa:")
    print(response.choices[0].message.content)
    print()
    print("⚙️ Parâmetros usados:")
    print("   • Temperature: 0.9 (mais criativo)")
    print("   • Max tokens: 100")
    print("   • Top P: 0.9")
    print()


def exemplo_10_multiplas_tarefas():
    """Exemplo 10: Múltiplas tarefas em uma mensagem"""
    print("=" * 60)
    print("🆓 EXEMPLO 10: Múltiplas Tarefas")
    print("=" * 60)
    print()

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": """
                Faça as seguintes tarefas:
                1. Traduza "Good morning" para português
                2. Calcule 15% de 200
                3. Dê uma dica de produtividade
                """
            }
        ]
    )

    print("📝 Respostas:")
    print(response.choices[0].message.content)
    print()


def main():
    """Executa todos os exemplos"""
    print("\n")
    print("🎉 EXEMPLOS PRÁTICOS - GLM-4.5-Flash (GRATUITO)")
    print("=" * 60)
    print("Este modelo é 100% GRATUITO!")
    print("Use quantas vezes quiser (respeitando rate limits)")
    print("=" * 60)
    print("\n")

    try:
        # Executa cada exemplo
        exemplo_1_chat_simples()
        exemplo_2_traducao()
        exemplo_3_resumo()
        exemplo_4_geracao_codigo()
        exemplo_5_analise_dados()
        exemplo_6_criacao_conteudo()
        exemplo_7_conversacao_com_historico()
        exemplo_8_streaming()
        exemplo_9_parametros_customizados()
        exemplo_10_multiplas_tarefas()

        print("=" * 60)
        print("✅ TODOS OS EXEMPLOS EXECUTADOS COM SUCESSO!")
        print("=" * 60)
        print()
        print("💡 DICAS:")
        print("   • Use temperature alta (0.7-1.0) para respostas criativas")
        print("   • Use temperature baixa (0.1-0.3) para respostas precisas")
        print("   • Use stream=True para respostas em tempo real")
        print("   • Mantenha histórico de mensagens para conversação")
        print("   • Limite: 2 requisições simultâneas")
        print()

    except Exception as e:
        print(f"\n❌ Erro: {e}\n")
        print("Verifique:")
        print("  • Arquivo .env com ZAI_API_KEY configurada")
        print("  • Conexão com internet")


if __name__ == "__main__":
    main()
