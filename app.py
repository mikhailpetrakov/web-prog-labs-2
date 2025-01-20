from flask import Flask, redirect, url_for, render_template
import os
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7


app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY','cекрет')
app.config['DB_TYPE'] = os.getenv('DB_TYPE','postgres')

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)


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
                <a href="/lab6">7 лабораторная</a>
            </li>
        </ul>

        <footer>
            &copy; Михаил Петраков, ФБИ-23, 3 курс, 2024
        </footer>
    </body>
</html>
"""