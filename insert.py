import conexao as conn


#5. Criar uma Tabela e Inserir Dados do tipo primary key

conn.cursor.execute('''
    INSERT INTO clientes (
        id,
        nome,
        idade,
        saldo
    ) VALUES 
        (
            1,
            "Raquel",
            31,
            124.5
        ),
        (
            2,
            "Maria",
            25,
            106.9
        ),
        (
            4,
            "João",
            18,
            96.92
''');


conn.cursor.execute('''
    INSERT INTO compras (
        id,
        cliente_id,
        produto,
        valor
    ) VALUES 
        (
            1,
            1,
            "computador",
            900
        ),
        (
            2,
            2,
            "mesa",
            320
        ),
        (
            3,
            4,
            "bolsa",
            230
        );
''')

conn.conexao.commit()
conn.conexao.close