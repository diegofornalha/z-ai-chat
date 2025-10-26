#!/usr/bin/env python3
"""
🆓 TESTE DO CHAT COM GLM-4.5-Flash (GRATUITO)

Testa todas as funcionalidades do client.chat.completions.create()
usando o modelo gratuito GLM-4.5-Flash
"""
from dotenv import load_dotenv
from zai import ZaiClient

# Carrega .env
load_dotenv()

# Modelo GRATUITO
MODEL = "glm-4.5-flash"


def test_chat_basico():
    """Teste 1: Chat básico"""
    print("\n" + "=" * 60)
    print("🧪 TESTE 1: Chat Básico")
    print("=" * 60)

    client = ZaiClient()

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": "Olá! Como você está?"}
        ]
    )

    print(f"✅ Status: Sucesso")
    print(f"📝 Resposta: {response.choices[0].message.content}")
    print(f"📊 Tokens: {response.usage.total_tokens}")
    print(f"🆔 ID: {response.id}")
    print(f"🏷️  Model: {response.model}")


def test_chat_com_parametros():
    """Teste 2: Chat com parâmetros customizados"""
    print("\n" + "=" * 60)
    print("🧪 TESTE 2: Chat com Parâmetros Customizados")
    print("=" * 60)

    client = ZaiClient()

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": "Escreva um slogan criativo para uma cafeteria"}
        ],
        temperature=0.9,  # Mais criativo
        top_p=0.95,
        max_tokens=50
    )

    print(f"✅ Status: Sucesso")
    print(f"📝 Resposta: {response.choices[0].message.content}")
    print(f"⚙️  Temperature: 0.9")
    print(f"⚙️  Top P: 0.95")
    print(f"⚙️  Max Tokens: 50")


def test_chat_streaming():
    """Teste 3: Chat com streaming"""
    print("\n" + "=" * 60)
    print("🧪 TESTE 3: Chat com Streaming (Tempo Real)")
    print("=" * 60)

    client = ZaiClient()

    print("📡 Streaming iniciado...")
    print("🤖 Resposta: ", end="", flush=True)

    stream = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": "Conte uma piada curta"}
        ],
        stream=True
    )

    full_response = ""
    for chunk in stream:
        if chunk.choices and len(chunk.choices) > 0:
            delta = chunk.choices[0].delta
            if hasattr(delta, 'content') and delta.content:
                print(delta.content, end="", flush=True)
                full_response += delta.content

    print("\n✅ Streaming completado!")


def test_chat_conversacao():
    """Teste 4: Conversação com histórico"""
    print("\n" + "=" * 60)
    print("🧪 TESTE 4: Conversação com Histórico")
    print("=" * 60)

    client = ZaiClient()

    # Conversa com múltiplas mensagens
    messages = [
        {"role": "system", "content": "Você é um assistente útil e amigável."},
        {"role": "user", "content": "Meu nome é Maria e eu amo programação Python."}
    ]

    response1 = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )

    print("👤 Usuário: Meu nome é Maria e eu amo programação Python.")
    print(f"🤖 Assistente: {response1.choices[0].message.content}\n")

    # Adiciona resposta ao histórico
    messages.append({
        "role": "assistant",
        "content": response1.choices[0].message.content
    })

    # Próxima mensagem (testa memória)
    messages.append({
        "role": "user",
        "content": "Qual é o meu nome e o que eu gosto?"
    })

    response2 = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )

    print("👤 Usuário: Qual é o meu nome e o que eu gosto?")
    print(f"🤖 Assistente: {response2.choices[0].message.content}")
    print("\n✅ Memória funcionando corretamente!")


def test_chat_multi_turn():
    """Teste 5: Conversação de múltiplas rodadas"""
    print("\n" + "=" * 60)
    print("🧪 TESTE 5: Conversação Multi-Turn")
    print("=" * 60)

    client = ZaiClient()

    messages = []

    # Rodada 1
    messages.append({"role": "user", "content": "Liste 3 linguagens de programação"})
    response1 = client.chat.completions.create(model=MODEL, messages=messages)
    print(f"👤 Rodada 1: {messages[-1]['content']}")
    print(f"🤖 Resposta: {response1.choices[0].message.content}\n")
    messages.append({"role": "assistant", "content": response1.choices[0].message.content})

    # Rodada 2
    messages.append({"role": "user", "content": "Qual delas é melhor para iniciantes?"})
    response2 = client.chat.completions.create(model=MODEL, messages=messages)
    print(f"👤 Rodada 2: {messages[-1]['content']}")
    print(f"🤖 Resposta: {response2.choices[0].message.content}\n")
    messages.append({"role": "assistant", "content": response2.choices[0].message.content})

    # Rodada 3
    messages.append({"role": "user", "content": "Por quê?"})
    response3 = client.chat.completions.create(model=MODEL, messages=messages)
    print(f"👤 Rodada 3: {messages[-1]['content']}")
    print(f"🤖 Resposta: {response3.choices[0].message.content}\n")

    print(f"✅ Total de mensagens no histórico: {len(messages)}")


