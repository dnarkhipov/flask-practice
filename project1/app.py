import os
from flask import Flask, render_template, send_from_directory
import data


app = Flask(__name__)


# https://flask.palletsprojects.com/en/1.1.x/patterns/favicon/
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def main():
    # return 'здесь будет Главная'
    return render_template('index.html')


@app.route('/departures/<departure>/')
def departures(departure):
    # return 'здесь будет Направление'
    return render_template('departure.html')


@app.route('/tours/<id>/')
def tours(id):
    # return 'здесь будет Тур'
    return render_template('tour.html')


@app.route('/data/')
def get_tours():
    # return 'список всех туров'
    response = ['<h1>Все туры:</h1>']

    for id, tour in data.tours.items():
        response.append(f'<p>{tour["country"]}: <a href="/data/tours/{id}/">{tour["title"]} {tour["price"]} {tour["stars"]}* </a></p>')

    return ' '.join(response)


@app.route('/data/departures/<departure>')
def get_tour_by_departure(departure):
    # return 'туры по направлению'
    if departure not in data.departures.keys():
        return f"Код отправления '{departure}' не найден.", 404

    response = [f'<h1>Туры по направлению {data.departures[departure]}:</h1>']
    for id, tour in {id: t for id, t in data.tours.items() if t['departure'] == departure}.items():
        response.append(f'<p>{tour["country"]}: <a href="/data/tours/{id}/">{tour["title"]} {tour["price"]} {tour["stars"]}* </a></p>')

    return ' '.join(response)


@app.route('/data/tours/<id>/')
def get_tour_by_id(id):
    # return 'тур по id'
    tour = data.tours.get(int(id), None)
    if tour is None:
        return f'Тур id={id} не найден', 404

    response = [
        f'<h1>{tour["country"]}: {tour["title"]} {tour["price"]}:</h1>',
        f'<p>{tour["nights"]} ночей</p>',
        f'<p>Стоимость: {tour["price"]} Р</p>',
        f'<p>{tour["description"]}</p>'
    ]

    return ' '.join(response)


if __name__ == '__main__':
    app.run()
