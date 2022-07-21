from aiogram.utils import executor
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random


bot = Bot('5412674596:AAEn0fN0AvcyHgNhpHuH69-RnSL3IzZRIE8')
dp = Dispatcher(bot)

list_of_jokes = []


@dp.message_handler(commands='start')
async def start_message(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет,могу рассказать анегдот', reply_markup=user_kb)


@dp.callback_query_handlers(text='joke_button')
async def get_joke(callback_query: types.CallbackQuery):
    global list_of_jokes
    if len(list_of_jokes) == 0:
        await bot.send_message(callback_query.from_user.id, 'В базе нет анекдотов', reply_markup=user_kb_update)
    else:
        await bot.send_message(callback_query.id, 'База данных успешно обновлена', show_alert=True)
        await bot.send_message(callback_query.from_user.id, 'хочешь получить анекдот?Тогда жми кнопку ниже', reply_markup=user_kb)



@dp.callback_query_handlers(text='update_button')
async def get_joke(callback_query: types.CallbackQuery):
    global list_of_jokes
    try:
        list_of_jokes = await aioparser.run_taskd()
        await bot.send_message(callback_query.id, 'База данных успешно обновлена', show_alert=True)
        await bot.send_message(callback_query.from_user.id, 'хочешь получить анекдот?Тогда жми кнопку ниже',
                               reply_markup=user_kb)
    except Exception as ex:
        await bot.send_message(callback_query.from_user.id, repr(ex), reply_markup=user_kb_update)





                                    # '''''''''''''''''''BUTTONS''''''''''''''''''

user_kb = InlineKeyboardMarkup(resize_keyboard=True).add(InlineKeyboardButton('Получить анегдот',
                                                                              callback_data='joke_button'))

user_kb_update = InlineKeyboardMarkup(resize_keyboard=True).add(InlineKeyboardButton('Обновить анегдот',
                                                                              callback_data='update_button'))

if __name__ == '__main__':
    print('bot polling started')
    executor.start_polling(dp, skip_updates=True)