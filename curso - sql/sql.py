import sqlite3

conn = sqlite3.connect('curso.db')


def tabelas():

    conn.execute('''CREATE TABLE IF NOT EXISTS matricula (
                id INTEGER NOT NULL,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                telefone TEXT NOT NULL,
                cpf TEXT NOT NULL,
                PRIMARY KEY (id)
                    )
                ''')

    conn.execute('''CREATE TABLE IF NOT EXISTS cursos (
                idcurso INTEGER NOT NULL,
                curso TEXT NOT NULL,
                turno TEXT NOT NULL,
                FOREIGN KEY (idcurso) REFERENCES matricula(id)
                    )
                ''')

    conn.execute('''CREATE TABLE IF NOT EXISTS pagamentos (
                idpagamento INTEGER NOT NULL,
                fdpagamento TEXT NOT NULL,
                FOREIGN KEY (idpagamento) REFERENCES matricula(id)
            )''')

    conn.execute('''CREATE TABLE IF NOT EXISTS avaliacao (
                idaprovacao INTEGER NOT NULL,
                aprovacao TEXT NOT NULL,
                FOREIGN KEY (idaprovacao) REFERENCES matricula(id)
                 )
    ''')

    conn.commit()

    conn.close()


t = tabelas()
t
