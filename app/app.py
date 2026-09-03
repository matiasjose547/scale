from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)


def conectar_banco():

    return psycopg2.connect(
    
    )


@app.route("/")
def index():

    try:

        conexao = conectar_banco()

        cursor = conexao.cursor()

        cursor.execute("""
            SELECT version();
        """)

        resultado = cursor.fetchone()

        cursor.close()
        conexao.close()

        return render_template(
            "index.html",
            banco=resultado[0]
        )

    except Exception as erro:

        return f"""
        <h1>Erro ao conectar ao PostgreSQL</h1>
        <p>{erro}</p>
        """, 500


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )