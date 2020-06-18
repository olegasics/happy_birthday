import telebot

from flask import Flask, render_template, redirect, url_for, request, make_response

bot = telebot.TeleBot('1237667281:AAEm_wbrbUXro2QCXujhMZDBUNJS-9Yf6sY')
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


@app.route('/quest_2')
def quest_2():
    answer = request.form.get('answer')
    if answer.lower().strip() == 'f':
        return 'yes'
    else:
        return make_response(404)


@app.route('/quest_3')
def quest_3():
    answer = request.form.get('answer')
    if answer.lower().strip() == 'колючий':
        return 'yes'
    elif answer.lower().strip() in 'колючий':
        return 'yes'
    else:
        return make_response(404)



@app.route('/quest')
def quest():

    return 'wq'

@app.route('/quest')
def quest():

    return 'wq'

bot.polling(none_stop=True, interval=0)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Приветики. Добро пожаловать в 4 квест. Тут ждет тебя 3 ребуса")
    while message.text != '':
        bot.send_message(message.from_user.id, "Верно")
    else:
        bot.send_message(message.from_user.id, "Не верно. Подумай еще")

    bot.send_message(message.from_user.id, 'Супер. 5-я буква в пароле - v')
    bot.send_message(message.from_user.id, 'Еще я создал стикеры, похожие на тебя. Можешь добавить себе, если хочешь. Ссылка ниже')
    bot.send_message(message.from_user.id, 'https://t.me/addstickers/s412037449_268317_by_stickerfacebot')
