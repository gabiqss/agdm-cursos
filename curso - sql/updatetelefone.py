import sqlite3

conn = sqlite3.connect('curso.db')

nome = input('Insira seu nome: ')
def ler():
    cursor = conn.execute(f"SELECT id FROM matricula WHERE nome = '{nome}'")
    for i in cursor:
        print(i[0]) 

ler()

id = int(input('Digite o ID do aluno: '))
tel = input('Digite o seu telefone: ')

def update():
    conn.execute('UPDATE matricula SET telefone = (?) WHERE id = (?)', (tel, id))


    conn.commit()
    conn.close()

update()
