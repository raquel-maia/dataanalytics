import sqlite3

conexao = sqlite3.connect('/Users/raque/Desktop/bancosql/banco')
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')
#cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')
#cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('DROP TABLE produtos') como excluir uma tabela completa
#cursor.execute('CREATE TABLE gerentes(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('INSERT INTO gerentes(id,nome,endereco,email) VALUES (4, "João","INGLATERRA","cici@gmail")')

#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES (1, "Raquel","Brazil","raquel@gmail", 1234)')
#cursor.execute('INSERT INTO gerentes(id,nome,endereco,email,telefone) VALUES (8, "Cintia","Inglaterra","ci@gmail")')
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES (1, "Daniel","SP","raquel@gmail", 1234)')
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES (1, "Maria","CEARA","raquel@gmail", 1234)')
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES (1, "Jose","SALVADOR","raquel@gmail", 1234)')
#cursor.execute('DELETE FROM usuario where nome="Jose"')

#dados = cursor.execute('SELECT * FROM usuario') # visualizar infos   * é tudo ou os dados como nome, telefone
#for usuario in dados:
    #print (usuario) #para cada usuario que estiver em dado mostre 

#cursor.execute('UPDATE usuario SET endereco="Minas gerais" WHERE nome="Maria"')#atualizar dados

#dadosOrder = cursor.execute('SELECT * FROM usuario ORDER BY nome, endereco DESC')#ordernar dados
#for usuario in dadosOrder:
    #print(usuario)

#LIMIT E DISTINCT
#dados = cursor.execute('SELECT * FROM usuario LIMIT 2')# para limitar o numero de informações por página
#for usuario in dados:
    #print(usuario)

    #DISTINCT SÓ TRAZER VALORES DIFERENTES
#dados = cursor.execute('SELECT DISTINCT * FROM usuario')
#for usuario in dados:
    #print(usuario)

#GROUP BY HAVING
#for usuario in dados:
    #print(usuario)

# JOIN TIPOS RIGHT, LEFT, FULL e INNER (QUANDO QUEREMOS RETORNAR INFORMAÇÃO DE MAIS DE UMA TABELA)
# INNER JOIN PEGA TODAS AS LINHAS COM CORRESPONDECIA PARA AMBAS TABELAS
#dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerentes ON usuario.nome = gerentes.nome')

#JOIN - LEFT JOOIN ELE PEGA OS DADOS DA TABELA ESQUERDA E DEPOIS COLOCA DA TABELA DIREITO SE FOREM ZINDETIFICADO IGUAL SE NAO FOREM IGUAIS ELE PREENCHE COM NONE
#dados = cursor.execute('SELECT * FROM usuario LEFT JOIN gerentes ON usuario.nome = gerentes.nome')

#JOIN - RIGHT JOOIN ELE PEGA OS DADOS DA TABELA DIREITA E DEPOIS COLOCA DA TABELA DIREITO SE FOREM INDETIFICADO IGUAL SE NAO FOREM IGUAIS ELE PREENCHE COM NONE
#dados = cursor.execute('SELECT * FROM usuario RIGHT JOIN gerentes ON usuario.nome = gerentes.nome')

#FULL JOIN ELE COMPARA AS INFOS IGUAIS EM TODOS OS LADOS
#dados = cursor.execute('SELECT * FROM usuario FULL JOIN gerentes ON usuario.nome = gerentes.nome')

#SUB-CONSULTAS SUB SELECT OU SUB QUERY - CONSULTAS SQL QUE SAO ALIADAS DENTRO DA CONSULTA PRINCIPAL , E UTILIZANDO O RESULTADO DE CONSULTA. PEGAR INFOS QUE ESTEJA EM OUTRA TABELA TAMBEM
dados = cursor.execute('SELECT * FROM usuario WHERE nome IN (SELECT nome FROM gerentes)')
for usuario in dados:
    print(usuario)

conexao.commit()
conexao.close