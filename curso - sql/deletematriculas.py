import sqlite3

conn = sqlite3.connect('curso.db')

nome = input('Insira seu nome: ')

def ler():
    cursor = conn.execute('SELECT id FROM matricula WHERE nome = ?', (nome,))
    for i in cursor:
        print(i[0]) 

ler()

id = int(input('Digite o ID do aluno: '))

def delete():
    conn.execute('DELETE from matricula WHERE id = ?', (id,))
    conn.execute('DELETE from cursos WHERE idcurso = ?', (id,))
    conn.execute('DELETE from pagamentos WHERE idpagamento = ?', (id,))
    conn.execute('DELETE from avaliacao WHERE idaprovacao = ?', (id,))

    conn.commit()

delete()

conn.close()
