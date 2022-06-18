import telebot
from telebot import types

from dsnet import Dsnet

bot = telebot.TeleBot('5293979248:AAEDyPwaxbfpaOCEq1ouO5GQyyHZazD_Fvs')


@bot.message_handler(commands=["start"])
def start(m):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Pritunl", callback_data='pritunl')
    item2 = types.InlineKeyboardButton("dsnet", callback_data='dsnet')
    markup.add(item1, item2)
    bot.send_message(m.chat.id, 'Pritunl or DSNET', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def get_user_info(call):
    if call.message:
        if call.data == 'dsnet':
            bot.send_message(call.message.chat.id, 'Send me Username')
            bot.register_next_step_handler(call.message, get_description, call)



def get_description(message, call):
    username = message.text
    bot.send_message(call.message.chat.id, 'Send me Description')
    bot.register_next_step_handler(call.message, test, username)

def test(message, username):
    description = message.text
    bot.send_message(message.chat.id , Dsnet(username,description).create_user)

bot.polling(none_stop=True, interval=0)
