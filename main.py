from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/test')
def index():
    return render_template('happy_birthday.html')

@app.route('/gift')
def gift():
    return render_template('gift.html')


@app.route('/quest')
def quest():

    return 'wq'


@app.route('/aboutwe')
def aboutwe():
    return render_template('aboutwe.html')


@app.route('/aboutyou')
def aboutyou():
    return render_template('aboutyou.html')
