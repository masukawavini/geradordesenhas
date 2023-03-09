import random
import string
import sqlite3

conexao = sqlite3.connect('senhas.db')

conexao.execute('''
        CREATE TABLE IF NOT EXISTS Senhas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            senha TEXT NOT NULL
        );
''')

def gerarSenha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(comprimento))
    return senha

comprimento = int(input("Digite o comprimento da senha desejada: "))
senhaGerada = gerarSenha(comprimento)

conexao.execute("INSERT INTO Senhas (senha) VALUES (?)", (senhaGerada,))
conexao.commit()

print("Senha gerada:", senhaGerada)
