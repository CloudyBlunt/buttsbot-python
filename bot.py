from twitchio.ext import commands
from twitchio import Message
from datetime import datetime
import twitchio
import asyncio
import time
import random
import json

class butt(commands.Bot):
    def __init__(self):
        super().__init__(token='', prefix='', initial_channels=[""])

    async def event_ready(self):
        print('Ready')
        await bot.get_channel('serbianfemboy').send(f"/me Reconnected")

    async def event_message(self, message:Message):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        try: 
            print(f"({message.channel.name}) [{current_time}] {message.author.name}: {message.content}")
        except AttributeError:
            print(f"({message.channel.name}) [{current_time}] bot: {message.content}")
            return
        if message.echo: 
            return

        with open('chance.json') as f:
            data = json.load(f)
        chance = data['chance']
        num = random.randint(1, int(chance))

        if num == 1:
            message_split = message.content.split()
            if len(message_split) <= 1:
                return
            rand_word = random.choice(message_split)
            #words = ("Retard", "zulul", "pepojam", )
            #random_word = random.choice(words)
            #await message.channel.send(f"{message.content.replace(rand_word, random_word)}")
            
            url_1 = f'https://api.ivr.fi/v2/twitch/user?login={message.channel.name}'
            response_1 = requests.get(url_1)
            data_1 = response_1.json()
            id = data_1[0]['id']

            url_2 = f'https://7tv.io/v3/users/twitch/{id}'
            response_2 = requests.get(url_2)
            data_2 = response_2.json()
            set_id = data_2['emote_set']['id']

            url = f'https://7tv.io/v3/emote-sets/{set_id}'
            response = requests.get(url)
            data = response.json()

            count = data['emote_count']
            random_emote1 = random.randint(0, count)
            test = data['emotes'][random_emote1]['name']
            await message.channel.send(f"{message.content.replace(rand_word, test)}")

        await self.handle_commands(message)
        
    @commands.command()
    @commands.cooldown(1, 5, commands.Bucket.user)
    async def ping(self, ctx: commands.Context):
        await ctx.reply(f'pong')

    @commands.command()
    @commands.cooldown(1, 2, commands.Bucket.user)
    async def set(self, ctx, chnc):    
        with open("chance.json", "r") as f:
            self.chance = json.load(f)
        self.chance["chance"] = chnc
        with open("chance.json", "w") as f:
            json.dump(self.chance, f)        
        await ctx.reply(f"✅ {chnc}")

bot = butt()
asyncio.run(bot.run())
