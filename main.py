
#from discord import FFmpegPCMAudio
import discord
import os
import random
import asyncio
import cffi
import ffmpeg

client = discord.Client()

global music_id
music_id = 0
global music_path
music_path = "100_Megalovania.mp3"

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Undertale OST | $undertale"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$play'):
        voice = discord.utils.get(client.voice_clients, guild=message.guild)


        if voice == None:
            channel = message.author.voice.channel
            voice = await channel.connect() 
            
        files=os.listdir(".\\music")
        d=random.choice(files)
        
        voice.stop()
        voice.play(discord.FFmpegPCMAudio(source=".\music\\"+d))
        #voice.play(discord.FFmpegPCMAudio(source="ost\\100_Megalovania.mp3"))

        embed=discord.Embed(title="Sans Muzykowanie", color=0x000000)
        embed.add_field(name="Odtwarzam utwór:", value=d, inline=True)
        embed.set_footer(text="by reversee | Sans Muzykowanie |")
        msgx = await message.channel.send(embed=embed)

client.run("ODIxODc0MzAwNzY3NDM2ODAx.YFKEFg.G1S5NnkVSNUqaSQbjTZU-ccDs0A")
