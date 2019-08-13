from flask import Flask
import psycopg2

app = Flask(__name__)

db = 'postgresql://postgres:123@localhost:5433/teste'
conn = psycopg2.connect(db)
cursor = conn.cursor()


@app.route('/')
def listar():
    cursor.execute("select * from esse.tb_esse")
    usuarios = cursor.fetchall()
    print(usuarios)
    return 'lista'


if __name__ == "__main__":
    app.run(debug=True)