import telebot
from googletrans import Translator
translator = Translator()

bot = telebot.TeleBot('1210335627:AAGV01ikEpaKFO35dmpBv_Kv9E9nB1FuKS4');

def TranslateText(text, to_lang):
    translatedBlock = translator.translate(text, to_lang)
    translatedText = translatedBlock.text
    return translatedText

@bot.message_handler(content_types=['text'])
def get_msg(msg):
    answer = TranslateText(msg.text, 'ru')
    bot.send_message(msg.from_user.id, answer)

bot.polling(none_stop = True, interval = 0)