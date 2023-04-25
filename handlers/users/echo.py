import os
from aiogram.dispatcher.filters import Text
from pytube import YouTube
from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InputFile
from aiogram.utils import executor
from loader import dp,bot
from io import BytesIO


# YouTubedagi vidyolarni audiosini yuklab olish uchun handler

# @dp.message_handler(Text(startswith="http"))
# async def download_audio(message:types.Message):
#     link=message.text
#     url=YouTube(link)
#     buffer=BytesIO()
#
#
#     if url.check_availability() is None:
#         audio=url.streams.get_audio_only()
#         audio.stream_to_buffer(buffer=buffer)
#         buffer.seek(0)
#         filename=url.title
#         await message.answer_audio(audio=buffer,caption=filename)
#
#     else:
#         await message.answer("Xatolik botga youtube link yuboring")


# TouTubedan video yuklab beruvchi handler

@dp.message_handler(Text(startswith="http"))
async def dewnload_video(message:types.Message):
    link=message.text
    url=YouTube(link)
    buffer=BytesIO()
    await message.reply(f"🔍")


    if url.check_availability() is None:
        try:
            video=url.streams.filter(progressive=True).get_highest_resolution()
        except:
            video=url.streams.filter(progressive=True).get_highest_resolution()
        video.stream_to_buffer(buffer=buffer)
        buffer.seek(0)
        filename=url.title
        await message.answer_video(video=buffer,caption=f"{filename}\n\n"
                                                        f"@Botur_9B_bot")

    else:
        await message.answer("Xatolik youtube linkini qayta yuboring")

