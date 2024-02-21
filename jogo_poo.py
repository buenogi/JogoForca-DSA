# Projeto 1 - Desenvolvimento de um jogo da forca em Python - Versão 2
# Com utilização dos conceitos de programação orientada a objetos
import random 
################################### Criação da classe ################################


class Jogo():
    
    def __init__(self):
        
        # Atributos  
        palavras = ["cenoura", "alface", "abobrinha", "quiabo", "acelga"]
        self.palavra = random.choice(palavras) # definição da palavra
        self.chances = len(self.palavra)-2     # definição do nº de chances
        self.letrasCorretas = ["_" for letra in self.palavra] # estrutura de advinhação da palavra

    # Método para adivinhar a letra
    
    def board(self):
        print(" ".join(self.letrasCorretas))

    def tentativa(self, tentativa):
        letras_erradas = []
           
        if tentativa in self.palavra:
            index = 0
            for letra in self.palavra:
                if tentativa == letra:
                    self.letrasCorretas[index] = letra
                index += 1
            print(" ".join(self.letrasCorretas))
        else:
            self.chances -= 1 
            letras_erradas.append(tentativa)
            print("\nErrou!\n")
            
    # Método para verificar se o jogo terminou
    
    def statusJogo(self):
        if "_" not in self.letrasCorretas:
            print("\nVocê venceu! A palavra era:", self.palavra)
            cond_cont = 0
        elif "_" in self.letrasCorretas and self.chances == 0:
            print("\n Você perdeu! A palavra era: ", self.palavra)
            cond_cont = 0
        else:
            print(f"\nAgora você tem apenas {self.chances} chances\n")
            cond_cont = 1
        return(cond_cont) 


########################### Jogo principal ##########################

if __name__ == "__main__":
    print("Bem-vindo(a) ao Jogo da Forca!\n")
    print("Você terá algumas tentativas para adivinhar uma palavra sorteada\n")
    
    jogada1 = Jogo()
    status = 1
    
    while status == 1:
        jogada1.board()
        x = str(input("\nInforme uma letra: "))   
        jogada1.tentativa(x)
        status = jogada1.statusJogo()
    

