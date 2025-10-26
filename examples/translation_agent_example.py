#!/usr/bin/env python3
"""
🌍 Translation Agent Example - Inglês → Português Brasileiro

Demonstra o uso do agente de tradução geral da Z.AI
com foco em traduções do inglês para português brasileiro.

Agente: General Translation Agent
Idioma origem: EN (Inglês)
Idioma destino: PT (Português Brasileiro)
Custo: $3.00 por 1M tokens (~$0.00003 por tradução curta)

💡 Para outros idiomas, altere os parâmetros:
   source_lang: en, zh, ja, ko, fr, de, es, ru, ar, pt
   target_lang: en, zh, ja, ko, fr, de, es, ru, ar, pt
"""
from dotenv import load_dotenv
from zai import ZaiClient

# Carrega variáveis de ambiente (.env)
load_dotenv()


def translate_text_sync():
    """Exemplo de tradução de inglês para português brasileiro com streaming"""
    client = ZaiClient()

    print("=" * 60)
    print("🌍 TRADUÇÃO COM STREAMING (EN → PT-BR)")
    print("=" * 60)
    print()

    print("📝 Texto original (EN): 'Hello, how are you today?'")
    print("🎯 Traduzindo para: Português Brasileiro (PT)")
    print()
    print("💬 Tradução: ", end="", flush=True)

    response = client.agents.invoke(
        agent_id="general_translation",
        stream=True,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Hello, how are you today?"
                    }
                ]
            }
        ],
        custom_variables={
            "source_lang": "en",  # Inglês
            "target_lang": "pt"   # Português Brasileiro
        }
    )

    for chunk in response:
        print(chunk, end="", flush=True)
    print("\n")


def translate_text_no_stream():
    """Exemplo de tradução de inglês para português sem streaming"""
    client = ZaiClient()

    print("=" * 60)
    print("🌍 TRADUÇÃO SEM STREAMING (EN → PT-BR)")
    print("=" * 60)
    print()

    print("📝 Texto original (EN): 'Good morning! Have a wonderful day!'")
    print("🎯 Traduzindo para: Português Brasileiro (PT)")
    print()

    response = client.agents.invoke(
        agent_id="general_translation",
        stream=False,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Good morning! Have a wonderful day!"
                    }
                ]
            }
        ],
        custom_variables={
            "source_lang": "en",  # Inglês
            "target_lang": "pt"   # Português Brasileiro
        }
    )

    print("💬 Tradução:", response)
    print()


def translate_multiple_texts_to_pt():
    """Exemplo de traduzir múltiplas frases do inglês para português"""
    client = ZaiClient()

    print("=" * 60)
    print("🌍 MÚLTIPLAS TRADUÇÕES EN → PT-BR")
    print("=" * 60)
    print()

    texts = [
        "Good morning! Have a great day!",
        "Thank you very much for your help.",
        "I love learning new things every day.",
        "The weather is beautiful today.",
        "Could you please help me with this?"
    ]

    for i, text in enumerate(texts, 1):
        print(f"📝 {i}. Original: '{text}'")
        print(f"   Tradução: ", end="", flush=True)

        response = client.agents.invoke(
            agent_id="general_translation",
            stream=True,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": text
                        }
                    ]
                }
            ],
            custom_variables={
                "source_lang": "en",
                "target_lang": "pt"
            }
        )

        for chunk in response:
            print(chunk, end="", flush=True)
        print()
        print()

    print()


def main():
    """Executa todos os exemplos de tradução"""
    print("\n")
    print("🎯 EXEMPLOS DO TRANSLATION AGENT")
    print("=" * 60)
    print()
    print("ℹ️  INFORMAÇÕES:")
    print("   • Agent ID: general_translation")
    print("   • Idiomas suportados: 10")
    print("   • EN, ZH, JA, KO, FR, DE, ES, RU, AR, PT")
    print("   • Streaming: Suportado")
    print("   • Custo: $3.00 por 1M tokens")
    print()

    # Exemplo 1: Com streaming (EN → PT-BR)
    translate_text_sync()

    # Exemplo 2: Sem streaming (EN → PT-BR)
    translate_text_no_stream()

    # Exemplo 3: Múltiplas frases (EN → PT-BR)
    translate_multiple_texts_to_pt()

    print("=" * 60)
    print("✅ TODOS OS EXEMPLOS EXECUTADOS COM SUCESSO!")
    print("=" * 60)
    print()
    print("💡 DICAS:")
    print("   • Use stream=True para ver tradução em tempo real")
    print("   • Use stream=False para tradução completa de uma vez")
    print("   • Suporta textos longos")
    print("   • Custo: ~$0.00003 por tradução curta (muito barato!)")
    print()
    print("🌍 OUTROS IDIOMAS:")
    print("   Para traduzir para outros idiomas, altere:")
    print("   target_lang: en, zh, ja, ko, fr, de, es, ru, ar, pt")
    print()


if __name__ == "__main__":
    main()
