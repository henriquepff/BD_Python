import psycopg2

try:
 # Conectando ao banco de dados
    conn = psycopg2.connect(
    dbname="empresabd", # substituir pelos dados do seu banco
    user="postgres", 
    password="admin", 
    host="localhost", 
    port="5432" 
    )
 # Criando o cursor
    cursor = conn.cursor()
 # Executando o SELECT
    cursor.execute("""
    SELECT id_emp, matricula, pr_nome, sobre_nome, sexo, salario, comissao
    FROM empregados
    """)
# Recuperando os resultados
    resultados = cursor.fetchall()
 # Exibindo os dados
    for res in resultados:
        print(f"ID: {res[0]}, Matrícula: {res[1]}, Nome: {res[2]} {res[3]}, Sexo: {res[4]}, Salário: R${res[5]}, Comissão: {res[6]}")

except Exception as e:
    print("Erro ao acessar o banco:", e)
# Fechando conexões
if cursor:
    cursor.close()
if conn:
    conn.close()
