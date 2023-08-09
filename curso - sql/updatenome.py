import sqlite3

conn = sqlite3.connect('curso.db')
nome = input("Insira o seu nome: ")

def ler():
    cursor = conn.execute('SELECT id FROM matricula WHERE nome = ?', (nome,))
    for i in cursor:
        print(i[0]) 

ler()

id = int(input('Digite o ID do aluno: '))
novo_nome = input('Insira o seu nome: ')

def update():
    conn.execute('UPDATE matricula SET nome   = (?) WHERE id = (?)', (novo_nome, id))


    conn.commit()
    conn.close()

update()
