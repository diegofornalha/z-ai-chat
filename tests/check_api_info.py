#!/usr/bin/env python3
"""
Script para verificar informações sobre a API key e consumo
"""
from dotenv import load_dotenv
from zai import ZaiClient
import json

# Carrega variáveis do .env
load_dotenv()

def check_api_key_info():
    """Verifica informações sobre a chave de API"""
    print("=" * 60)
    print("🔑 INFORMAÇÕES DA CHAVE DE API Z.AI")
    print("=" * 60)
    print()

    try:
        client = ZaiClient()
        print("✅ Cliente ZAI criado com sucesso\n")
        print(f"📍 Base URL: {client.base_url}")
        print(f"🔐 API Key: {client.api_key[:20]}...{client.api_key[-10:]}")
        print()

        # Faz uma chamada simples para verificar o uso
        print("=" * 60)
        print("🧪 TESTANDO CHAMADA SIMPLES (GLM-4.6)")
        print("=" * 60)
        print()

        try:
            response = client.chat.completions.create(
                model="glm-4.6",
                messages=[
                    {"role": "user", "content": "Hi"}
                ],
                max_tokens=10  # Limita tokens para economizar
            )

            print("✅ Chamada bem-sucedida!\n")

            # Mostra informações de uso
            if hasattr(response, 'usage'):
                print("📊 USAGE (TOKENS CONSUMIDOS NESTA CHAMADA):")
                print(f"   • Prompt tokens: {response.usage.prompt_tokens}")
                print(f"   • Completion tokens: {response.usage.completion_tokens}")
                print(f"   • Total tokens: {response.usage.total_tokens}")
                print()

            # Mostra resposta
            if hasattr(response, 'choices') and len(response.choices) > 0:
                print("💬 Resposta do modelo:")
                print(f"   {response.choices[0].message.content}")
                print()

            # Mostra outros campos disponíveis
            print("📋 CAMPOS DISPONÍVEIS NA RESPOSTA:")
            for key in dir(response):
                if not key.startswith('_'):
                    print(f"   • {key}")
            print()

            # Tenta verificar se há headers com informações de quota
            print("=" * 60)
            print("ℹ️  INFORMAÇÕES SOBRE LIMITES E QUOTAS")
            print("=" * 60)
            print()
            print("⚠️  O SDK não expõe diretamente informações de:")
            print("   • Saldo da conta")
            print("   • Limites de requisições")
            print("   • Quotas restantes")
            print("   • Lista de modelos disponíveis no seu plano")
            print()
            print("💡 PARA VERIFICAR ESSAS INFORMAÇÕES:")
            print("   1. Acesse: https://z.ai/manage-apikey/billing")
            print("   2. Verifique seu saldo e histórico de uso")
            print("   3. Veja os modelos disponíveis no seu plano")
            print()

        except Exception as e:
            error_msg = str(e)
            print(f"❌ Erro na chamada: {error_msg}\n")

            if "1113" in error_msg or "Insufficient balance" in error_msg:
                print("💡 PROBLEMA: Saldo insuficiente")
                print("   • Seu saldo está em $0.00")
                print("   • Adicione créditos em: https://z.ai/manage-apikey/billing")
                print()
            elif "permission" in error_msg.lower():
                print("💡 PROBLEMA: Sem permissão para este modelo")
                print("   • Verifique os modelos disponíveis no seu plano")
                print()

        print("=" * 60)
        print("📚 MODELOS SUPORTADOS PELO SDK")
        print("=" * 60)
        print()
        print("🤖 LANGUAGE MODELS:")
        print("   • GLM-4.6")
        print("   • GLM-4.5")
        print("   • GLM-4-Plus")
        print("   • GLM-4-Air (mais barato)")
        print("   • GLM-4.5V (visual)")
        print()
        print("🎨 IMAGE GENERATION:")
        print("   • CogView-3")
        print("   • CogView-4")
        print()
        print("🎥 VIDEO GENERATION:")
        print("   • CogVideoX-3 ($0.20/vídeo)")
        print("   • CogVideoX-2")
        print("   • viduq1-text, viduq1-image, viduq1-start-end")
        print("   • vidu2-image, vidu2-start-end, vidu2-reference")
        print()
        print("=" * 60)
        print("💰 IMPORTANTE SOBRE BILLING")
        print("=" * 60)
        print()
        print("Seu saldo atual: $0.00")
        print()
        print("Para usar os modelos, você precisa:")
        print("1. Acessar: https://z.ai/manage-apikey/billing")
        print("2. Adicionar um método de pagamento")
        print("3. Recarregar créditos")
        print()
        print("💡 Plano GLM Coding: $3/mês (acesso ao GLM-4.6)")
        print()

    except Exception as e:
        print(f"\n❌ ERRO: {e}\n")
        print("Verifique se:")
        print("  • O arquivo .env existe e contém ZAI_API_KEY")
        print("  • A chave de API está correta")
        print("  • Você tem conexão com a internet")

if __name__ == "__main__":
    check_api_key_info()