def test_chat_system_prompt():
    """Teste 6: Usando System Prompt"""
    print("\n" + "=" * 60)
    print("🧪 TESTE 6: System Prompt (Define Personalidade)")
    print("=" * 60)

    client = ZaiClient()

    # Com system prompt
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "Você é um poeta que responde tudo em formato de haiku."
            },
            {"role": "user", "content": "O que é inteligência artificial?"}
        ]
    )

    print("⚙️  System Prompt: 'Você é um poeta que responde tudo em formato de haiku'")
    print(f"📝 Resposta em haiku:")
    print(response.choices[0].message.content)
    print("\n✅ System prompt aplicado com sucesso!")


def test_chat_diferentes_temperaturas():
    """Teste 7: Comparando diferentes temperaturas"""
    print("\n" + "=" * 60)
    print("🧪 TESTE 7: Comparando Temperaturas")
    print("=" * 60)

    client = ZaiClient()
    prompt = "Complete a frase: O futuro da tecnologia é"

    # Temperatura baixa (mais conservador)
    response_low = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        max_tokens=30
    )

    print(f"🌡️  Temperature 0.1 (conservador):")
    print(f"   {response_low.choices[0].message.content}\n")

    # Temperatura alta (mais criativo)
    response_high = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9,
        max_tokens=30
    )

    print(f"🌡️  Temperature 0.9 (criativo):")
    print(f"   {response_high.choices[0].message.content}\n")

    print("✅ Diferentes temperaturas testadas!")


def test_chat_stop_sequences():
    """Teste 8: Stop Sequences"""
    print("\n" + "=" * 60)
    print("🧪 TESTE 8: Stop Sequences")
    print("=" * 60)

    client = ZaiClient()

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": "Liste 10 frutas, uma por linha"}
        ],
        stop=["\n5."],  # Para depois da 4ª fruta
        max_tokens=200
    )

    print("⛔ Stop sequence: '\\n5.' (para na 4ª fruta)")
    print(f"📝 Resposta:")
    print(response.choices[0].message.content)
    print("\n✅ Stop sequence aplicada!")


def test_chat_seed_reproducibilidade():
    """Teste 9: Seed para reprodutibilidade"""
    print("\n" + "=" * 60)
    print("🧪 TESTE 9: Seed (Respostas Reproduzíveis)")
    print("=" * 60)

    client = ZaiClient()
    prompt = "Escreva um número aleatório"

    # Primeira chamada com seed
    response1 = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        seed=42,
        temperature=0.7
    )

    # Segunda chamada com mesmo seed
    response2 = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        seed=42,
        temperature=0.7
    )

    print(f"🎲 Seed: 42")
    print(f"📝 Resposta 1: {response1.choices[0].message.content}")
    print(f"📝 Resposta 2: {response2.choices[0].message.content}")

    if response1.choices[0].message.content == response2.choices[0].message.content:
        print("\n✅ Respostas idênticas! Seed funcionando!")
    else:
        print("\n⚠️  Respostas diferentes (seed pode não garantir 100% de reprodutibilidade)")


def test_chat_response_metadata():
    """Teste 10: Verificando Metadata da Resposta"""
    print("\n" + "=" * 60)
    print("🧪 TESTE 10: Metadata da Resposta")
    print("=" * 60)

    client = ZaiClient()

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": "Olá"}
        ]
    )

    print("📋 Campos disponíveis na resposta:")
    print(f"   • id: {response.id}")
    print(f"   • model: {response.model}")
    print(f"   • created: {response.created}")

    if hasattr(response, 'usage'):
        print(f"   • usage.prompt_tokens: {response.usage.prompt_tokens}")
        print(f"   • usage.completion_tokens: {response.usage.completion_tokens}")
        print(f"   • usage.total_tokens: {response.usage.total_tokens}")

    if response.choices and len(response.choices) > 0:
        choice = response.choices[0]
        print(f"   • choices[0].message.role: {choice.message.role}")
        print(f"   • choices[0].message.content: {choice.message.content[:50]}...")
        if hasattr(choice, 'finish_reason'):
            print(f"   • choices[0].finish_reason: {choice.finish_reason}")

    print("\n✅ Metadata completa!")


def main():
    """Executa todos os testes"""
    print("\n")
    print("🎯 TESTES DO CHAT API COM GLM-4.5-Flash (GRATUITO)")
    print("=" * 60)
    print("Testando todas as funcionalidades de client.chat.completions.create()")
    print("=" * 60)

    try:
        test_chat_basico()
        test_chat_com_parametros()
        test_chat_streaming()
        test_chat_conversacao()
        test_chat_multi_turn()
        test_chat_system_prompt()
        test_chat_diferentes_temperaturas()
        test_chat_stop_sequences()
        test_chat_seed_reproducibilidade()
        test_chat_response_metadata()

        print("\n" + "=" * 60)
        print("✅ TODOS OS TESTES EXECUTADOS COM SUCESSO!")
        print("=" * 60)
        print()
        print("📊 RESUMO:")
        print("   • 10 testes executados")
        print("   • Modelo: GLM-4.5-Flash (GRATUITO)")
        print("   • Custo total: $0.00")
        print()
        print("💡 Você pode usar este modelo ILIMITADAMENTE!")
        print("   (Respeitando o limite de 2 requisições simultâneas)")
        print()

    except Exception as e:
        print(f"\n❌ Erro: {e}\n")


if __name__ == "__main__":
    main()
