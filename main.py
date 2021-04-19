import discord
import os
import random
import asyncio
import cffi
import ffmpeg

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="$play | Play random undertale Music!"))

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

        embed=discord.Embed(title="Sans Muzykowanie", color=0x000000)
        embed.add_field(name="Now playing:", value=d, inline=True)
        embed.set_footer(text="by reversee-dev <-- Github | Sans Muzykowanie |")
        msgx = await message.channel.send(embed=embed)

client.run("TOKEN")
