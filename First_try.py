import discord
import logging
from discord.ext import commands
import random


intents = discord.Intents.default()
intents.members = True
logging.basicConfig(level=logging.INFO)
client = discord.Client()

description = '''Python Discord Bot'''
bot = commands.Bot(command_prefix='?', description=description)


@client.event
async def on_ready():
    print('Ne-am logat ca si {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('It s me...')

    if message.content.startswith('vrei sa pleci'):
        await message.channel.send('da ,nu ma, nu ma iei')

    if message.content.startswith('nu ma, nu ma iei'):
        await message.channel.send('nu ma, nu ma, nu ma ieii')

    if message.content.startswith('chipul tau si dragostea din tei'):
        await message.channel.send('Mi-amintesc de ochiiii taiiiiii')

    if message.content.startswith('MAIA HEE'):
        await message.channel.send('MAIA HOO')

    if message.content.startswith('MAIA HAA'):
        await message.channel.send('MAIA HAHAA')

    if message.content.startswith('asa i boss?'):
        await message.channel.send('da boss cum sa nu')




client.run('ODE2OTU3Nzg1NzAxODc1NzYz.YEChOg.Q8NFfunHXSKwCl9WhkWCqvB6IP8')