import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    await client.change_presence(game=discord.Game(name='Anyones Bot'))
    if message.content.startswith('-bot'):
        await client.send_message(message.channel, 'Open Source collective v.0 (patch #1.0.0')

client.run('hidden token')
