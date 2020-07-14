from telebot import  TeleBot, apihelper, types
import time


bot = TeleBot('API-KEY')
apihelper.proxy = {
    'https': 'http://IpwJHbsVr:fbpw6t8ys@176.103.87.81:59185'
}

def decorator(func):
    def wrap(*args, **kwargs):
        print(args[0].text, **kwargs)
        return func(*args, **kwargs)
    return wrap

def get_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Да", callback_data="Да")
    keyboard.add(callback_button)
    return keyboard

def get_sticjers():
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Стикеры для той самой",
                                                 url='https://t.me/addstickers/s412037449_268317_by_stickerfacebot')
    keyboard.add(callback_button)
    return keyboard

@bot.message_handler(commands=['start'])
@decorator
def send_welcome(message):
    bot.reply_to(message, 'Приветики. Добро пожаловать в 4 квест. Тут ждет тебя 3 ребуса')
    bot.send_message(message.from_user.id, 'Готова?', reply_markup=get_keyboard())

@bot.message_handler(content_types=['text'])
@decorator
def request_1(message):
    if message.text.lower().strip() == 'ответ':
        bot.send_message(message.from_user.id, "Верно.))")
        time.sleep(3)
        bot.send_message(message.from_user.id, "Следующий ребус")

        time.sleep(3)
        bot.send_photo(message.from_user.id,
                       "https://konstruktortestov.ru/files/4dc5/ea25/359d/bc1d/d465/0f88/f4b2/9d35/3100282544.jpg")

    elif message.text.lower().strip() == 'корги':
        bot.send_message(message.from_user.id, "Ох уж эти милые корги")
        bot.send_photo(message.from_user.id,
                       'https://avatars.mds.yandex.net/get-pdb/1598525/d83a34b6-c0a7-4f5a-9437-cb9db283cf0e/s1200?webp=false')

        time.sleep(3)
        bot.send_message(message.from_user.id, "Следующий ребус")
        time.sleep(3)

        bot.send_photo(message.from_user.id, "http://rebus1.com/pictures/261.jpg")

    elif message.text.lower().strip() == 'ответ':
        bot.send_message(message.from_user.id, "Верно")
        time.sleep(3)
        bot.send_message(message.from_user.id, 'Держи 5-ю буква в пароле - j')
        bot.send_message(message.from_user.id,
                         'Еще я создал стикеры, похожие на тебя. Можешь добавить себе, если хочешь. Ссылка ниже',
                         reply_markup=get_sticjers()
                         )
    else:
        bot.send_message(message.from_user.id, "Не верно.")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "Да":
        bot.send_message(call.message.chat.id, 'Погнали. В первом ребусе зашифрована песня')
        time.sleep(3)

        bot.send_photo(call.message.chat.id,
                       "https://sun9-47.userapi.com/c853624/v853624445/2349db/IFztUdfK10U.jpg")

bot.polling()


