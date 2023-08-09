import sqlite3

conn = sqlite3.connect('curso.db')

nome = input('Insira seu nome: ')

def ler():
    cursor = conn.execute('SELECT id FROM matricula WHERE nome = ?', (nome,))
    for i in cursor:
        print(i[0]) 

ler()

id = int(input('Digite o ID do aluno: '))

email = input('Insira o seu e-mail: ')

def update():
    conn.execute('UPDATE matricula SET email = (?) WHERE id = (?)', (email, id))


    conn.commit()
    conn.close()

update()
