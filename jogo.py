# Projeto 1 - Desenvolvimento de um jogo da forca em Python - Versão 1

# Importações

import random
from os import system, name

# Função para limpar a tela a cada execução

def limpa_tela():
    # Windows
    if name == "nt":
        _ = system("cls")
        
    # Mac/Linux    
    else:
        _ = system("clear")

# Função do jogo

def jogo():
    # 1. Mensagem de boas vindas
    print("\nBem-vindo(a) ao jogo da forca!")
    print("Advinhe a palavra abaixo:\n")
    
    # 2. Definir lista de palavras que podem ser advinhadas
    
    palavras = ["cenoura", "alface", "abobrinha", "quiabo", "acelga"]
    
    # 3. Escolha aleatória de uma palavra
    palavra = random.choice(palavras)
    
    # 4. Imprimir na tela o numero de letras da palavra. Retorno do numero de traços de acordo com o tabalho da palavra escolhida
    letras_descobertas = ["_" for letra in palavra]
    
    # 5. Definir o numero de chances que o usuário terá
    chances = len(palavra)
    
    # 6. Letras erradas
    
    letras_erradas = []
    
    #7. Repetir o processo até que a palavra tenha sido descoberta ou o numero de chances zere
    # Tentativa
    while chances >0:
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))
        
        tentativa = input("\n Digite uma letra: ").lower()
        
        # Condicional 1
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)
        
        # Condicional 2
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era:", palavra)
            break

        # Condicional 3
    if "_" in letras_descobertas:
        print("\n Você perdeu, a palavra era: ", palavra)   
      
# Bloco main
if __name__ == "__main__":
    jogo()
    