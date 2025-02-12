from flask import Blueprint, render_template, request, redirect, url_for, session
lab9 = Blueprint('lab9', __name__)


@lab9.route('/lab9/')
def main():
    if 'name' in session and 'age' in session and 'gender' in session and 'preference1' in session :
        return redirect(url_for('lab9.step5'))
    return render_template('lab9/index.html')

@lab9.route('/lab9/step1', methods=['POST'])
def step1():
    session['name'] = request.form.get('name')
    return render_template('lab9/step2.html')

@lab9.route('/lab9/step2', methods=['POST'])
def step2():
    session['age'] = request.form.get('age')
    return render_template('lab9/step3.html')

@lab9.route('/lab9/step3', methods=['POST'])
def step3():
    session['gender'] = request.form.get('gender')
    return render_template('lab9/step4.html')

@lab9.route('/lab9/step4', methods=['POST'])
def step4():
    session['preference1'] = request.form.get('preference1')
    return render_template('lab9/step5.html')

@lab9.route('/lab9/step5', methods=['POST','GET'])
def step5():
    if session.get('preference2') == None:
        session['preference2'] = request.form.get('preference2')
        
    preference2 = session.get('preference2')
    name = session.get('name')
    age = session.get('age')
    gender = session.get('gender')
    preference1 = session.get('preference1')
    
    return render_template('lab9/final.html', name=name, age=age, gender=gender, preference1=preference1, preference2=preference2)

@lab9.route('/lab9/reset')
def reset():
    # Очищаем сессию и перенаправляем на главную страницу
    session.clear()
    return redirect(url_for('lab9.main'))