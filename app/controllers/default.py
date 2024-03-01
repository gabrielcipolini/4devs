from app.models.users_db import Users
from app import app
from flask import render_template, redirect, request
from flask_login import LoginManager, login_user, current_user
import sqlite3


login_manager = LoginManager(app)


@app.route("/")
def index():
    # try:
    #     current_user.name
    #     return "Logado"
    # except AttributeError:
    return render_template("index.html")


@login_manager.user_loader
def load_user(user_id):
    print("ENTROU")
    with sqlite3.connect('instance\\test.db') as conexao:
        print("ENTROU")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM user WHERE username = ?", (user_id,))
        user_data = cursor.fetchone()
        if user_data:
            name = user_data[1]
            is_admin = user_data[3]
            print("CHEGOU ATÈ AQUI")
            if is_admin == "True":
                return Users(name=name, trouth=True)
            else:
                return Users(name=name)
        else:
            print("CHEGOU ATÈ AQUI")
            return None


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        nome = request.form.get("name")
        senha = request.form.get("senha")

        with sqlite3.connect('instance\\test.db') as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM user WHERE username = ? \
                           AND password = ?", (nome, senha))
            user_data = cursor.fetchone()

        if user_data:
            name, _ = user_data[1], user_data[2]
            user = load_user(name)
            login_user(user)
            return redirect("/")

    return 'Usuário ou senha incorretos. Tente novamente.'
