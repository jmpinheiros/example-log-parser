import pyodbc

# string de conexão
conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};' \
           'SERVER=myserver;DATABASE=mydatabase;' \
           'UID=myusername;PWD=mypassword'

# estabelece conexão
conn = pyodbc.connect(conn_str)

# cria cursor
cursor = conn.cursor()

# exemplo de consulta
cursor.execute('SELECT * FROM mytable')

# exibe resultado
for row in cursor.fetchall():
    print(row)

# fecha conexão
conn.close()
