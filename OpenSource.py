import discord
import asyncio
import json
import logging

# bot logging, useful for debugging if the windows closes
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

# Load configuration
configfile = open('./config.json')
config = json.loads(configfile.read())
configfile.close()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='Anyone\'s Bot'))

@client.event
async def on_message(message):
    if message.content.startswith(config['prefix'] + 'bot'):
        await client.send_message(message.channel, 'Open Source collective v.0 (patch #1.0.0')
        
    if message.content.startswith(config['prefix'] + 'source'):
        await client.send_message(message.channel, 'Source Code: https://github.com/BeastKing0/Coders-Delight-Bot')
        
client.run(config['token'])
