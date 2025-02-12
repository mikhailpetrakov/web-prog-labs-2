from flask import Blueprint, render_template, request, redirect, url_for
lab9 = Blueprint('lab9', __name__)


@lab9.route('/lab9/')
def main():
    return render_template('lab9/index.html')

@lab9.route('/lab9/step1', methods=['POST'])
def step1():
    name = request.form.get('name')
    return render_template('lab9/step2.html', name=name)

@lab9.route('/lab9/step2', methods=['POST'])
def step2():
    name = request.form.get('name')
    age = request.form.get('age')
    return render_template('lab9/step3.html', name=name, age=age)

@lab9.route('/lab9/step3', methods=['POST'])
def step3():
    name = request.form.get('name')
    age = request.form.get('age')
    gender = request.form.get('gender')
    return render_template('lab9/step4.html', name=name, age=age, gender=gender)

@lab9.route('/lab9/step4', methods=['POST'])
def step4():
    name = request.form.get('name')
    age = request.form.get('age')
    gender = request.form.get('gender')
    preference1 = request.form.get('preference1')
    return render_template('lab9/step5.html', name=name, age=age, gender=gender, preference1=preference1)

@lab9.route('/lab9/step5', methods=['POST'])
def step5():
    name = request.form.get('name')
    age = request.form.get('age')
    gender = request.form.get('gender')
    preference1 = request.form.get('preference1')
    preference2 = request.form.get('preference2')
    return render_template('lab9/final.html', name=name, age=age, gender=gender, preference1=preference1, preference2=preference2)