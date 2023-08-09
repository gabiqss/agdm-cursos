import sqlite3

conn = sqlite3.connect('curso.db')

nome = input('Insira seu nome: ')

def ler():
    cursor = conn.execute('SELECT id FROM matricula WHERE nome = ?', (nome,))
    for i in cursor:
        print(i[0]) 

ler()

id = int(input('Digite o ID do aluno: '))

print('Opções de turno\n1 - Matutino\n2 - Vespertino\n3 - Noturno')

turno = int(input('Insira seu turno: '))

if turno == 1:
    b = "Matutino"
elif turno == 2:
    b = "Vespertino"
else:
    b = "Noturno"

def update():
    conn.execute('UPDATE cursos SET turno   = (?) WHERE idcurso = (?)', (b, id))


    conn.commit()
    conn.close()

update()
