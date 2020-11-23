from flask import Flask, render_template

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


if __name__ == '__main__':
    app.run()
