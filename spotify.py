# spotify.py - Funções relacionadas ao Spotify

from utils import limpar_tela, pausar
from cadastro import carregar_usuarios, atualizar_usuarios


def mostrar_instrucoes_spotify():
    """Mostra as instruções para obter tempo de música no Spotify"""
    limpar_tela()
    print("=" * 50)
    print("📱  COMO OBTER SEU TEMPO DE MÚSICA NO SPOTIFY")
    print("=" * 50)
    print("\n1️⃣  Abra o aplicativo do Spotify")
    print("2️⃣  Vá até seu perfil")
    print("3️⃣  Procure pela opção 'MÁQUINA DO TEMPO'")
    print("4️⃣  Lá você verá os minutos ouvidos no mês!")
    print("\n💡 Anote esse número e volte aqui para inserir!")
    print("=" * 50)
    pausar()


def inserir_minutos(usuario):
    """Permite o usuário inserir seus minutos de música ouvidos"""
    limpar_tela()
    print("=" * 50)
    print("⏱️  INSERIR TEMPO DE MÚSICA")
    print("=" * 50)
    
    try:
        minutos = int(input("\nQuantos MINUTOS você ouviu de música este mês? "))
        usuario["minutos"] = minutos
        
        # Atualiza o arquivo de usuários
        usuarios = carregar_usuarios()
        for u in usuarios:
            if u["email"] == usuario["email"]:
                u["minutos"] = minutos
                break
        atualizar_usuarios(usuarios)
        
        print(f"\n✅ {minutos} minutos registrados!")
    except:
        print("\n❌ Por favor, digite apenas números!")
        pausar()
        return False
    
    pausar()
    return True