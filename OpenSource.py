import discord
import asyncio
import logging

# bot logging, useful for debugging if the windows closes
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

# lol a face. Prefix used for all commands
prefix = '-'
# Oauth 2.0 token
token = ''

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='Anyones Bot'))

@client.event
async def on_message(message):
    if message.content.startswith(prefix + 'bot'):
        await client.send_message(message.channel, 'Open Source collective v.0 (patch #1.0.0')
        
    if message.content.startswith(prefix + 'source'):
        await client.send_message(message.channel, 'Source Code: https://github.com/BeastKing0/Coders-Delight-Bot')
        
client.run(token)
