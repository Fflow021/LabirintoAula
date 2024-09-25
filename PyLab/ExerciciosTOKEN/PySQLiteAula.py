import sqlite3 as sq

# Cria a dataBase de nome "teste.db" e também o objeto connection que representa a conexão entre maquina e dataBase em disco
connection = sq.connect("teste.db")
# Pra executar QUERYS SQL é preciso de um cursor de database, aqui se cria o objeto cursor
cursor = connection.cursor()
query = "CREATE TABLE IF NOT EXISTS Aluno(nome TEXT, matricula INTEGER, CPF INTEGER, CURSO TEXT, PERIODO INTEGER)"
# cursor.execute() executa uma query passada como parametro, nesse caso a string query acima
cursor.execute(query)

# Função que adiciona um elemento na tabela que passada como primeiro parametro
def adicionarAluno(nomeTabela, alunoNome, matricula, cpf, curso, periodo):
    cursor.execute("INSERT INTO '" + nomeTabela + "'VALUES('" + alunoNome + "','" + str(matricula)

                   + "','" + str(cpf) + "','" + curso + "','" + str(periodo) + "')")
# Função que busca um elemento na tabela Aluno
def buscarAluno(metodo):
    if isinstance(metodo,str):
        response = cursor.execute("SELECT * FROM Aluno WHERE nome LIKE '" + metodo +"'").fetchall()
    else:
        response = cursor.execute("SELECT * FROM Aluno WHERE matricula = ?", (metodo,)).fetchall()
    return response


# Chamadas dos métodos pra teste
adicionarAluno('Aluno',"Wolff",202404620123,10020030045,"ADS","4")
print(buscarAluno("Wolff") + ["print através do nome"])
print(buscarAluno(202404620123) + ["print através da matrícula"])

