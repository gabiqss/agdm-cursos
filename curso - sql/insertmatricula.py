import sqlite3

conn = sqlite3.connect('curso.db')

nome = input("Insira seu nome: ")
email = input('Insira o seu e-mail: ')
tel = input('Insira o seu telefone: ')
cpf = input('Digite o seu cpf: ')

def insert():
    conn.execute("INSERT INTO matricula (nome, email, telefone, cpf) VALUES (?, ?, ?, ?)", (nome, email, tel, cpf))

    conn.commit()
    conn.close()


insert()