import conexao as conn

#Consultas Básicas SQL

#a) Selecionar todos os registros da tabela "alunos".

all_register = conn.cursor.execute('SELECT * FROM alunos')
for alunos in all_register:
    print(alunos)

# Selecionar o nome e a idade dos alunos com mais de 20 anos.
filter_idade = conn.cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20')
for alunos in filter_idade:
    print(alunos)

# Selecionar os alunos do curso de "Engenharia" em ordem alfabética.

order_curso = conn.cursor.execute('SELECT nome FROM alunos WHERE curso = "Engenharia" ORDER BY nome ASC')
for alunos in order_curso:
    print(alunos)

#Contar o número total de alunos na tabela
count_total = conn.cursor.execute('SELECT COUNT(*) FROM alunos')
for alunos in count_total:
    print(alunos)

# Atualização e Remoção 
#a) Atualize a idade de um aluno específico na tabela.
up_date = conn.cursor.execute('UPDATE alunos SET idade=35 WHERE idade==26')
for alunos in up_date:
    print(alunos)
#b) Remova um aluno pelo seu ID.
delete_date = conn.cursor.execute('DELETE FROM alunos WHERE id==6')
for alunos in delete_date:
    print(alunos)


#6. Consultas e Funções Agregadas
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
filter_age = conn.cursor.execute('SELECT nome, idade FROM clientes WHERE idade>30')
for clientes in filter_age:
    print(clientes)
#b) Calcule o saldo médio dos clientes.
count_avg= conn.cursor.execute('SELECT AVG(saldo) FROM clientes')
for clientes in count_avg:
    print("Saldo médio dos clientes:", clientes[0])
#c) Encontre o cliente com o saldo máximo.
count_max = conn.cursor.execute('SELECT MAX(saldo) FROM clientes')
for cliente in count_max:
    print("Saldo máximo dos clientes é:", clientes[0])

#d) Conte quantos clientes têm saldo acima de 1000
count_saldo = conn.cursor.execute('SELECT COUNT(*) AS total_clientes FROM clientes WHERE saldo > 1000')
for clientes in count_saldo:
    print(clientes)

#7. Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.
update_saldo = conn.cursor.execute('UPDATE clientes SET saldo=150 WHERE nome=="Raquel"')
for clientes in update_saldo:
    print(clientes)

# b) Remova um cliente pelo seu ID
rm_cliente = conn.cursor.execute('DELETE FROM clientes WHERE id==4')
for clientes in rm_cliente:
    print(clientes)

#Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra
client_buy = conn.cursor.execute('''
    SELECT clientes.nome, compras.produto, compras.valor 
    FROM compras 
    INNER JOIN clientes ON compras.cliente_id = clientes.id
''')

for compra in client_buy:
    print(compra)

conn.conexao.commit()
conn.conexao.close