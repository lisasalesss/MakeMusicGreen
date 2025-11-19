# nivel.py - Sistema de Níveis do Usuário

from utils import limpar_tela, pausar


def calcular_nivel(minutos):
    """Calcula o nível do usuário baseado nos minutos ouvidos"""
    if minutos <= 900:
        return "SILVER 🥈", "basico"
    elif minutos <= 1800:
        return "GOLD 🥇", "basico"
    else:
        return "DIAMOND 💎", "avancado"


def mostrar_nivel(usuario):
    """Mostra o nível atual do usuário"""
    limpar_tela()
    print("=" * 50)
    print("🏆  SEU NÍVEL DE USUÁRIO")
    print("=" * 50)
    
    nivel, tipo = calcular_nivel(usuario["minutos"])
    
    print(f"\n👤 Usuário: {usuario['nome']}")
    print(f"⏱️  Minutos ouvidos: {usuario['minutos']} min")
    print(f"🎖️  Seu nível é: {nivel}")
    
    print("\n📊 Tabela de Níveis:")
    print("   🥈 SILVER: 0 a 900 min (0 a 15h)")
    print("   🥇 GOLD: 901 a 1.800 min (16 a 30h)")
    print("   💎 DIAMOND: acima de 1.801 min (mais de 30h)")
    
    print("=" * 50)
    pausar()
    return tipo