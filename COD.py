import asyncio
from aiogram import Bot, Dispatcher, types
import logging
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.base import StorageKey
from aiogram import F
import numpy as np
from aiogram.client.bot import DefaultBotProperties
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import emoji

a = [1]
u = 0
logging.basicConfig(level=logging.INFO)
bot = Bot(token='', default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()

data = pd.read_csv(r"C:\Users\Маша\PycharmProjects\pythonProject41\данные.csv")
del data['Loan_ID']
del data['Education']

ar = []
av = []
aj = []
at = []

for i in range(0, 10 ** 7):
    ar.append(str(i))
for i in range(0, 10 ** 7):
    av.append(str(i))
for i in range(0, 10 ** 7):
    aj.append(str(i))
for i in range(0, 10 ** 7):
    at.append(str(i))


class O(StatesGroup):
    c = State()
    ch = State()
    chj = State()
    chjk = State()
    chjkl = State()


def data_Self_Employed(x):
    if x == "No":
        return 0
    return 1


data['Self_Employed'] = data['Self_Employed'].apply(data_Self_Employed)


def data_Dependents(x):
    if x == "1":
        return 1
    elif x == "2":
        return 2
    elif x == "3" or x == "3+":
        return 3
    return 0


data['Dependents'] = data['Dependents'].apply(data_Dependents)


def data_Loan_Amount_Term(x):
    if x > 1:
        return x
    return 0


data['Loan_Amount_Term'] = data['Loan_Amount_Term'].apply(data_Loan_Amount_Term)
s = data['Loan_Amount_Term']
s = data['LoanAmount']


def data_LoanAmount(x):
    if x > 1:
        return x
    return 0


data['LoanAmount'] = data['LoanAmount'].apply(data_LoanAmount)


def data_gender(x):
    if x == "Male":
        return 1
    return 0


data['Gender'] = data['Gender'].apply(data_gender)


def data_Married(x):
    if x == "No":
        return 0
    return 1


data['Married'] = data['Married'].apply(data_Married)


def data_Loan_Status(x):
    if x == 'N':
        return 0
    return 1


data['Loan_Status'] = data['Loan_Status'].apply(data_Loan_Status)

del data['Property_Area']
x = data.copy()
del x['Loan_Status']
del x['Credit_History']
y = data['Loan_Status']
x['Gender'] = x['Gender'].astype('float64')
x['Married'] = x['Married'].astype('float64')
x['ApplicantIncome'] = x['ApplicantIncome'].astype('float64')
x['CoapplicantIncome'] = x['CoapplicantIncome'].astype('float64')
x['LoanAmount'] = x['LoanAmount'].astype('float64')
x['Loan_Amount_Term'] = x['Loan_Amount_Term'].astype('float64')
X_train, X_validation, Y_train, Y_validation = train_test_split(x, y, test_size=0.20)



@dp.message(F.text.lower() == "/start")
async def reply_builder(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="начать"),

        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )

    await message.answer(
        "Здраствуйте,отвечая на вопросы вы узнаете одобрят ли вам кредит (акуратность ответа  0.78449 (0.023950)) ",
        reply_markup=keyboard)


@dp.message(F.text.lower() == "начать")
async def reply_builder(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="male"),
            types.KeyboardButton(text="female"),

        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    a.clear()
    print(a)
    await message.answer("укажите ваш пол", reply_markup=keyboard)


@dp.message(F.text.lower() == "female")
async def reply_builder(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="yes"),
            types.KeyboardButton(text="no"),

        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True

    )
    a.append(0)
    print(a)
    await message.answer("вы женаты/замужем?", reply_markup=keyboard)


@dp.message(F.text.lower() == "male")
async def reply_builder(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="yes"),
            types.KeyboardButton(text="no"),

        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True

    )
    a.append(1)
    print(a)
    await message.answer("вы женаты/замужем?", reply_markup=keyboard)


@dp.message(F.text.lower() == "1")
async def reply_builder(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text=emoji.emojize(":check_mark_button:")),
            types.KeyboardButton(text=emoji.emojize(":cross_mark:")),

        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    a.append(1)
    print(a)
    await message.answer("Вы самозаняты ?", reply_markup=keyboard)


