from aiogram import Bot, Dispatcher, executor, types

VOLUME_CONTROL:str = 'norm'
API_TOKEN: str = '5822562559:AAGmtLjuY2_yaxZ7HjKzgCiLdTdciZuVRK8'

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)

async def process_start_command(message: types.Message):
    await message.answer('''Привет!\nМеня зовут Эхо-бот 📢\nНапиши мне что-нибудь!''')

async def process_help_command(message: types.Message):
    await message.answer('''Напиши мне что-нибудь и в ответ я пришлю тебе твое сообщение.
Громкость эха можно регулировать с помощью команд:
/normecho - обычное эхо (по умолчанию)
/loudecho - громкое эхо
/quietecho - тихое эхо''')

async def process_normecho_command(message: types.Message):
    global VOLUME_CONTROL
    VOLUME_CONTROL = 'norm'
    await message.answer('🔉')

async def process_loudecho_command(message: types.Message):
    global VOLUME_CONTROL
    VOLUME_CONTROL = 'loud'
    await message.answer('🔊')

async def process_quietecho_command(message: types.Message):
    global VOLUME_CONTROL
    VOLUME_CONTROL = 'quiet'
    await message.answer('🔈')

async def send_photo_echo(message: types.Message):
    await message.answer_photo(message.photo[0].file_id)

async def send_audio_echo(message: types.Message):
    await message.answer_audio(message.audio.file_id)

async def send_video_echo(message: types.Message):
    await message.answer_video(message.video.file_id)

async def send_sticker_echo(message: types.Message):
    await message.answer_sticker(message.sticker.file_id)

async def send_voice_echo(message: types.Message):
    await message.answer_voice(message.voice.file_id)

async def send_files(message: types.Message):
    await message.answer_document(message.document.file_id)

async def send_echo(message: types.Message):
    if VOLUME_CONTROL == 'loud':
        await message.reply(message.text.upper())
    elif VOLUME_CONTROL == 'quiet':
        await message.reply(message.text.lower())
    else:
        await message.reply(message.text)

dp.register_message_handler(process_start_command, commands='start')
dp.register_message_handler(process_help_command, commands='help')
dp.register_message_handler(process_normecho_command, commands='normecho')
dp.register_message_handler(process_loudecho_command, commands='loudecho')
dp.register_message_handler(process_quietecho_command, commands='quietecho')
dp.register_message_handler(send_photo_echo, content_types=['photo'])
dp.register_message_handler(send_audio_echo, content_types=['audio'])
dp.register_message_handler(send_video_echo, content_types=['video'])
dp.register_message_handler(send_sticker_echo, content_types=['sticker'])
dp.register_message_handler(send_voice_echo, content_types=['voice'])
dp.register_message_handler(send_files,content_types=['document'])
dp.register_message_handler(send_echo)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)