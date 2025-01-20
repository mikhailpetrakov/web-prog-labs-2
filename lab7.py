from flask import Blueprint,render_template,request, redirect, session
lab7 = Blueprint('lab7',__name__)

@lab7.route('/lab7/')
def main():
    return render_template('lab7/index.html')

films = [
    {
        "title":"1+1",
        "title_ru":"1+1",
        "year":2011,
        "description":"Аристократ на коляске нанимает в сиделки бывшего заключенного. Искрометная французская комедия с Омаром Си"
    },
    {
        "title":"Джентльмены",
        "title_ru":"The Gentlemen",
        "year":2019,
        "description":"Один ушлый американец ещё с студенческих лет приторговывал наркотиками, а теперь придумал схему нелегального обогащения с использованием поместий обедневшей английской аристократии и очень неплохо на этом разбогател. Другой пронырливый журналист приходит к Рэю, правой руке американца, и предлагает тому купить киносценарий, в котором подробно описаны преступления его босса при участии других представителей лондонского криминального мира — партнёра-еврея, китайской диаспоры, чернокожих спортсменов и даже русского олигарха."
    },
    {
        "title":"Достать ножи",
        "title_ru":"Knives Out",
        "year":2019,
        "description":"На следующее утро после празднования 85-летия известного автора криминальных романов Харлана Тромби виновника торжества находят мёртвым. Налицо — явное самоубийство, но полиция по протоколу опрашивает всех присутствующих в особняке членов семьи, хотя, в этом деле больше заинтересован частный детектив Бенуа Блан. Тем же утром он получил конверт с наличными от неизвестного и заказ на расследование смерти Харлана. Не нужно быть опытным следователем, чтобы понять, что все приукрашивают свои отношения с почившим главой семейства, но Блану достаётся настоящий подарок — медсестра покойного, которая физически не выносит ложь."
    },
    {
        "title":"Остров проклятых ",
        "title_ru":"Shutter Island",
        "year":2019,
        "description":"Два американских судебных пристава отправляются на один из островов в штате Массачусетс, чтобы расследовать исчезновение пациентки клиники для умалишенных преступников. При проведении расследования им придется столкнуться с паутиной лжи, обрушившимся ураганом и смертельным бунтом обитателей клиники."
    },
]

@lab7.route('/lab7/rest-api/films/',methods=['GET'])
def get_films():
    return films

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
        if id <= (len(films)-1):
            return films[id]
        else:
            return {"error": "Film not found"}, 404
        
@lab7.route('/lab7/rest-api/films/<int:id>',methods=['DELETE'])
def del_film(id):
    if id <= (len(films)-1):
        del films[id]
        return '',204
    else:
        return {"error": "Film not found"}, 404
    
@lab7.route('/lab7/rest-api/films/<int:id>',methods=['PUT'])
def put_film(id):
    film = request.get_json()
    if id <= (len(films)-1):
        films[id] = film
        return film[id]
    else:
        return {"error": "Film not found"}, 404
    
@lab7.route('/lab7/rest-api/films/',methods=['POST'])
def add_film():
    new_film = request.get_json()
    films.append(new_film)
    return {'id':len(films)-1},201