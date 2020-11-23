from flask import Flask, render_template
import data

app = Flask(__name__)


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


@app.route('/data')
def get_tours():
    # data.tours
    return 'список всех туров'


@app.route('/data/departures/<departure>')
def get_tour_by_departure(departure):
    return 'туры по направлению'


@app.route('/data/tours/<id>')
def get_tour_by_id(id):
    return 'тур по id'


if __name__ == '__main__':
    app.run()
