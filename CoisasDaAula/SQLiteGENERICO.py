import sqlite3 as sq

# Criação de DB
nomeDataBase = "DBZteste" + ".db"
connection = sq.connect(nomeDataBase)
cursor = connection.cursor()


# Função para criar Tabela x, recebe o nome da tabela e a statement SQL das colunas da tabela
def criaTabela(nomeTabela, colunasTabela1):
    cursor.execute("CREATE TABLE IF NOT EXISTS " + nomeTabela + "(" + colunasTabela1 +")")


# Função para adicionar elementos na Tabela alvo, recebe nome da tabela alvo e elementos para ser adicionado
def adicionaElementosNaTabela(tabelaAlvo,arg1):
    cursor.execute("INSERT INTO '" + tabelaAlvo + "' VALUES('"+ arg1 + "')")


# Função para adicionar elementos na Tabela alvo, recebe nome
def buscaElementosTabelaX(tabelaAlvo, coluna, metodo):
    if isinstance(metodo,str):
        response = cursor.execute("SELECT * FROM '" + tabelaAlvo + "' WHERE '" + coluna + "' LIKE '" + metodo + "'").fetchall()
    else:
        response = cursor.execute("SELECT * FROM '" + tabelaAlvo + "' WHERE '" + coluna + "' = ?",(metodo,)).fetchall()
    return response


# CASOS TESTE
criaTabela("Flamenguistas", "'nome' TEXT")
adicionaElementosNaTabela("Flamenguistas", "Wolff")
print(cursor.execute("SELECT * FROM Flamenguistas").fetchall())
print(buscaElementosTabelaX("Flamenguistas", "nome", "Wolff"))
print(cursor.execute("PRAGMA table_info(Flamenguistas)").fetchall())
