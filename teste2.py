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
    cursor.execute("SELECT e.pr_nome || ' ' || e.sobre_nome AS nome_funcionario, c.nome_cargo, d.nome_dept FROM empregados e JOIN cargos c ON e.id_cargo = c.id_cargo JOIN departamentos d ON e.id_dept = d.id_dept;")
# Recuperando os resultados
    resultados = cursor.fetchall()
 # Exibindo os dados
    for nome, cargo, departamento in resultados:
        print(f"Funcionário: {nome} | Cargo: {cargo} | Departamento: {departamento}")

except Exception as e:
    print("Erro ao acessar o banco:", e)
# Fechando conexões
if cursor:
    cursor.close()
if conn:
    conn.close()
