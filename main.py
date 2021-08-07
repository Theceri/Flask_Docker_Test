from flask import Flask, app, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy

from configs.base import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.route('/')
def index():
    return render_template('index.html')

