# quiz.py - Sistema de Quiz

import random
import time
from utils import limpar_tela, pausar
from nivel import calcular_nivel
from cadastro import carregar_usuarios, atualizar_usuarios
from datetime import datetime


def carregar_questoes(arquivo):
    """Carrega as questões do arquivo txt"""
    questoes = []
    
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            linhas = f.readlines()
            
            i = 0
            while i < len(linhas):
                linha = linhas[i].strip()
                
                # Ignora linhas vazias
                if not linha:
                    i += 1
                    continue
                
                # Linha com a pergunta
                pergunta = linha
                opcoes = []
                resposta = ""
                
                # Lê as 4 opções
                i += 1
                for j in range(4):
                    if i < len(linhas):
                        opcao = linhas[i].strip()
                        if opcao:
                            opcoes.append(opcao)
                        i += 1
                
                # Lê a resposta (próxima linha após as opções)
                if i < len(linhas):
                    resp_linha = linhas[i].strip()
                    if resp_linha.startswith("Resposta:") or resp_linha.startswith("Gabarito:"):
                        resposta = resp_linha.split(":")[-1].strip().lower()
                        i += 1
                
                # Se encontrou pergunta com 4 opções e resposta, adiciona
                if len(opcoes) == 4 and resposta:
                    questoes.append({
                        "pergunta": pergunta,
                        "opcoes": opcoes,
                        "resposta": resposta
                    })
                
                i += 1
    
    except FileNotFoundError:
        print(f"\n❌ Arquivo {arquivo} não encontrado!")
    
    return questoes


def carregar_quiz():
    """Mostra animação de carregamento do quiz"""
    limpar_tela()
    print("\n⏳ Carregando quiz", end="")
    for i in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print(" ✅")
    time.sleep(1)


def sortear_perguntas(tipo_nivel):
    """Sorteia 10 perguntas de acordo com o nível"""
    if tipo_nivel == "basico":
        questoes = carregar_questoes("questoes_basicas.txt")
    else:
        questoes = carregar_questoes("questoes_avancadas.txt")
    
    if len(questoes) < 10:
        print(f"\n⚠️  Atenção: Apenas {len(questoes)} questões disponíveis!")
        return questoes
    
    random.shuffle(questoes)
    return questoes[:10]


def salvar_respostas(usuario, perguntas, respostas_usuario, acertos):
    """Salva as respostas do usuário no arquivo respostas.txt"""
    with open("respostas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write("=" * 60 + "\n")
        arquivo.write(f"USUÁRIO: {usuario['nome']} ({usuario['email']})\n")
        arquivo.write(f"DATA: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        arquivo.write(f"NÍVEL: {calcular_nivel(usuario['minutos'])[0]}\n")
        arquivo.write(f"PONTUAÇÃO: {acertos}/10 ({acertos * 10}%)\n")
        arquivo.write("=" * 60 + "\n\n")
        
        for i, (pergunta, resposta) in enumerate(zip(perguntas, respostas_usuario), 1):
            correto = "✅" if resposta == pergunta["resposta"] else "❌"
            arquivo.write(f"PERGUNTA {i}: {pergunta['pergunta']}\n")
            arquivo.write(f"Resposta do usuário: {resposta.upper()} {correto}\n")
            arquivo.write(f"Resposta correta: {pergunta['resposta'].upper()}\n\n")
        
        arquivo.write("\n")


def mostrar_resultado(usuario, acertos):
    """Mostra o resultado final do quiz"""
    limpar_tela()
    print("=" * 50)
    print("📊  RESULTADO DO QUIZ")
    print("=" * 50)
    
    print(f"\n👤 {usuario['nome']}")
    print(f"✅ Acertos: {acertos}/10")
    print(f"📈 Pontuação: {acertos * 10}%")
    
    if acertos >= 8:
        print("\n🌟 EXCELENTE! Você é um expert em música!")
    elif acertos >= 6:
        print("\n👏 MUITO BOM! Continue aprendendo!")
    elif acertos >= 4:
        print("\n💪 BOM! Pratique mais para melhorar!")
    else:
        print("\n📚 Continue estudando! Você vai melhorar!")
    
    print("\n" + "=" * 50)
    print("💚  MENSAGEM MOTIVACIONAL  💚")
    print("=" * 50)
    print("\nCada pequena ação que você faz importa!")
    print("🌱 Ao aprender sobre sustentabilidade através")
    print("da música, você se torna parte da mudança!")
    print("🌍 Juntos, podemos criar um planeta melhor!")
    print("=" * 50)
    
    pausar()
    
    print("\n🎉 Obrigado por jogar! Continue tentando! 🎉\n")
    pausar()


def aplicar_quiz(usuario):
    """Aplica o quiz completo ao usuário"""
    nivel, tipo_nivel = calcular_nivel(usuario["minutos"])
    carregar_quiz()
    
    perguntas = sortear_perguntas(tipo_nivel)
    
    if len(perguntas) == 0:
        print("\n❌ Não há questões disponíveis!")
        pausar()
        return
    
    acertos = 0
    respostas_usuario = []
    
    limpar_tela()
    print("=" * 50)
    print(f"🎯  QUIZ MAKEMUSICGREEN - NÍVEL {nivel}")
    print("=" * 50)
    print(f"\n📝 Responda as {len(perguntas)} perguntas abaixo:\n")
    pausar()
    
    for i, questao in enumerate(perguntas, 1):
        limpar_tela()
        print(f"PERGUNTA {i}/{len(perguntas)}")
        print("=" * 50)
        print(f"\n{questao['pergunta']}\n")
        
        for opcao in questao['opcoes']:
            print(opcao)
        
        resposta = input("\nSua resposta (a/b/c/d): ").strip().lower()
        respostas_usuario.append(resposta)
        
        if resposta == questao['resposta']:
            print("✅ Correto!")
            acertos += 1
        else:
            print(f"❌ Errado! A resposta correta era: {questao['resposta']}")
        
        time.sleep(1.5)
    
    # Atualiza pontuação do usuário
    usuario["pontuacao"] = acertos
    usuarios = carregar_usuarios()
    for u in usuarios:
        if u["email"] == usuario["email"]:
            u["pontuacao"] = acertos
            break
    atualizar_usuarios(usuarios)
    
    # Salva as respostas
    salvar_respostas(usuario, perguntas, respostas_usuario, acertos)
    
    # Mostra resultado
    mostrar_resultado(usuario, acertos)