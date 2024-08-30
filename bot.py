from twitchio.ext import commands
from twitchio import Message
from datetime import datetime
import twitchio
import asyncio
import time
import random

class butt(commands.Bot):
    def __init__(self):
        super().__init__(token='', prefix='', initial_channels=[""])

    async def event_ready(self):
        print('Ready')

    async def event_message(self, message:Message):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        try: 
            print(f"({message.channel.name}) [{current_time}] {message.author.name}: {message.content}")
        except AttributeError:
            print(f"({message.channel.name}) [{current_time}] neobuttsbot: {message.content}")
            return

        if message.echo: 
            return

        num = random.randint(1, 5)
        if num == 1:
            message_split = message.content.split()
            if len(message_split) <= 1:
                return
            rand_word = random.choice(message_split)
            words = ("butt", "zulul", "glorytoukraine", "pepojam")
            random_word = random.choice(words)
            await message.channel.send(f"{message.content.replace(rand_word, random_word)}")

bot = butt()
asyncio.run(bot.run())
