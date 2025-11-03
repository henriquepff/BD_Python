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
   # cursor.execute("delete from empregados where id_emp = %s", (8,))
   # cursor.execute("delete from empregados where id_emp = %s", (7,))

    empregados = [(7,),(8,)]

    cursor.executemany("delete from empregados where id_emp = %s", empregados)

    conn.commit()
    print("Registros excluídos com sucesso!")

except Exception as e:
    print("Erro ao excluir registros:", e)
    conn.rollback()
    
# Fechando conexões
if cursor:
    cursor.close()
if conn:
    conn.close()
