#this is the discord bot replying the message
from http import client
from discord.channel import VoiceChannel
from discord.player import FFmpegPCMAudio
import discord
import time

#以下TOKEN 
TOKEN  = 'OTk3MTUzOTU4NzE4MDk5NTg3.Ge5MmH.z3orHZTPU8uA6gXXAa4Ndx3SuBDcwpxn-PshiA'

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    global voiceChannel

    if message.author.bot:
        return
      
    if message.content == '/KAF':
        await message.channel.send('あ?かかってこいよ、俺がKAFなんだよ')
      
    if message.content == '/kuso':
        await message.channel.send('(`Д´)ｸｯｿｫｫｫｫｫ!!')
      
    if message.content == '/ike':
        await message.channel.send('いけ！')

    if message.content == '/tobe':
        await message.channel.send('とべ！')
      
    if message.content == '/mc':
        await message.channel.send('らんらんるー()')
        await message.channel.send(file=discord.File('test.jpg'))

    #if it reseive 'invite', get in to voice chanel and play the music
    if message.content == '/invite':
        #if the author is not in the voice channel, return
        if not message.author.voice:
            await message.channel.send('あなたは音声チャンネルに参加していません')
            return
        #if the author is in the voice channel, get in to the voice channel
        else: 
            await message.channel.send('コマンドを打った人のvoive chanelで美しい音が再生されています。')
            voiceChannel = await VoiceChannel.connect(message.author.voice.channel)
            message.guild.voice_client.play(discord.FFmpegPCMAudio("fart.mp3"))
            #when the music is finished, disconnect from the voice chanel
            time.sleep(5)
            await voiceChannel.disconnect()
    
    if message.content == '/help':
        await message.channel.send('/kuso:\t(`Д´)ｸｯｿｫｫｫｫｫ!!と叫びます\n/KAF:\tKAF煽り\n/ike: \tいけ！と叫びます\n/tobe:\tとべ！と叫びます\n/mc: \tドナルドがムカつきます\n/invite:\t綺麗な音楽を再生します')

client.run(TOKEN)