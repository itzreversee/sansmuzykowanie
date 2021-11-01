import discord
from discord.ext import commands

import os
import random
import asyncio
import cffi
import ffmpeg
import time

from mutagen.mp3 import MP3

# super quality code
llock = "n"

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())

@bot.command()
async def setup(ctx):
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="$play | Play random music!"))


@bot.command()
async def play(ctx, song: str = None):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    global llock
    llock = "n"

    if voice == None:
        channel = ctx.author.voice.channel
        voice = await channel.connect() 
    
    path = '/home/server/servers/sansmuzykowanie/music/'
    if song == None:
        song = random.choice(os.listdir(path)) 

    else:
        if os.path.isfile(path+song) == False:
            song = random.choice(os.listdir(path)) 
        
    voice.stop()
    voice.play(discord.FFmpegPCMAudio(source=path+song))

    embed=discord.Embed(title="Sans Muzykowanie", color=0x000000)
    embed.add_field(name="Now playing:", value=song, inline=True)
    embed.set_footer(text="by reversee#2134 | Sans Muzykowanie |")
    msgx = await ctx.channel.send(embed=embed)

@bot.command()
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()
    
    global llock
    llock = "n"

@bot.command()
async def list(ctx):
    path = '/home/server/servers/sansmuzykowanie/music/'
    d = os.listdir(path)
    n = 0
    
    embed=discord.Embed(title="Sans Muzykowanie", color=0x000000)
    embed=discord.Embed(description="List of songs ( use $play \"song\" to play exact song)")

    for i in d:
        n = n + 1
        embed.add_field(name=n, value=i, inline=True)


    embed.set_footer(text="by reversee#2134 | Sans Muzykowanie |")
    msgx = await ctx.channel.send(embed=embed)

@bot.command()
async def loop(ctx, song: str = None):

    rSong = False

    path = '/home/server/servers/sansmuzykowanie/music/'
    if song == None:
        song = random.choice(os.listdir(path)) 
        rSong = True
    else:
        if os.path.isfile(path+song) == False:
            song = random.choice(os.listdir(path)) 
            rSong = True

    tsong = song
    if rSong == True:   
        tsong = "Random!" 
    
    embed=discord.Embed(title="Sans Muzykowanie", color=0x000000)
    embed.add_field(name="Now playing:", value=tsong, inline=True)
    embed.add_field(name="Loop enabled!", value="Use $play to disable.", inline=True)
    embed.set_footer(text="by reversee#2134 | Sans Muzykowanie |")
    msgx = await ctx.channel.send(embed=embed)
        
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    if voice == None:
        channel = ctx.author.voice.channel
        voice = await channel.connect() 
    
    #copied from play
    global llock 
    llock = "y"
    while llock == "y":  
        voice.stop()
        voice.play(discord.FFmpegPCMAudio(source=path+song))

        sSong = MP3(path + song)

        await asyncio.sleep(sSong.info.length)

        if rSong == True:
            song = random.choice(os.listdir(path))
            msgx = await ctx.channel.send("changing to: (random) - " + song)
        
        if llock == "n":
            break

    #end of copy
    
bot.run("ur_token_here")
