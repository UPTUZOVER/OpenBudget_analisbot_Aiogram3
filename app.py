from aiogram import types, Dispatcher, Bot
import asyncio
from aiogram.types.bot_command import *
from aiogram.filters import *
import requests
import json
import time


url = f"https://openbudget.uz/boards/initiatives/initiative/32/bee2ca81-eb5a-4319-9d7f-63a5d0cab95f"
token = "6800368804:AAGUofUrTfOX67-t4s46yYmCN3fb5HFRhEU"
bot = Bot(token=token, parse_mode="HTML")
dp = Dispatcher()

commands = [
    BotCommand(command='start', description="Restart the bot"),
    BotCommand(command='reyting', description="reyting"),
    BotCommand(command='help', description="help"),

]

@dp.message(Command("help"))
async def start(message: types.Message):
    await message.answer("Agar siz birorta loyiha haqida malumotga olmoqchi bulsangiz /reyting commadasidagi tartib raqamini yozib yuboring")



@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Assalomu alaykum bu bot openbudget ni urgutdagi ishlanini haqida malumot beradigan bot\n reyting commandasini bossangiz urguttadi openbudgetda quyilgan hamma loyihalar bor sizga aynan biror mahalla kerak bolda uni reytindagi tartib raqamini yozib yoboring")


response = requests.get(f'https://openbudget.uz/api/v2/info/board/32?regionId=8&districtId=93&page=0&size=30&stage=PASSED&quality=')
a = response.json()

@dp.message(Command('reyting'))
async def help_command(message: types.Message):
    format = "%Y-%m-%d %H:%M:%S"
    belgilangan_vaqt = time.strftime(format, time.localtime())
    global m
    global p
    o = (f"by: @Samur_coder_0 "
         f"\n\n\njoriy vaqt: {belgilangan_vaqt}\n\n   ")
    m = [o]
    for i in range(30):
        p = i+1
        m.append(f"{p}) Vote Count: {a['content'][i]['voteCount']} {a['content'][i]['quarterName']}")
    await message.answer('\n'.join(m))


@dp.message()
async def bitta_command(message: types.Message):
    b = message.text
    try:
        b = int(b)
        b = b - 1
        if 0 <= b < 30:
            vote_count = a['content'][b]['voteCount']
            name_mahalla = a['content'][b]['quarterName']
            cat = a['content'][b]['categoryName']
            dis = a['content'][b]["description"]
            await message.answer(f"mahalla name😅: {name_mahalla}:voteCount   : {vote_count} \n\n {cat}, {dis}")
        else:
            await message.answer("raqam yoborring.")
    except ValueError:
        await message.answer("raqam yuboring")




async def main():
    await bot.set_my_commands(commands=commands)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
+