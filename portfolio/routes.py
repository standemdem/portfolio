from portfolio import app
from flask import render_template, redirect, url_for, flash, request

@app.route('/')
@app.route('/home_page')
def home_page():
    return render_template('home.html')