import sqlite3

conexao = sqlite3.connect('/Users/raque/Desktop/bancosql/banco')
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (1,"Raquel",31,"Programação");')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (2,"Joana",19,"Matematica");')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (3,"Maria",21,"Data Analytics");')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (4,"Ana",25,"Recursos Humanos");')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (5,"Lia",26,"Marketing");')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (6,"Alice",18,"Engenharia");')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES (6,"Daniel",24,"Engenharia");')

#Consultas Básicas SQL

#a) Selecionar todos os registros da tabela "alunos".

#registro = cursor.execute('SELECT * FROM alunos')
#for alunos in registro:
    #print(alunos)

# Selecionar o nome e a idade dos alunos com mais de 20 anos.
registro = cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20')
for alunos in registro:
    print(alunos)

# Selecionar os alunos do curso de "Engenharia" em ordem alfabética.

registro = cursor.execute('SELECT nome FROM alunos WHERE curso = "Engenharia" ORDER BY nome ASC')
for alunos in registro:
    print(alunos)

conexao.commit()
conexao.close