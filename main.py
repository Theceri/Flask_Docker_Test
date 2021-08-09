from flask import Flask, app, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

from configs.base import DevelopmentConfig
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    try:
        db.create_all()
        print('tryied and tested')
    except Exception as e:
        print('failed:', e)


from models.User import User


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', users = User.query.all())

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']

        new_user = User(first_name = first_name, last_name = last_name, email = email)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('register.html')