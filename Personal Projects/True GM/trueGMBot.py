import discord, os

from dotenv import load_dotenv

import gmisms

#https://realpython.com/how-to-make-a-discord-bot-python/
#https://github.com/jagrosh/MusicBot/issues/1679
load_dotenv()
TOKEN = os.getenv('TOKEN')
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif client.user in message.mentions:
        userPing = '<@{}>'.format(message.author.id)
        quote = gmisms.selectQuote(userPing)
        print(quote)
        await message.reply(quote)
        #await message.channel.send(quote)

client.run(TOKEN)
