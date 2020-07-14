from flask import Flask, render_template, redirect, url_for, request, make_response

app = Flask(__name__)


@app.route('/open')
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


@app.route('/quest_2/<symbol>')
def quest_2(symbol):
    if symbol.lower().strip() == 'ответ':
        return 'yes'
    else:
        return make_response(404)


@app.route('/quest_3/<answer>')
def quest_3(answer):
    if answer.lower().strip() == 'ответ':
        return 'yes'
    elif answer.lower().strip() in 'ответ':
        return 'yes'
    else:
        return make_response(404)


@app.route('/quest_4/<answer>')
def quest_4(answer):
    if answer.lower().strip() == 'ответ':
        return 'yes'
    else:
        return make_response(404)


@app.route('/quest_5/<answer>')
def quest_5(answer):
    if answer.lower().strip() == 'ответ':
        return 'yes'

    else:
        return make_response(404)
