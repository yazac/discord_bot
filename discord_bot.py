#this is the discord bot replying the message
from http import client
import discord

#以下TOKEN 
TOKEN  = ''

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/kuso':
        await message.channel.send('(`Д´)ｸｯｿｫｫｫｫｫ!!')

client.run(TOKEN)