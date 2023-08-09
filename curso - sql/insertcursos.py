import sqlite3

conn = sqlite3.connect('curso.db')

nome = input('Insira seu nome: ')

print('Opções de curso\n1 - Matemática\n2 - Geografia\n3 - Inglês')


curso = int(input('Insira seu curso: '))

if curso == 1:
    a = "Matemática"
elif curso == 2:
    a = "Geografia"
else:
    a = "Inglês"


print('Opções de turno\n1 - Matutino\n2 - Vespertino\n3 - Noturno')

turno = int(input('Insira seu turno: '))

if turno == 1:
    b = "Matutino"
elif turno == 2:
    b = "Vespertino"
else:
    b = "Noturno"

def insert():
    conn.execute("INSERT INTO cursos (curso, turno, idcurso) VALUES (?, ?, (SELECT id FROM matricula WHERE nome = ?))", (a, b, nome))

    conn.commit()

    conn.close

insert()