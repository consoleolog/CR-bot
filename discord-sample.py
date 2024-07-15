import discord

import datetime
from chatgpt import call_gpt
import logging
import time
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.environ["TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_ID"]

current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

formatter = logging.Formatter(f"[%(levelname)s] {current_time} :: %(message)s")

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
file_handler = logging.FileHandler(f".logs/discord.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class MyClient(discord.Client):
    async def on_ready(self):
        await self.change_presence(status=discord.Status.online, activity=discord.Game("꺼져"))

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content == "입장":
            await self.join(message)
        if message.content == "이제가봐":
            await self.out(message)
        # try:
        #     logger.info(f"{message.author} == {message.content}.")
        #     response = call_gpt(message.content)
        #     await message.channel.send(response)
        # except Exception as e:
        #     logger.error(f"{message.author} == {message.content}.")
        #     await message.channel.send("똑바로 질문 하라고 했지")
        logger.info(f"{message.author} == {message.content}.")
        await message.channel.send("점검 중 입니다.")


    async def join(self, ctx):
        if ctx.author.voice and ctx.author.voice.channel:
            channel = ctx.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("음성 채널이 존재하지 않습니다")

    async def out(self, ctx):
        await self.voice_clients[0].disconnect()


intents = discord.Intents.default()
intents.voice_states = True
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
