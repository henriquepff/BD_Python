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
    cursor.execute("update empregados set salario = %s, comissao = %s where id_emp = %s", (5500,400,3))

    conn.commit()
    print("Empregado atualizado com sucesso!")

except Exception as e:
    print("Erro ao atualizar empregado:", e)
    conn.rollback()
    
# Fechando conexões
if cursor:
    cursor.close()
if conn:
    conn.close()
