
from boas_vindas import boas_vindas
from cadastro import cadastrar_usuario, fazer_login
from spotify import mostrar_instrucoes_spotify, inserir_minutos
from nivel import mostrar_nivel
from quiz import aplicar_quiz
from utils import limpar_tela, pausar


def menu_principal():
    while True:
        limpar_tela()
        print("●" * 50)
        print("🎵  MAKEMUSICGREEN - MENU PRINCIPAL")
        print("●" * 50)
        print("\n1️⃣  Cadastrar novo usuário")
        print("2️⃣  Fazer login")
        print("3️⃣  Sair")
        print("●" * 50)
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            usuario = fazer_login()
            if usuario:
                menu_usuario(usuario)
        elif opcao == "3":
            limpar_tela()
            print("\n👋 Obrigado por usar o MakeMusicGreen!")
            print("🌍 Juntos por um planeta melhor! 🌱\n")
            break
        else:
            print("\n❌ Opção inválida!")
            pausar()


def menu_usuario(usuario):
    while True:
        limpar_tela()
        print("●" * 50)
        print(f"👤  OLÁ, {usuario['nome'].upper()}!")
        print("●" * 50)
        print("\n1️⃣  Ver instruções do Spotify")
        print("2️⃣  Inserir minutos de música")
        print("3️⃣  Ver meu nível")
        print("4️⃣  Fazer quiz")
        print("5️⃣  Voltar ao menu principal")
        print("●" * 50)
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            mostrar_instrucoes_spotify()
        elif opcao == "2":
            inserir_minutos(usuario)
        elif opcao == "3":
            if usuario["minutos"] > 0:
                mostrar_nivel(usuario)
            else:
                print("\n⚠️  Você precisa inserir seus minutos primeiro!")
                pausar()
        elif opcao == "4":
            if usuario["minutos"] > 0:
                aplicar_quiz(usuario)
            else:
                print("\n⚠️  Você precisa inserir seus minutos primeiro!")
                pausar()
        elif opcao == "5":
            break
        else:
            print("\n❌ Opção inválida!")
            pausar()


if __name__ == "__main__":
    boas_vindas()

    menu_principal()

