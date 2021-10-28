import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import youtube_dl
import json
import os

TOKEN = 'ODE2OTU3Nzg1NzAxODc1NzYz.YEChOg.Q8NFfunHXSKwCl9WhkWCqvB6IP8'


intents = discord.Intents.default()
intents.members = True
description = '''Python Discord Bot'''
bot = commands.Bot(command_prefix='?', description=description, intents= intents)
client = discord.Client()

queues = {}

def check_queue(ctx, id):
    if queues[id] != []:
        voice = ctx.guild.voice_client
        source = queues[id].pop(0)
        player = voice.play(source)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    channel = bot.get_channel(816962160814587904)
    await channel.send("trimit mesaju asta de fiecare data cand Vlad ruleaza un test de cod, sau cand isi da restart serveru")

@client.event
async def on_message(msg):
    if msg.content.startswith('Ce viata de cacat'):
        await  msg.channel.send('Chiar ca, bine zici')


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(589108014087405581)
    await channel.send("Ohoooo uite cine a venit")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(589108014087405581)
    await channel.send("O iesit cnv de pe server...oof ce pacat....aia e")

# in jos dai comenzi la bot care o sa inceapa cu ? + numele pe care l dai la functie ex ?Lovinescu

@bot.command()
async def Lovinescu(msg):
    await msg.send("da , prezent, no picat serveru e ok")

@bot.command(pass_context = True)
async def lovinescu_play_despacito(ctx):
    if (ctx.author.voice):

        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)  # This allows for more functionality with voice channels

        if voice == None:  # None being the default value if the bot isnt in a channel (which is why the is_connected() is returning errors)
            channel = ctx.message.author.voice.channel
            vc = await channel.connect()
            await vc.connect()
            await ctx.send(f"Am intrat pe **{vc}** ca sa va cant niste Despacito")
            source = FFmpegPCMAudio('despacito')
            player = voice.play(source)

        else:
            source = FFmpegPCMAudio('despacito')
            player = voice.play(source)

    else:
        await ctx.send("Nu vreau frate, intra si tu cu mine ca nu vorbesc singur")



@bot.command(pass_context = True)
async def leave(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Am iesit v am pupat sal")
    else:
        await ctx.send("Am iesit deja bro e ok pwp")

@bot.command(pass_context = True)
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.command(pass_context = True)
async def join2(ctx):
   user = ctx.message.author
   vc = user.voice.channel

   voice = discord.utils.get(bot.voice_clients, guild=ctx.guild) # This allows for more functionality with voice channels

   if voice == None: # None being the default value if the bot isnt in a channel (which is why the is_connected() is returning errors)
      await vc.connect()
      await ctx.send(f"Am intrat pe **{vc}**")
   else:
      await ctx.send("Is deja aici ,nu ma vezi?")


@bot.command(pass_context = True)
async def q(ctx, url:str):
    if (ctx.author.voice):


        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        guild_id = ctx.message.guild.id



        # download la yt video

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")

        source = FFmpegPCMAudio('song.mp3')

        if guild_id in queues:
            queues[guild_id].append(source)
        else: queues[guild_id] = [source]

        await ctx.send("Bagat in lista")



@bot.command(pass_context = True)
async def play(ctx, url:str):
    if(ctx.author.voice):

        channel = ctx.message.author.voice.channel
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

        #download la yt video

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")

        if voice.is_playing():
            voice.stop()
            source = FFmpegPCMAudio('song.mp3')
            player = voice.play(source, after= lambda x=None: check_queue(ctx, ctx.message.guild.id))
        else:
            source = FFmpegPCMAudio('song.mp3')
            player = voice.play(source, after= lambda x=None: check_queue(ctx, ctx.message.guild.id))

@bot.command(pass_context = True)
async def repeat(ctx):
    if(ctx.author.voice):
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        channel = ctx.message.author.voice.channel
        source = FFmpegPCMAudio('song.mp3')
        player = voice.play(source)


@bot.command(pass_context = True)
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild = ctx.guild)

    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Vezi ca nu canta nimica, n-am la ce sa pun pauza")

@bot.command(pass_context = True)
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Nu e pus nimic in pausa sorry")

@bot.command(pass_context = True)
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.stop()
    else:
        await ctx.send("Nu e pusa nicio muzica, e deja liniste")

bot.run(TOKEN)