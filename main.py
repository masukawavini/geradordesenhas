import random
import string

def gerarSenha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(comprimento))
    return senha

comprimento = int(input("Digite o comprimento da senha desejada: "))
senhaGerada = gerarSenha(comprimento)

print("Senha gerada:", senhaGerada)
