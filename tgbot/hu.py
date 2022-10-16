TOKEN = 'YOUR_ACCESS_TOKEN'
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from settings import *
from aiogram import Bot,executor,Dispatcher,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
bot = Bot(TOKEN)
class Switcher(StatesGroup):
    api = State()
dp = Dispatcher(bot,storage=MemoryStorage())
@dp.callback_query_handler()
async def call(call: types.CallbackQuery):
    if call.data == 'menu':
        await call.message.answer('Привет')
@dp.message_handler(commands=['start'])
async def main(message: types.Message):
    k = InlineKeyboardMarkup()
    koshel2 = InlineKeyboardButton(text='Мен',callback_data='menu')#.add('Меню')
    k.add(koshel2)
    await message.answer('Hi!\n Track the movement of funds and the balance of your wallet.',reply_markup=k)
if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,skip_updates=False)
