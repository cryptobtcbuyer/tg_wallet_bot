import asyncio
from typing import Type
from urllib import request
from aiogram import Bot,executor,Dispatcher,types
import sqlite3
import requests
import json
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from settings import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = 'YOUR_TG_ACCESS_TOKEN'
bot = Bot(TOKEN)
class Switcher(StatesGroup):
    api = State()
dp = Dispatcher(bot,storage=MemoryStorage())
con = sqlite3.connect('db.db')
cur = con.cursor()
@dp.callback_query_handler()
async def call(call: types.CallbackQuery):
    if call.data == 'odin1':
        print('ok')
        bal = cur.execute(f"SELECT add1 from users where user_id = '{call.from_user.id}'").fetchone()[0]
        one = requests.get(f'https://haqq-t.api.manticore.team/cosmos/bank/v1beta1/spendable_balances/{bal}')
        one = json.loads(one.text)
        h = one["balances"][0]['denom']
        one1 = one["balances"][0]['amount']
        h = one["balances"][0]['denom']
        await call.message.answer(f'{bal}\nBalance: {one1} {h}',reply_markup=menu)
    if call.data == 'dva1':
        print('ok1')
        bal = cur.execute(f"SELECT add2 from users where user_id = '{call.from_user.id}'").fetchone()[0]
        one = requests.get(f'https://haqq-t.api.manticore.team/cosmos/bank/v1beta1/spendable_balances/{bal}')
        one = json.loads(one.text)
        h = one["balances"][0]['denom']
        one1 = one["balances"][0]['amount']
        h = one["balances"][0]['denom']
        await call.message.answer(f'{bal}\nBalance: {one1} {h}',reply_markup=menu)
    if call.data == 'tri1':
        bal = cur.execute(f"SELECT add3 from users where user_id = '{call.from_user.id}'").fetchone()[0]
        one = requests.get(f'https://haqq-t.api.manticore.team/cosmos/bank/v1beta1/spendable_balances/{bal}')
        one = json.loads(one.text)
        h = one["balances"][0]['denom']
        one1 = one["balances"][0]['amount']
        h = one["balances"][0]['denom']
        await call.message.answer(f'{bal}\nBalance: {one1} {h}',reply_markup=menu)
    if call.data == 'chet1':
        bal = cur.execute(f"SELECT add4 from users where user_id = '{call.from_user.id}'").fetchone()[0]
        one = requests.get(f'https://haqq-t.api.manticore.team/cosmos/bank/v1beta1/spendable_balances/{bal}')
        one = json.loads(one.text)
        h = one["balances"][0]['denom']
        one1 = one["balances"][0]['amount']
        h = one["balances"][0]['denom']
        await call.message.answer(f'{bal}\nBalance: {one1} {h}',reply_markup=menu)
    if call.data == 'pyat1':
        bal = cur.execute(f"SELECT add5 from users where user_id = '{call.from_user.id}'").fetchone()[0]
        one = requests.get(f'https://haqq-t.api.manticore.team/cosmos/bank/v1beta1/spendable_balances/{bal}')
        one = json.loads(one.text)
        h = one["balances"][0]['denom']
        one1 = one["balances"][0]['amount']
        h = one["balances"][0]['denom']
        await call.message.answer(f'{bal}\nBalance: {one1} {h}',reply_markup=menu)
    
    if call.data == 'delete':
                    try:
                        per1 = cur.execute(f"SELECT add1 from users where user_id = '{call.from_user.id}'").fetchone()[0]
                        per2 = cur.execute(f"SELECT add2 from users where user_id = '{call.from_user.id}'").fetchone()[0]
                        per3 = cur.execute(f"SELECT add3 from users where user_id = '{call.from_user.id}'").fetchone()[0]
                        per4 = cur.execute(f"SELECT add4 from users where user_id = '{call.from_user.id}'").fetchone()[0]
                        per5 = cur.execute(f"SELECT add5 from users where user_id = '{call.from_user.id}'").fetchone()[0]
                        pyat1 = InlineKeyboardButton(per1,callback_data='odin')
                        pyat2 = InlineKeyboardButton(per2,callback_data='dva')
                        pyat3 = InlineKeyboardButton(per3,callback_data='tri')
                        pyat4 = InlineKeyboardButton(per4,callback_data='chet')
                        pyat5 = InlineKeyboardButton(per5,callback_data='pyat')
                        pyat = InlineKeyboardMarkup(resize_keyboard=True).add(pyat1).add(pyat2).add(pyat3).add(pyat4).add(pyat5)
                        await call.message.answer('Select the wallet to delete',reply_markup=pyat)
                    except TypeError:
                        try:
                            per1 = cur.execute(f"SELECT add1 from users where user_id = '{call.from_user.id}'").fetchone()[0]
                            per2 = cur.execute(f"SELECT add2 from users where user_id = '{call.from_user.id}'").fetchone()[0]
                            per3 = cur.execute(f"SELECT add3 from users where user_id = '{call.from_user.id}'").fetchone()[0]
                            per4 = cur.execute(f"SELECT add4 from users where user_id = '{call.from_user.id}'").fetchone()[0]
                            chet1 = InlineKeyboardButton(per1,callback_data='odin')
                            chet2 = InlineKeyboardButton(per2,callback_data='dva')
                            chet3 = InlineKeyboardButton(per3,callback_data='tri')
                            chet4 = InlineKeyboardButton(per4,callback_data='chet')
                            chet = InlineKeyboardMarkup(resize_keyboard=True).add(chet1).add(chet2).add(chet3).add(chet4)
                            await call.message.answer('Select the wallet to delete',reply_markup=chet)
                        except TypeError:
                            try:
                                per1 = cur.execute(f"SELECT add1 from users where user_id = '{call.from_user.id}'").fetchone()[0]
                                per2 = cur.execute(f"SELECT add2 from users where user_id = '{call.from_user.id}'").fetchone()[0]
                                per3 = cur.execute(f"SELECT add3 from users where user_id = '{call.from_user.id}'").fetchone()[0]
                                tri1 = InlineKeyboardButton(per3,callback_data='tri')
                                tri2 = InlineKeyboardButton(per2,callback_data='dva')
                                tri3 = InlineKeyboardButton(per1,callback_data='odin')
                                tri = InlineKeyboardMarkup(resize_keyboard=True).add(tri1).add(tri2).add(tri3)
                                await call.message.answer('Select the wallet to delete',reply_markup=tri)
                            except TypeError:
                                try:
                                    per1 = cur.execute(f"SELECT add1 from users where user_id = '{call.from_user.id}'").fetchone()[0]
                                    per2 = cur.execute(f"SELECT add2 from users where user_id = '{call.from_user.id}'").fetchone()[0]
                                    dva1 = InlineKeyboardButton(per2,callback_data='dva')
                                    dva2 = InlineKeyboardButton(per1,callback_data='odin')
                                    dva = InlineKeyboardMarkup(resize_keyboard=True).add(dva1).add(dva2)
                                    await call.message.answer('Select the wallet to delete',reply_markup=dva)
                                except TypeError:
                                    per = cur.execute(f"SELECT add1 from users where user_id = '{call.from_user.id}'").fetchone()[0]
                                    one1 = InlineKeyboardButton(per,callback_data='odin')
                                    one = InlineKeyboardMarkup(resize_keyboard=True).add(one1)
                                    await call.message.answer('Select the wallet to delete',reply_markup=one)
    if call.data == 'odin':
        hihi = cur.execute(f"SELECT add1 from users where user_id = '{call.from_user.id}'").fetchone()[0]
        cur.execute(f"UPDATE users SET add1 = '' where user_id = {call.from_user.id}")
        con.commit()
        cur.execute(f"UPDATE users SET is_addres1 = 0 where user_id = {call.from_user.id}")
        con.commit()
        hi = cur.execute(f"SELECT is_addres1 from users where user_id = '{call.from_user.id}'").fetchone()[0]
        print(hi)
        await call.message.answer(f'Your wallet has been deleted {hihi}',reply_markup=menu)
    if call.data == 'dva':
        hihi = cur.execute(f"SELECT add2 from users where user_id = '{call.from_user.id}'").fetchone()[0]
        cur.execute(f"UPDATE users SET add2 = '' where user_id = {call.from_user.id}")
        con.commit()
        cur.execute(f"UPDATE users SET is_addres2 = 0 where user_id = {call.from_user.id}")
        con.commit()
        hi = cur.execute(f"SELECT is_addres2 from users where user_id = '{call.from_user.id}'").fetchone()[0]
        print(hi)
        await call.message.answer(f'Your wallet has been deleted {hihi}',reply_markup=menu)
    if call.data == 'tri':
        hihi = cur.execute(f"SELECT add3 from users where user_id = '{call.from_user.id}'").fetchone()[0]
        cur.execute(f"UPDATE users SET add3 = '' where user_id = {call.from_user.id}")
        con.commit()
        cur.execute(f"UPDATE users SET is_addres3 = 0 where user_id = {call.from_user.id}")
        con.commit()
        await call.message.answer(f'Your wallet has been deleted {hihi}',reply_markup=menu)
    if call.data == 'chet':
        hihi = cur.execute(f"SELECT add4 from users where user_id = '{call.from_user.id}'").fetchone()[0]
        cur.execute(f"UPDATE users SET add4 = '' where user_id = {call.from_user.id}")
        con.commit()
        cur.execute(f"UPDATE users SET is_addres4 = 0 where user_id = {call.from_user.id}")
        con.commit()
        await call.message.answer(f'Your wallet has been deleted {hihi}',reply_markup=menu)
    if call.data == 'pyat':
        hihi = cur.execute(f"SELECT add5 from users where user_id = '{call.from_user.id}'").fetchone()[0]
        cur.execute(f"UPDATE users SET add5 = '' where user_id = {call.from_user.id}")
        con.commit()
        cur.execute(f"UPDATE users SET is_addres5 = 0 where user_id = {call.from_user.id}")
        con.commit()
        await call.message.answer(f'Your wallet has been deleted {hihi}',reply_markup=menu)
    if call.data == 'menu':
        addres = cur.execute(f"SELECT add1,add2,add3,add4,add5 from users where user_id = '{call.from_user.id}'").fetchone()
        if addres == None or addres == ('','','','',''):
            await call.message.answer('Hi!!\n Track the movement of funds and the balance of your wallet.',reply_markup=start2)
        else:
            await call.message.answer('Hi!!\n Track the movement of funds and the balance of your wallet.',reply_markup=start1)
    if call.data == 'balance':
        a = cur.execute(f"SELECT is_addres1 from users where user_id = '{call.from_user.id}'").fetchone()[0]
        b = cur.execute(f"SELECT is_addres2 from users where user_id = '{call.from_user.id}'").fetchone()[0]
        c = cur.execute(f"SELECT is_addres3 from users where user_id = '{call.from_user.id}'").fetchone()[0]
        d = cur.execute(f"SELECT is_addres4 from users where user_id = '{call.from_user.id}'").fetchone()[0]
        i = cur.execute(f"SELECT is_addres5 from users where user_id = '{call.from_user.id}'").fetchone()[0]
        if b == 0:
            if a == 1:
                bal = cur.execute(f"SELECT add1 from users where user_id = '{call.from_user.id}'").fetchone()[0]
                one = requests.get(f'https://haqq-t.api.manticore.team/cosmos/bank/v1beta1/spendable_balances/{bal}')
                one = json.loads(one.text)
                h = one["balances"][0]['denom']
                one1 = one["balances"][0]['amount']
                h = one["balances"][0]['denom']
                await call.message.answer(f'{bal}\nBalance: {one1} {h}',reply_markup=menu)
        else:
            if c == 0:
                if b == 1:
                    bal = cur.execute(f"SELECT add2 from users where user_id = '{call.from_user.id}'").fetchone()[0]
                    one = requests.get(f'https://haqq-t.api.manticore.team/cosmos/bank/v1beta1/spendable_balances/{bal}')
                    one = json.loads(one.text)
                    h = one["balances"][0]['denom']
                    one1 = one["balances"][0]['amount']
                    h = one["balances"][0]['denom']
                    await call.message.answer(f'{bal}\nBalance: {one1} {h}',reply_markup=menu)
            else:
                if d == 0:
                    if c == 1:
                        bal = cur.execute(f"SELECT add3 from users where user_id = '{call.from_user.id}'").fetchone()[0]
                        one = requests.get(f'https://haqq-t.api.manticore.team/cosmos/bank/v1beta1/spendable_balances/{bal}')
                        one = json.loads(one.text)
                        h = one["balances"][0]['denom']
                        one1 = one["balances"][0]['amount']
                        h = one["balances"][0]['denom']
                        await call.message.answer(f'{bal}\nBalance: {one1} {h}',reply_markup=menu)
                else:
                    if i == 0:
                        if d == 1:
                            bal = cur.execute(f"SELECT add4 from users where user_id = '{call.from_user.id}'").fetchone()[0]
                            one = requests.get(f'https://haqq-t.api.manticore.team/cosmos/bank/v1beta1/spendable_balances/{bal}')
                            one = json.loads(one.text)
                            h = one["balances"][0]['denom']
                            one1 = one["balances"][0]['amount']
                            h = one["balances"][0]['denom']
                            await call.message.answer(f'{bal}\nBalance: {one1} {h}',reply_markup=menu)
                    else:
                        if i == 1:
                            bal = cur.execute(f"SELECT add5 from users where user_id = '{call.from_user.id}'").fetchone()[0]
                            one = requests.get(f'https://haqq-t.api.manticore.team/cosmos/bank/v1beta1/spendable_balances/{bal}')
                            one = json.loads(one.text)
                            h = one["balances"][0]['denom']
                            one1 = one["balances"][0]['amount']
                            h = one["balances"][0]['denom']
                            await call.message.answer(f'{bal}\nBalance: {one1} {h}',reply_markup=menu)
    if call.data == 'my_koshel':
        add1 = cur.execute(f"SELECT add1 from users where user_id = '{call.from_user.id}'").fetchall()
        add2 = cur.execute(f"SELECT add2 from users where user_id = '{call.from_user.id}'").fetchall()
        add3 = cur.execute(f"SELECT add3 from users where user_id = '{call.from_user.id}'").fetchall()
        add4 = cur.execute(f"SELECT add4 from users where user_id = '{call.from_user.id}'").fetchall()
        add5 = cur.execute(f"SELECT add5 from users where user_id = '{call.from_user.id}'").fetchall()
        ad1 = cur.execute(f"SELECT add1 from users where user_id = '{call.from_user.id}'").fetchone()
        ad2 = cur.execute(f"SELECT add2 from users where user_id = '{call.from_user.id}'").fetchone()
        ad3 = cur.execute(f"SELECT add3 from users where user_id = '{call.from_user.id}'").fetchone()
        ad4 = cur.execute(f"SELECT add4 from users where user_id = '{call.from_user.id}'").fetchone()
        ad5 = cur.execute(f"SELECT add5 from users where user_id = '{call.from_user.id}'").fetchone()
        if add1 != []:
            if add2 != [('',)]:
                if add3 != [('',)]:
                    if add4 != [('',)]:
                        if add5 != [('',)]:
                            odin = InlineKeyboardButton(text=ad1[0],callback_data='odin1')
                            dva = InlineKeyboardButton(text=ad2[0],callback_data='dva1')
                            tri = InlineKeyboardButton(text=ad3[0],callback_data='tri1')
                            chet = InlineKeyboardButton(text=ad4[0],callback_data='chet1')
                            pyat = InlineKeyboardButton(text=ad5[0],callback_data='pyat1')
                            k = InlineKeyboardMarkup(resize_keyboard=True).add(odin).add(dva).add(tri).add(chet).add(pyat).add(menu_button)
                            await call.message.answer('Your wallets',reply_markup=k)
                        else:
                            odin = InlineKeyboardButton(text=ad1[0],callback_data='odin1')
                            dva = InlineKeyboardButton(text=ad2[0],callback_data='dva1')
                            tri = InlineKeyboardButton(text=ad3[0],callback_data='tri1')
                            chet = InlineKeyboardButton(text=ad4[0],callback_data='chet1')
                            k = InlineKeyboardMarkup(resize_keyboard=True).add(odin).add(dva).add(tri).add(chet).add(menu_button)
                            await call.message.answer('Your wallets',reply_markup=k)
                    else:
                        odin = InlineKeyboardButton(text=ad1[0],callback_data='odin1')
                        dva = InlineKeyboardButton(text=ad2[0],callback_data='dva1')
                        tri = InlineKeyboardButton(text=ad3[0],callback_data='tri1')
                        k = InlineKeyboardMarkup(resize_keyboard=True).add(odin).add(dva).add(tri).add(menu_button)
                        await call.message.answer('Your wallets',reply_markup=k)
                else:
                    odin = InlineKeyboardButton(text=ad1[0],callback_data='odin1')
                    dva = InlineKeyboardButton(text=ad2[0],callback_data='dva1')
                    k = InlineKeyboardMarkup(resize_keyboard=True).add(odin).add(dva).add(menu_button)
                    await call.message.answer('Your wallets',reply_markup=k)
            else:
                odin = InlineKeyboardButton(text=ad1[0],callback_data='odin1')
                k = InlineKeyboardMarkup(resize_keyboard=True).add(odin).add(menu_button)
                await call.message.answer('Your wallets',reply_markup=k)
        else:
            await call.message.answer('You don't have wallets',reply_markup=menu)
    if call.data == 'add_koshel':
        await call.message.answer('Enter your wallet address')
        await Switcher.api.set()
@dp.message_handler(commands=['start'])
async def main(message: types.Message):
    addres = cur.execute(f"SELECT add1,add2,add3,add4,add5 from users where user_id = '{message.from_user.id}'").fetchone()
    if addres == None or addres == ('','','','',''):
        await message.answer('Hi!!\n Track the movement of funds and the balance of your wallet.',reply_markup=start2)
    else:
        await message.answer('Hi!!\n Track the movement of funds and the balance of your wallet.',reply_markup=start1)


    
@dp.message_handler(state=Switcher.api)
async def withdrawal_phone_handler(message: types.Message, state: FSMContext):
    text = message.text
    add1 = cur.execute(f"SELECT add1 from users where user_id = '{message.from_user.id}'").fetchall()
    add2 = cur.execute(f"SELECT add2 from users where user_id = '{message.from_user.id}'").fetchall()
    add3 = cur.execute(f"SELECT add3 from users where user_id = '{message.from_user.id}'").fetchall()
    add4 = cur.execute(f"SELECT add4 from users where user_id = '{message.from_user.id}'").fetchall()
    add5 = cur.execute(f"SELECT add5 from users where user_id = '{message.from_user.id}'").fetchall()
    if add1 != []:
        if add2 != [('',)]:
            if add3 != [('',)]:
                if add4 != [('',)]:
                    if add5 != [('',)]:
                        await message.answer('You have max. number of wallets',reply_markup=menu)
                    else:
                        cur.execute(f"UPDATE users SET is_addres5 = 1 where user_id = {message.from_user.id}")
                        con.commit()
                        cur.execute(f"UPDATE users SET add5 = '{text}' where user_id = {message.from_user.id}")
                        con.commit()
                        await message.answer(f"You have successfully added the address {text}",reply_markup=addres)
                else:
                    cur.execute(f"UPDATE users SET is_addres4 = 1 where user_id = {message.from_user.id}")
                    con.commit()
                    cur.execute(f"UPDATE users SET add4 = '{text}' where user_id = {message.from_user.id}")
                    con.commit()
                    await message.answer(f"You have successfully added the address {text}",reply_markup=addres)
            else:
                cur.execute(f"UPDATE users SET add3 = '{text}' where user_id = {message.from_user.id}")
                con.commit()
                cur.execute(f"UPDATE users SET is_addres3 = 1 where user_id = {message.from_user.id}")
                con.commit()
                await message.answer(f"You have successfully added the address {text}",reply_markup=addres)
        else:
            cur.execute(f"UPDATE users SET is_addres2 = 1 where user_id = {message.from_user.id}")
            con.commit()
            cur.execute(f"UPDATE users SET add2 = '{text}' where user_id = {message.from_user.id}")
            con.commit()
            await message.answer(f"You have successfully added the address {text}",reply_markup=addres)
    else:
        cur.execute(f"INSERT INTO users (user_id,add1,add2,add3,add4,add5,bal1,bal2,bal3,bal4,bal5,is_addres1,is_addres2,is_addres3,is_addres4,is_addres5) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(message.from_user.id,text,'','','','','','','','','',0,0,0,0,0))
        con.commit()
        cur.execute(f"UPDATE users SET is_addres1 = 1 where user_id = {message.from_user.id}")
        con.commit()
        cur.execute(f"UPDATE users SET add1 = '{text}' where user_id = {message.from_user.id}")
        con.commit()
        await message.answer(f'You have successfully added the address {text}',reply_markup=addres)
    await state.finish()
    while True:
        await asyncio.sleep(10)
        pervi = cur.execute(f"SELECT is_addres1 from users where user_id = '{message.from_user.id}'").fetchone()[0]
        vtor = cur.execute(f"SELECT is_addres2 from users where user_id = '{message.from_user.id}'").fetchone()[0]
        tret = cur.execute(f"SELECT is_addres3 from users where user_id = '{message.from_user.id}'").fetchone()[0]
        chetv = cur.execute(f"SELECT is_addres4 from users where user_id = '{message.from_user.id}'").fetchone()[0]
        pyati = cur.execute(f"SELECT is_addres5 from users where user_id = '{message.from_user.id}'").fetchone()[0]
        if pervi == 1:
            a = cur.execute(f"SELECT add1 from users where user_id = '{message.from_user.id}'").fetchone()[0]
            one = requests.get(f'https://haqq-t.api.manticore.team/cosmos/bank/v1beta1/balances/{a}')
            p = json.loads(one.text)
            b = cur.execute(f"SELECT bal1 from users where user_id = '{message.from_user.id}'").fetchone()[0]
            g = str(p["balances"][0]["amount"])
            if b != '':
                if b != g:
                    print(g)
                    print(b)
                    await message.answer(f'Balance has changed\n Past balance: {b} aISLM\n New balance: {g} aISLM\n Wallet: {a}',reply_markup=menu)
                    cur.execute(f"UPDATE users SET bal1 = '{g}' where user_id = {message.from_user.id}")
                    con.commit()
                else:
                    pass
            else:
                cur.execute(f"UPDATE users SET bal1 = '{g}' where user_id = {message.from_user.id}")
                con.commit()
        if vtor == 1:
            a = cur.execute(f"SELECT add2 from users where user_id = '{message.from_user.id}'").fetchone()[0]
            one = requests.get(f'https://haqq-t.api.manticore.team/cosmos/bank/v1beta1/balances/{a}')
            p = json.loads(one.text)
            b = cur.execute(f"SELECT bal2 from users where user_id = '{message.from_user.id}'").fetchone()[0]
            g = str(p["balances"][0]["amount"])
            if b != '':
                if b != g:
                    print(g)
                    print(b)
                    await message.answer(f'Balance has changed\n Past balance: {b} aISLM\n New balance: {g} aISLM\n Wallet: {a}',reply_markup=menu)
                    cur.execute(f"UPDATE users SET bal2 = '{g}' where user_id = {message.from_user.id}")
                    con.commit()
                else:
                    pass
            else:
                cur.execute(f"UPDATE users SET bal2 = '{g}' where user_id = {message.from_user.id}")
                con.commit()
        if tret == 1:
            a = cur.execute(f"SELECT add3 from users where user_id = '{message.from_user.id}'").fetchone()[0]
            one = requests.get(f'https://haqq-t.api.manticore.team/cosmos/bank/v1beta1/balances/{a}')
            p = json.loads(one.text)
            b = cur.execute(f"SELECT bal3 from users where user_id = '{message.from_user.id}'").fetchone()[0]
            g = str(p["balances"][0]["amount"])
            if b != '':
                if b != g:
                    print(g)
                    print(b)
                    await message.answer(f'Balance has changed\n Past balance: {b} aISLM\n New balance: {g} aISLM\n Wallet: {a}',reply_markup=menu)
                    cur.execute(f"UPDATE users SET bal3 = '{g}' where user_id = {message.from_user.id}")
                    con.commit()
                else:
                    pass
            else:
                cur.execute(f"UPDATE users SET bal3 = '{g}' where user_id = {message.from_user.id}")
                con.commit()
        if chetv == 1:
            a = cur.execute(f"SELECT add4 from users where user_id = '{message.from_user.id}'").fetchone()[0]
            one = requests.get(f'https://haqq-t.api.manticore.team/cosmos/bank/v1beta1/balances/{a}')
            p = json.loads(one.text)
            b = cur.execute(f"SELECT bal4 from users where user_id = '{message.from_user.id}'").fetchone()[0]
            g = str(p["balances"][0]["amount"])
            if b != '':
                if b != g:
                    print(g)
                    print(b)
                    await message.answer(f'Balance has changed\n Past balance: {b} aISLM\n New balance: {g} aISLM\n Wallet: {a}',reply_markup=menu)
                    cur.execute(f"UPDATE users SET bal4 = '{g}' where user_id = {message.from_user.id}")
                    con.commit()
                else:
                    pass
            else:
                cur.execute(f"UPDATE users SET bal4 = '{g}' where user_id = {message.from_user.id}")
                con.commit()
        if pyati == 1:
            a = cur.execute(f"SELECT add5 from users where user_id = '{message.from_user.id}'").fetchone()[0]
            one = requests.get(f'https://haqq-t.api.manticore.team/cosmos/bank/v1beta1/balances/{a}')
            p = json.loads(one.text)
            b = cur.execute(f"SELECT bal5 from users where user_id = '{message.from_user.id}'").fetchone()[0]
            g = str(p["balances"][0]["amount"])
            if b != '':
                if b != g:
                    print(g)
                    print(b)
                    await message.answer(f'Balance has changed\n Past balance: {b} aISLM\n New balance: {g} aISLM\n Wallet: {a}',reply_markup=menu)
                    cur.execute(f"UPDATE users SET bal5 = '{g}' where user_id = {message.from_user.id}")
                    con.commit()
                else:
                    pass
            else:
                cur.execute(f"UPDATE users SET bal5 = '{g}' where user_id = {message.from_user.id}")
                con.commit()
def db_creater():
    cur.execute("""
        CREATE TABLE if not exists users (
            user_id TEXT DEFAULT '',
            bal1 TEXT DEFAULT '',
            bal2 TEXT DEFAULT '',
            bal3 TEXT DEFAULT '',
            bal4 TEXT DEFAULT '',
            bal5 TEXT DEFAULT '',
            add1 TEXT DEFAULT '',
            add2 TEXT DEFAULT '',
            add3 TEXT DEFAULT '',
            add4 TEXT DEFAULT '',
            add5 TEXT DEFAULT '',
            is_addres1 INTENGER DEFAULT 0,
            is_addres2 INTENGER DEFAULT 0,
            is_addres3 INTENGER DEFAULT 0,
            is_addres4 INTENGER DEFAULT 0,
            is_addres5 INTENGER DEFAULT 0
        );
    """)

if __name__ == '__main__':
    db_creater()
    executor.start_polling(dispatcher=dp,skip_updates=False)
