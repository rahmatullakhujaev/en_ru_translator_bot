import json
import requests
from pprint import pprint
import logging
from aiogram import Bot, Dispatcher, executor, types
from googletrans import Translator

translator = Translator()

# def get_def(word_id):
#
#
#     app_id = "6d5e2af8"
#     app_key = "8bfa97e278b5c65703b9b608b8cbb95a"
#
#     language = "en-gb"
#     url = "https://od-api-sandbox.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
#     r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
#     res = r.json()
#
#     senses = res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
#     definitions = []
#     for sense in senses:
#         definitions.append(f'👉{sense['definitions'][0]}')
#     definitions = '\n'.join(definitions)
#     if res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
#         audio = res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']
#     else:
#         audio = None
#     output = {
#         "definitions": definitions,
#         "audio": audio
#     }
#     return output



API_TOKEN = '6799257373:AAFAlX8AaVtrBv1hn57QtA3452uyVCP1bxc'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Write anything!\nНапишите что-нибудь")



@dp.message_handler()
async def send_def(message: types.Message):
    # lang = translator.detect(message.text).lang
    # if len(message.text.split()) >= 2 or not message.text.startswith('a'):
    #     dest = 'uz' if lang == 'en' else 'en'
    #     await message.reply(translator.translate(message.text, dest).text)
    # else:
    #     if lang == 'en':
    #         word_id = message.text
    #     else:
    #         word_id = translator.translate(message.text, 'en').text
    #
    #     lookup = get_def(word_id)
    #     if lookup.get('definitions'):
    #         await message.reply(f'Word: {word_id}\nDefinition: {lookup["definitions"]}')
    #         if lookup.get('audio'):
    #             await message.reply_voice(lookup["audio"])
    #     else:
    #         if lang == 'en':
    #             await message.reply('Word not found')
    #         else:
    #             await message.reply('So\'z topilmadi')
    lang = translator.detect(message.text).lang
    dest = 'uz' if lang == 'en' else 'en'
    await message.reply(translator.translate(message.text, dest).text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

