import psycopg2

try:
    conn = psycopg2.connect(
        dbname="empresabd",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )

    cursor = conn.cursor()

    cursor.execute("INSERT INTO cargos (nome_cargo) VALUES (%s)", ('Analista de Dados',))

    cursor.execute("INSERT INTO departamentos (nome_dept) VALUES (%s)", ('Pesquisa e Desenvolvimento',))

    cursor.execute("DELETE FROM empregados WHERE id_emp = %s", (12,))

    cursor.execute("UPDATE empregados SET pr_nome= %s WHERE id_emp= %s", ('João Paulo', 1))

    conn.commit()
    print("Operações realizadas com sucesso!")

except Exception as e:
    print("Erro ao executar operações: ", e)
    conn.rollback()

if cursor:
    cursor.close()
if conn:
    conn.close()