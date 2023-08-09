import sqlite3

conn = sqlite3.connect('curso.db')
nome = input('Insira o nome do aluno: ')
aprovacao= input('Aluno aprovado?(S/N) ').upper()
aprovado = True if aprovacao == 'S' else False
if aprovado == True:
    a = "Aprovado"
else:
    a = "Reprovado"

    
def insert():
    conn.execute('INSERT INTO avaliacao (idaprovacao, aprovacao) VALUES ((SELECT id FROM matricula WHERE nome = ?), ?)', (nome, a))
    conn.commit()
    conn.close()

insert()
