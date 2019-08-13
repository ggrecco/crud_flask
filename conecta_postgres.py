import psycopg2

con = psycopg2.connect(host="localhost",
                       port="5433",
                       database="teste",
                       user="postgres",
                       password="123")

cur = con.cursor()

# selecionar todos os dados da tabela
cur.execute("select * from esse.tb_esse")

# inserir dados na tabela
# cur.execute('insert into esse.tb_esse (id, esse_nome) values (%s,%s)',(2,"testador"))
# con.commit()

# exibir usuarios no terminal
usuarios = cur.fetchall()

for u in usuarios:
    print("id={} | login={} | nome={} | senha={}".format(
        u[0], u[1], u[2], u[3]))

con.close()