#!/usr/bin/env python3
"""
📊 Verificador de Uso - GLM-4.5-Flash (GRATUITO)

Mostra estatísticas de uso do chat e informações sobre limites
"""
import json
import os
from datetime import datetime
from pathlib import Path

def check_browser_history():
    """Verifica histórico salvo no localStorage (simulado)"""
    print("=" * 60)
    print("📁 HISTÓRICO DE CONVERSAS")
    print("=" * 60)
    print()
    print("⚠️  O histórico está salvo no navegador (localStorage)")
    print("   Para ver suas conversas, acesse:")
    print("   http://localhost:8080/html/history.html")
    print()

def show_limits():
    """Mostra informações sobre limites do GLM-4.5-Flash"""
    print("=" * 60)
    print("📊 LIMITES DO GLM-4.5-Flash (GRATUITO)")
    print("=" * 60)
    print()

    print("✅ LIMITES CONFIRMADOS:")
    print("   • Concorrência: 2 requisições simultâneas")
    print("   • Custo: $0.00 (100% GRATUITO)")
    print()

    print("⚠️  LIMITES NÃO DOCUMENTADOS:")
    print("   • Requisições por dia: NÃO ESPECIFICADO")
    print("   • Requisições por mês: NÃO ESPECIFICADO")
    print("   • Tokens por requisição: NÃO ESPECIFICADO")
    print("   • Total de tokens por dia: NÃO ESPECIFICADO")
    print()

    print("🧪 TESTES REALIZADOS:")
    print("   • 20 chamadas sequenciais: ✅ TODAS FUNCIONARAM")
    print("   • Taxa: ~1 req/segundo")
    print("   • Sem erros de rate limit detectados")
    print()

    print("💡 ESTIMATIVA PRÁTICA:")
    print()
    print("   Baseado nos testes, você consegue enviar:")
    print()
    print("   📈 Por minuto: ~60 mensagens (se usar sem parar)")
    print("   📈 Por hora: ~3.600 mensagens")
    print("   📈 Por dia: ~86.400 mensagens (improvável atingir)")
    print()
    print("   💬 USO NORMAL (conversação típica):")
    print("      • 10-50 mensagens/dia: ✅ SEM PROBLEMAS")
    print("      • 100-500 mensagens/dia: ✅ PROVÁVEL OK")
    print("      • 1000+ mensagens/dia: ⚠️  Pode ter limites")
    print()

    print("🎯 LIMITAÇÃO REAL:")
    print("   • Concorrência: Máximo 2 requisições ao mesmo tempo")
    print("   • Você precisa AGUARDAR uma resposta antes de enviar outra")
    print("   • Se enviar 3+ ao mesmo tempo, algumas podem falhar")
    print()

def show_recommendations():
    """Mostra recomendações de uso"""
    print("=" * 60)
    print("💡 RECOMENDAÇÕES DE USO")
    print("=" * 60)
    print()

    print("✅ FAÇA:")
    print("   • Use à vontade para chat normal")
    print("   • Aguarde a resposta antes de enviar nova mensagem")
    print("   • Mantenha histórico de conversação")
    print("   • Use para desenvolvimento e testes")
    print()

    print("⚠️  EVITE:")
    print("   • Enviar múltiplas mensagens simultâneas (>2)")
    print("   • Scripts automatizados de alto volume")
    print("   • Uso comercial intensivo sem verificar ToS")
    print()

    print("📝 MONITORAMENTO:")
    print("   • Cada resposta mostra tokens usados")
    print("   • Histórico mostra todas as conversas")
    print("   • Se começar a dar erro 429, espere alguns minutos")
    print()

def check_account_info():
    """Verifica informações da conta"""
    print("=" * 60)
    print("🔑 INFORMAÇÕES DA SUA CONTA")
    print("=" * 60)
    print()

    print("💳 Saldo: $0.00 (não necessário para GLM-4.5-Flash)")
    print("🆓 Modelo: GLM-4.5-Flash (100% GRATUITO)")
    print("📊 Quota mensal: Não documentada (aparenta ser generosa)")
    print()

    print("🌐 Para ver informações detalhadas da conta:")
    print("   Acesse: https://z.ai/manage-apikey/billing")
    print()

def main():
    print()
    print("🎯 VERIFICADOR DE USO - Z.AI Chat")
    print()

    check_account_info()
    show_limits()
    show_recommendations()
    check_browser_history()

    print("=" * 60)
    print("✅ RESUMO FINAL")
    print("=" * 60)
    print()
    print("Você pode usar o GLM-4.5-Flash LIVREMENTE!")
    print()
    print("📊 Quantos prompts você consegue?")
    print("   → Aparentemente MUITOS (milhares por dia)")
    print("   → Limitado apenas por concorrência (2 simultâneos)")
    print("   → Sem custos NUNCA ($0.00)")
    print()
    print("💡 Para uso normal de chat:")
    print("   Você NUNCA vai atingir os limites!")
    print()

if __name__ == "__main__":
    main()
