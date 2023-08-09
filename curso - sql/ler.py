import sqlite3

conn = sqlite3.connect('curso.db')


def select():
    cursor = conn.execute('SELECT matricula.nome, pagamentos.fdpagamento, cursos.curso, cursos.turno, avaliacao.aprovacao \
                 FROM matricula \
                 INNER JOIN pagamentos ON matricula.id=pagamentos.idpagamento \
                 INNER JOIN cursos ON matricula.id=cursos.idcurso \
                 INNER JOIN avaliacao ON matricula.id=avaliacao.idaprovacao')
    for i in cursor:
        print(i)
    conn.close()

select()