import conexao as conn

#Criar uma Tabela e Inserir Dados
""" Crie uma tabela chamada "clientes" com os campos: id (chave
primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns
registros de clientes na tabela. """


conn.cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INT PRIMARY KEY,
        nome VARCHAR(100),
        idade INT,
        saldo FLOAT
    );
''') 
#Junção de Tabelas
""" Crie uma segunda tabela chamada "compras" com os campos: id
(chave primária), cliente_id (chave estrangeira referenciando o id
da tabela "clientes"), produto (texto) e valor (real).  """

conn.cursor.execute('''
    CREATE TABLE IF NOT EXISTS compras (
        id INT PRIMARY KEY,
        cliente_id INT,
        produto VARCHAR(100),
        valor REAL,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    );
''')

conn.conexao.commit()
conn.conexao.close()