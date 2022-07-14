#this is the discord bot replying the message
from http import client
import discord

#以下TOKEN 
TOKEN  = 'OTk3MTUzOTU4NzE4MDk5NTg3.GQMPpe.5gfkP4yoyTUJ62I2OTdU5obquWDF_YbBZ4EuSA'

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