#!/usr/bin/env python3
"""
Script para testar os MODELOS GRATUITOS da Z.AI
Estes modelos NÃO consomem créditos!
"""
from dotenv import load_dotenv
from zai import ZaiClient

# Carrega variáveis do .env
load_dotenv()

def test_free_text_model():
    """Testa o GLM-4.5-Flash (GRATUITO)"""
    print("=" * 60)
    print("🆓 TESTANDO GLM-4.5-Flash (MODELO DE TEXTO GRATUITO)")
    print("=" * 60)
    print()

    try:
        client = ZaiClient()

        response = client.chat.completions.create(
            model="glm-4.5-flash",
            messages=[
                {"role": "user", "content": "Hello! Can you write a short poem about AI?"}
            ]
        )

        print("✅ SUCESSO! Modelo gratuito funcionando!\n")
        print("📝 Resposta:")
        print(response.choices[0].message.content)
        print()

        if hasattr(response, 'usage'):
            print("📊 Tokens usados (GRÁTIS):")
            print(f"   • Input: {response.usage.prompt_tokens}")
            print(f"   • Output: {response.usage.completion_tokens}")
            print(f"   • Total: {response.usage.total_tokens}")
        print()

        return True

    except Exception as e:
        print(f"❌ Erro: {e}\n")
        return False


def test_free_image_model():
    """Testa o CogView-3-Flash (GRATUITO)"""
    print("=" * 60)
    print("🆓 TESTANDO CogView-3-Flash (GERAÇÃO DE IMAGEM GRATUITA)")
    print("=" * 60)
    print()

    try:
        client = ZaiClient()

        response = client.images.generations(
            model="cogview-3-flash",
            prompt="A cute cat playing with a ball of yarn"
        )

        print("✅ SUCESSO! Imagem gerada gratuitamente!\n")

        if hasattr(response, 'data') and len(response.data) > 0:
            print("🖼️ Imagem gerada:")
            print(f"   URL: {response.data[0].url}")
        print()

        return True

    except Exception as e:
        error_msg = str(e)
        print(f"❌ Erro: {error_msg}\n")

        if "Unknown Model" in error_msg or "1211" in error_msg:
            print("💡 O modelo 'cogview-3-flash' pode ter outro nome.")
            print("   Tente: 'cogview-flash' ou 'cogview-3'")

        return False


def test_free_video_model():
    """Testa o CogVideoX-Flash (GRATUITO)"""
    print("=" * 60)
    print("🆓 TESTANDO CogVideoX-Flash (GERAÇÃO DE VÍDEO GRATUITA)")
    print("=" * 60)
    print()

    try:
        client = ZaiClient()

        response = client.videos.generations(
            model="cogvideox-flash",
            prompt="A cat walking in a garden",
            quality="speed",
            size="1280x720",
            fps=30
        )

        print("✅ SUCESSO! Vídeo iniciado gratuitamente!\n")
        print(f"📋 Task ID: {response.id}")
        print(f"📊 Status: {response.task_status}")
        print()
        print("⏳ Aguarde alguns minutos para o vídeo ser gerado.")
        print("   Verifique o status usando o task_id acima.")
        print()

        return True

    except Exception as e:
        error_msg = str(e)
        print(f"❌ Erro: {error_msg}\n")

        if "Unknown Model" in error_msg or "1211" in error_msg:
            print("💡 O modelo 'cogvideox-flash' pode ter outro nome.")
            print("   Modelos de vídeo gratuitos podem ainda estar em beta.")

        return False


def main():
    print("🎉 TESTANDO MODELOS GRATUITOS DA Z.AI")
    print("=" * 60)
    print()
    print("Estes modelos NÃO consomem créditos do seu saldo!")
    print("Você pode usá-los ILIMITADAMENTE (respeitando rate limits)")
    print()

    # Testa modelo de texto gratuito
    test_free_text_model()

    print("\n")

    # Testa modelo de imagem gratuito
    test_free_image_model()

    print("\n")

    # Testa modelo de vídeo gratuito
    test_free_video_model()

    print("=" * 60)
    print("📋 RESUMO DE MODELOS GRATUITOS")
    print("=" * 60)
    print()
    print("✅ GLM-4.5-Flash (texto) - GRÁTIS")
    print("   Limite: 2 requisições simultâneas")
    print()
    print("⚠️ CogView-3-Flash (imagem) - GRÁTIS")
    print("   Verifique se está disponível na sua conta")
    print()
    print("⚠️ CogVideoX-Flash (vídeo) - GRÁTIS")
    print("   Pode estar em beta/limitado")
    print()
    print("💡 MODELOS PAGOS MAIS BARATOS:")
    print("   • GLM-4.5-Air: $0.20 input / $1.10 output (por 1M tokens)")
    print("   • GLM-4-32B: $0.10 input / $0.10 output (por 1M tokens)")
    print("   • CogView-4: $0.01 por imagem")
    print("   • CogVideoX-3: $0.20 por vídeo")
    print()


if __name__ == "__main__":
    main()
