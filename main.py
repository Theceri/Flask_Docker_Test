from flask import Flask, app, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from configs.base import DevelopmentConfig


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


@app.before_first_request
def create_tables():
    db.create_all()

db = SQLAlchemy(app)

from models.User import User


@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html')

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