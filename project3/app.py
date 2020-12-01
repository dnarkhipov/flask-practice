from flask import Flask, render_template, send_from_directory
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField


class MyForm(FlaskForm):
    name = StringField('name')
    email = StringField('email')
    promocode = StringField('promocode')
    accepted = BooleanField('accepted')


app = Flask(__name__)


# https://flask.palletsprojects.com/en/1.1.x/patterns/favicon/
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def main():
    return ''


if __name__ == '__main__':
    app.run()