@dp.message(F.text.lower() == "2")
async def reply_builder(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text=emoji.emojize(":check_mark_button:")),
            types.KeyboardButton(text=emoji.emojize(":cross_mark:")),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    a.append(2)
    print(a)
    await message.answer("Вы самозаняты ?", reply_markup=keyboard)


@dp.message(F.text.lower() == "3")
async def reply_builder(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text=emoji.emojize(":check_mark_button:")),
            types.KeyboardButton(text=emoji.emojize(":cross_mark:")),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    a.append(3)
    print(a)
    await message.answer("Вы самозаняты ?", reply_markup=keyboard)


@dp.message(F.text.lower() == "0")
async def reply_builder(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text=emoji.emojize(":check_mark_button:")),
            types.KeyboardButton(text=emoji.emojize(":cross_mark:")),

        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    a.append(0)
    print(a)
    await message.answer("Вы самозаняты ?", reply_markup=keyboard)


@dp.message(F.text.lower() == "no")
async def reply_builder(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="1"),
            types.KeyboardButton(text="2"),
            types.KeyboardButton(text="3"),
            types.KeyboardButton(text="0"),

        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    print(a)
    a.append(0)
    await message.answer("сколько у вас иждивенцев?", reply_markup=keyboard)


@dp.message(F.text.lower() == "yes")
async def reply_builder(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="1"),
            types.KeyboardButton(text="2"),
            types.KeyboardButton(text="3"),
            types.KeyboardButton(text="0"),

        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    print(a)
    a.append(1)
    await message.answer("сколько у вас иждивенцев?", reply_markup=keyboard)


@dp.message(F.text.lower() == emoji.emojize(":check_mark_button:"))
async def cmd_food(message: types.Message, state: FSMContext):
    await message.answer('введите вашу зарплату(введите число не меньше 4)')
    a.append(1)
    await state.set_state(O.c)


@dp.message(F.text.lower() == emoji.emojize(":cross_mark:"))
async def cmd_food(message: types.Message, state: FSMContext):
    a.append(0)
    await message.answer('введите вашу зарплату(введите число не меньше 4)')
    await state.set_state(O.c)


@dp.message(O.c, F.text.in_(ar))
async def food_chosen(message: types.Message, state: FSMContext):
    await state.update_data(chosen_food=message.text.lower())
    await message.answer('введите вашу совместную зарплату(введите число не меньше 4)')
    s = int(message.text.lower())
    print(s)
    s //= 92
    a.append(s)
    print(a)
    await state.set_state(O.ch)


@dp.message(O.ch, F.text.in_(av))
async def food_size_chosen(message: types.Message, state: FSMContext):
    await message.answer('введите сумму займа(введите число не меньше 4)')
    s = int(message.text.lower())
    print(s)
    s //= 92
    a.append(s)
    print(a)
    await state.set_state(O.chj)


@dp.message(O.chj, F.text.in_(aj))
async def food_size_chosen(message: types.Message, state: FSMContext):
    await message.answer('введите количество дней на выплату кредита(введите число не меньше 4)')
    s = int(message.text.lower())
    print(s)
    s //= 92
    a.append(s)
    print(a)
    await state.set_state(O.chjk)


@dp.message(O.chjk, F.text.in_(at))
async def food_size_chosen(message: types.Message, state: FSMContext):
    s = int(message.text.lower())
    print(s)
    a.append(s)
    print(a)
    await message.answer("Данные получены ,идет подведение итогов... \n")
    prediction = LinearDiscriminantAnalysis()
    prediction = prediction.fit(X_train, Y_train)
    а = np.asarray(a)
    predictions = prediction.predict([a])
    if predictions == 1:
        await message.answer("вам одобрят кредит")
        print("вам одобрят кредит ")
    else:
        await message.answer("вам не одобрят кредит")
        print("вам не одобрят кредит")
    kb = [
        [
            types.KeyboardButton(text="начать"),

        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True

    )

    await message.answer(
        "Вы можете начать заново нажав на кнопку 'начать' ",
        reply_markup=keyboard)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
