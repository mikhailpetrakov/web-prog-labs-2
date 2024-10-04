from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

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
        </ul>

        <footer>
            &copy; Михаил Петраков, ФБИ-23, 3 курс, 2024
        </footer>
    </body>
</html>
"""

@app.route("/lab1")
def lab1():
    return '''
<!DOCTYPE html>
<html>
    <head>
        <title>Петраков Михаил Вячеславович, лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') +'''">
    </head>
    <body class="body">
        <header class="header">
            НГТУ, ФБ, Лабораторная работа 1
        </header>
            <p class="text">
                Flask — фреймворк для создания веб-приложений на языке
                программирования Python, использующий набор инструментов
                Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
                называемых микрофреймворков — минималистичных каркасов
                веб-приложений, сознательно предоставляющих лишь самые ба-
                зовые возможности.
            </p>
            <ul class="text">
                <li>
                    <a href="/menu">Меню</a>
                </li>
            </ul>

            <h2>
                Реализованные роуты
            </h2>

            <ul class=text>
                <li>
                    <a href="/lab1/oak">Дуб</a>
                </li>
           
                <li>
                    <a href="/lab1/student">Студент</a>
                </li>
           
                <li>
                    <a href="/lab1/python">Python</a>
                </li>

                 <li>
                    <a href="/lab1/bioshock">BioShock</a>
                </li>
            </ul>
        <footer class="footer">
            &copy; Михаил Петраков, ФБИ-23, 3 курс, 2024
        </footer>
    </body>
</html>
'''
@app.route("/lab1/oak")
def oak():
    return '''
<!DOCTYPE html>
    <head>
       <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') +'''">
    </head>
<html>
    <body class="body">
        <h1 class="oak-title">Дуб</h1>
        <img class="image" src="''' + url_for('static', filename='oak.jpg')+'''">
    </body>
</html>
'''
@app.route("/lab1/student")
def student():
    return '''
<!DOCTYPE html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') +'''">
    </head>
<html>
    <body class="body">
        <h1 class="oak-title">Петраков Михаил Вячеславович</h1>
        <img class="png" src="''' + url_for('static', filename='nstu.png')+'''">
    </body>
</html>
'''

@app.route("/lab1/python")
def python():
    return '''
<!DOCTYPE html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') +'''">
    </head>
<html>
    <body class="body">
        <h1 class="oak-title">Язык программирования Python</h1>
        <div class="text">
            Python — это высокоуровневый язык программирования общего назначения.
            Его философия дизайна делает акцент на читаемости кода с использованием значительных отступов.
            Python — динамически типизированный язык с функцией сборки мусора. 
            Он поддерживает несколько парадигм программирования , включая структурированное (особенно процедурное ), 
            объектно-ориентированное и функциональное программирование. Его часто называют языком «с батарейками в комплекте»
            из-за его всеобъемлющей стандартной библиотеки.
        </div>
        <img class="png" src="''' + url_for('static', filename='python.png')+'''">
    </body>
</html>
'''

@app.route("/lab1/bioshock")
def bioshock():
    return '''
<!DOCTYPE html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') +'''">
    </head>
<html>
    <body class="body">
        <h1 class="oak-title">Bioshok Infinite</h1>
        <div class="text">
            <p>
                BioShock Infinite — компьютерная игра в жанре шутера от первого лица с элементами RPG, стимпанка и научной фантастики,
                разработанная студией Irrational Games под руководством геймдизайнера Кена Левина. 
                Игра была издана компанией 2K Games 26 марта 2013 года на трёх игровых платформах: Xbox 360, PlayStation 3
                и персональных компьютерах с операционной системой Microsoft Windows. Версия для операционной системы OS X, разработанная компанией Aspyr Media,
                была издана 29 августа 2013 года[3]. В России издателем игры выступила компания 1С-СофтКлаб. В 2016 году BioShock Infinite был переиздан на PlayStation 4,
                Xbox One в составе сборника BioShock: The Collection, а в 2020 году для Nintendo Switch.
            </p>
            <p>
                Сюжет игры основан на многомировой интерпретации квантовой механики, согласно которой каждый раз, 
                когда события могут пойти одним из нескольких возможных путей, мир разделяется на несколько параллельных миров, 
                в каждом из которых реализуется один из возможных исходов. Герои перемещаются между такими мирами, отличающимися тем, 
                что персонажи игры приняли в них разные ключевые решения в своей жизни. Действие игры происходит в 1912 году 
                в вымышленном летающем городе Колумбия. Главный герой, частный детектив Букер Девитт, проникает в город в поисках девушки по имени Элизабет. 
                Позже Букер и Элизабет оказываются в центре войны между властями города и мятежными рабочими. Благодаря сверхъестественной способности Элизабет 
                создавать «разрывы» между параллельными мирами герои раскрывают мрачные секреты города и своего собственного прошлого. 
                Игра BioShock Infinite не является продолжением предыдущих игр серии Bioshock. Однако, в DLC Burial at Sea: Episode 2 
                раскрывается сюжетная связь между городами Колумбия и Восторг.
            </p>
        </div>
        <img class="png" src="''' + url_for('static', filename='bioshock.png')+'''">
    </body>
</html>
'''

@app.route('/lab2/example')
def example():
    name = 'Михаил Петраков'
    number = '2'
    group =  'ФБИ-23'
    course = '3 курс'
    return render_template('example.html')
