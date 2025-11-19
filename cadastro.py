
from utils import limpar_tela, pausar
import os


def carregar_usuarios():
    usuarios = []
    
    if not os.path.exists("usuarios.txt"):
        return usuarios
    
    with open("usuarios.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            if linha.strip():
                partes = linha.strip().split("|")
                if len(partes) == 5:
                    usuario = {
                        "nome": partes[0],
                        "email": partes[1],
                        "senha": partes[2],
                        "minutos": int(partes[3]),
                        "pontuacao": int(partes[4])
                    }
                    usuarios.append(usuario)
    
    return usuarios


def salvar_usuario(usuario):
    with open("usuarios.txt", "a", encoding="utf-8") as arquivo:
        linha = f"{usuario['nome']}|{usuario['email']}|{usuario['senha']}|{usuario['minutos']}|{usuario['pontuacao']}\n"
        arquivo.write(linha)


def atualizar_usuarios(usuarios):
    with open("usuarios.txt", "w", encoding="utf-8") as arquivo:
        for usuario in usuarios:
            linha = f"{usuario['nome']}|{usuario['email']}|{usuario['senha']}|{usuario['minutos']}|{usuario['pontuacao']}\n"
            arquivo.write(linha)


def cadastrar_usuario():
    limpar_tela()
    print("●" * 50)
    print("📝  CADASTRO DE USUÁRIO")
    print("●" * 50)
    
    nome = input("\nDigite seu nome: ").strip()
    email = input("Digite seu email: ").strip()
    senha = input("Digite uma senha: ").strip()
    
    usuarios = carregar_usuarios()
    
    for usuario in usuarios:
        if usuario["email"] == email:
            print("\n❌ Este email já está cadastrado!")
            pausar()
            return None
    
    novo_usuario = {
        "nome": nome,
        "email": email,
        "senha": senha,
        "minutos": 0,
        "pontuacao": 0
    }
    
    salvar_usuario(novo_usuario)
    print(f"\n✅ Cadastro realizado com sucesso! Bem-vindo(a), {nome}!")
    pausar()
    return novo_usuario


def fazer_login():
    limpar_tela()
    print("●" * 50)
    print("🔐  LOGIN")
    print("●" * 50)
    
    email = input("\nDigite seu email: ").strip()
    senha = input("Digite sua senha: ").strip()
    
    usuarios = carregar_usuarios()
    
    for usuario in usuarios:
        if usuario["email"] == email and usuario["senha"] == senha:
            print(f"\n✅ Login realizado! Bem-vindo(a) de volta, {usuario['nome']}!")
            pausar()
            return usuario
    
    print("\n❌ Email ou senha incorretos!")
    pausar()

    return None
