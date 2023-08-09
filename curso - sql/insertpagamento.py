import sqlite3

conn = sqlite3.connect('curso.db')

nome = input('Insira seu nome: ')

print('Opções de pagamento\n1 - PIX\n2 - Débito\n3 - Crédito\n4 - Dinheiro\n5 - Boleto')

fdpagamento = int(input('Escolha sua forma de pagamento: '))

if fdpagamento == 1:
    a = 'PIX'
elif fdpagamento == 2:
    a = 'Débito'
elif fdpagamento == 3:
    a = 'Crédito'
elif fdpagamento == 4:
    a = 'Dinheiro'
else:
    a = 'Boleto'

def insert():
    conn.execute('INSERT INTO pagamentos (fdpagamento, idpagamento) VALUES (?, (SELECT id FROM matricula WHERE nome = ?))', (a, nome))

    conn.commit()

    conn.close()

insert()