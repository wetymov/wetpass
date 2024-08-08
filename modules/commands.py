from telebot import types
from modules.template import Template


def commands_main(bot, db):
    @bot.message_handler(commands=['add'])
    def add_notice(message):
        msg = bot.send_message(message.chat.id, Template("add").get())
        bot.register_next_step_handler(msg, add_notice_step2)

    def add_notice_step2(message):
        try:
            name, login, password, *description = message.text.split()
            description = " ".join(description)
            db.create_notice(message.chat.id, name, login, password, description)
            bot.send_message(message.chat.id, "Аккаунт добавлен, посмотреть можете по команде /all")
        except Exception as e:
            msg = bot.send_message(message.chat.id, "Извините, видимо вы что-то не ввели, попробуйте еще раз\nname login password description")
            print(e)
            bot.register_next_step_handler(msg, add_notice_step2)


    @bot.message_handler(commands=['all'])
    def all_notice(message):
        markup = types.InlineKeyboardMarkup()
        data = db.get_all_notice(message.chat.id)
        if data:
            for note in data:
                markup.add(types.InlineKeyboardButton(note[-1], callback_data=f"{note[1]} read"))
            bot.send_message(message.chat.id, Template("all").get(), reply_markup=markup)
        else:
            bot.send_message(message.chat.id, Template("empty").get(), reply_markup=markup)



    @bot.message_handler(commands=['remove'])
    def remove_notice(message):
        markup = types.InlineKeyboardMarkup()
        data = db.get_all_notice(message.chat.id)
        for note in data:
            markup.add(types.InlineKeyboardButton(note[-1], callback_data=f"{note[1]} remove"))
        bot.send_message(message.chat.id, Template("remove").get(), reply_markup=markup)



    @bot.callback_query_handler(func=lambda call: True)
    def callback_inline(call):
        if call.data.split()[1] == "read":
            notice = db.get_notice(call.data.split()[0])
            print(notice)
            log_pass_desc = f"Login: {notice[2]}\nPassword: {notice[3]}\nDescription: {notice[4]}"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=log_pass_desc)
        elif call.data.split()[1] == "remove":
            notice = db.remove_notice(call.data.split()[0])
            log_pass_desc = f"Запись удалена"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=log_pass_desc)