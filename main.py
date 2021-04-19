import discord, os, asyncio, cffi, ffmpeg
client = discord.Client()
@client.event
async def on_ready():
    print('Logged in using: {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user: return
    if message.content.startswith('$play'):
        voice = discord.utils.get(client.voice_clients, guild=message.guild)
        if voice == None:
            channel = message.author.voice.channel
            voice = await channel.connect() 
        files=os.listdir(".\\music")
        d=random.choice(files)
        voice.stop()
        voice.play(discord.FFmpegPCMAudio(source=".\music\\"+d))
        embed=discord.Embed(title="Sans Muzykowanie nano | https://github.com/reversee-dev/sansmuzykowanie | "color=0x000000)
        embed.add_field(name="Now playing:", value=d, inline=True)
        msgx = await message.channel.send(embed=embed)
client.run("TOKEN")
