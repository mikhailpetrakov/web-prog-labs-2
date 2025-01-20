from flask import Flask, redirect, url_for, render_template
import os
from os import path
from flask_sqlalchemy import SQLAlchemy
from db import db

from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from lab8 import lab8


app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY','cекрет')
app.config['DB_TYPE'] = os.getenv('DB_TYPE','postgres')

if app.config['DB_TYPE']=='postgres':
    db_name = 'mikhail_petrakov_orm'
    db_user = 'mikhail_petrakov_orm'
    db_password = '123'
    host_ip = '127.0.0.1'
    host_port = 5432

    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{host_ip}:{host_port}/{db_name}'

else:
    dir_path = path.dirname(path.realpath(__file__))
    db_path = path.join(dir_path,"mikhail_petrakov_orm.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

db.init_app(app)

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)


@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)


@app.route("/menu")
def menu():
    return """
<!DOCTYPE html>
<html>
    <head>
        <title>НГТУ ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
        
        <ul>
            <li>
                <a href="/lab1">1 лабораторная</a>
            </li>
            <li>
                <a href="/lab2">2 лабораторная</a>
            </li>
            <li>
                <a href="/lab3">3 лабораторная</a>
            </li>
            <li>
                <a href="/lab4">4 лабораторная</a>
            </li>
            <li>
                <a href="/lab5">5 лабораторная</a>
            </li>
            <li>
                <a href="/lab6">6 лабораторная</a>
            </li>
            <li>
                <a href="/lab7">7 лабораторная</a>
            </li>
            <li>
                <a href="/lab8">8 лабораторная</a>
            </li>
        </ul>

        <footer>
            &copy; Михаил Петраков, ФБИ-23, 3 курс, 2024
        </footer>
    </body>
</html>
"""