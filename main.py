
#from discord import FFmpegPCMAudio
import discord
import os
import random
import asyncio
import youtube_dl
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

    if message.content.startswith('$undertale'):
        voice = discord.utils.get(client.voice_clients, guild=message.guild)


        if voice == None:
            channel = message.author.voice.channel
            voice = await channel.connect() 
            
        random_music = "s"

        music_id = random.randint(0, 98)

        if music_id == 0:
            music_path = "ost\\01_Once_Upon_a_Time"
        if music_id == 1:
            music_path = "ost\\02_Start_Menu"
        if music_id == 2:
            music_path = "ost\\03_Your_Best_Friend" 
        if music_id == 3:
            music_path = "ost\\04_Fallen_Down" 
        if music_id == 4:
            music_path = "ost\\05_Ruins" 
        if music_id == 5:
            music_path = "ost\\06_Uwa!!_So_Temperate"    
        if music_id == 6:
            music_path = "ost\\07_Anticipation" 
        if music_id == 7:
            music_path = "ost\\08_Unnecessary_Tension" 
        if music_id == 8:
            music_path = "ost\\09_Enemy_Approaching" 
        if music_id == 9:
            music_path = "ost\\10_Ghost_Fight" 
        if music_id == 10:
            music_path = "ost\\11_Determination" 
        if music_id == 11:
            music_path = "ost\\12_Home" 
        if music_id == 12:
            music_path = "ost\\13_Home_(Music_Box)" 
        if music_id == 13:
            music_path = "ost\\14_Heartache" 
        if music_id == 14:
            music_path = "ost\\15_Sans" 
        if music_id == 15:
            music_path = "ost\\16_Nyeh_Heh_Heh!" 
        if music_id == 16:
            music_path = "ost\\17_Snowy" 
        if music_id == 17:
            music_path = "ost\\18_Uwa!!_So_Holiday" 
        if music_id == 18:
            music_path = "ost\\19_Dogbass" 
        if music_id == 19:
            music_path = "ost\\20_Mysterious_Place" 
        if music_id == 20:
            music_path = "ost\\21_Dogsong" 
        if music_id == 21:
            music_path = "ost\\22_Snowdin_Townend" 
        if music_id == 22:
            music_path = "ost\\23_Shop" 
        if music_id == 23:
            music_path = "ost\\24_Bonetrousle" 
        if music_id == 24:
            music_path = "ost\\25_Dating_Start!" 
        if music_id == 25:
            music_path = "ost\\26_Dating_Tense!" 
        if music_id == 26:
            music_path = "ost\\27_Dating_Fight!" 
        if music_id == 27:
            music_path = "ost\\28_Premonition" 
        if music_id == 28:
            music_path = "ost\\29_Danger_Mystery" 
        if music_id == 29:
            music_path = "ost\\30_Undyne" 
        if music_id == 30:
            music_path = "ost\\31_Waterfall" 
        if music_id == 31:
            music_path = "ost\\32_Run!" 
        if music_id == 32:
            music_path = "ost\\33_Quiet_Water" 
        if music_id == 33:
            music_path = "ost\\34_Memory" 
        if music_id == 34:
            music_path = "ost\\35_Bird_That_Carries_You_Over_A_Disproportionately_Small_Gap" 
        if music_id == 35:
            music_path = "ost\\36_Dummy!" 
        if music_id == 36:
            music_path = "ost\\37_Pathetic_House" 
        if music_id == 37:
            music_path = "ost\\38_Spooktune" 
        if music_id == 38:
            music_path = "ost\\39_Spookwave" 
        if music_id == 39:
            music_path = "ost\\40_Ghouliday" 
        if music_id == 40:
            music_path = "ost\\41_Chill" 
        if music_id == 41:
            music_path = "ost\\42_Thundersnail" 
        if music_id == 42:
            music_path = "ost\\43_Temmie_Village" 
        if music_id == 43:
            music_path = "ost\\44_Tem_Shop" 
        if music_id == 44:
            music_path = "ost\\45_Ngahhh!!" 
        if music_id == 45:
            music_path = "ost\\46_Spear_of_Justice" 
        if music_id == 46:
            music_path = "ost\\47_Ooo" 
        if music_id == 47:
            music_path = "ost\\48_Alphys" 
        if music_id == 48:
            music_path = "ost\\49_It'S_Showtime!" 
        if music_id == 49:
            music_path = "ost\\50_Metal_Crusher" 
        if music_id == 50:
            music_path = "ost\\51_Another_Medium" 
        if music_id == 51:
            music_path = "ost\\52_Uwa!!_So_Heats!!" 
        if music_id == 52:
            music_path = "ost\\53_Stronger_Monsters" 
        if music_id == 53:
            music_path = "ost\\54_Hotel" 
        if music_id == 54: 
            music_path = "ost\\55_Can_You_Really_Call_This_A_Hotel,_I_Didn'T_Receive_A_Mint_On_My_Pillow_Or_Anything" 
        if music_id == 55:
            music_path = "ost\\56_Confession" 
        if music_id == 56:
            music_path = "ost\\57_Live_Report" 
        if music_id == 57:
            music_path = "ost\\58_Death_Report" 
        if music_id == 58:
            music_path = "ost\\59_Spider_Dance" 
        if music_id == 59:
            music_path = "ost\\60_Wrong_Enemy_!-" 
        if music_id == 60:
            music_path = "ost\\61_Oh!_One_True_Love" 
        if music_id == 61:
            music_path = "ost\\62_Oh!_Dungeon" 
        if music_id == 62:
            music_path = "ost\\63_It'S_Raining_Somewhere_Else" 
        if music_id == 63:
            music_path = "ost\\64_Core_Approach" 
        if music_id == 64:
            music_path = "ost\\65_Core" 
        if music_id == 65:
            music_path = "ost\\66_Last_Episode!" 
        if music_id == 66:
            music_path = "ost\\67_Oh_My..." 
        if music_id == 67:
            music_path = "ost\\68_Death_by_Glamour" 
        if music_id == 68:
            music_path = "ost\\69_For_the_Fans" 
        if music_id == 69:
            music_path = "ost\\70_Long_Elevator" 
        if music_id == 70:
            music_path = "ost\\71_Undertale" 
        if music_id == 71:
            music_path = "ost\\73_The_Choice" 
        if music_id == 72:
            music_path = "ost\\74_Small_Shock" 
        if music_id == 73:
            music_path = "ost\\75_Barrier" 
        if music_id == 74:
            music_path = "ost\\76_Bergentrückung" 
        if music_id == 75:
            music_path = "ost\\77_Asgore" 
        if music_id == 76:
            music_path = "ost\\78_You_Idiot" 
        if music_id == 77:
            music_path = "ost\\79_Your_Best_Nightmare" 
        if music_id == 78:
            music_path = "ost\\80_Finale" 
        if music_id == 79:
            music_path = "ost\\81_An_Ending" 
        if music_id == 80:
            music_path = "ost\\82_She'S_Playing_Piano" 
        if music_id == 81:
            music_path = "ost\\83_Here_We_Are" 
        if music_id == 82:
            music_path = "ost\\84_Amalgam" 
        if music_id == 83:
            music_path = "ost\\85_Fallen_Down_(Reprise)" 
        if music_id == 84:
            music_path = "ost\\86_Don'T_Give_Up" 
        if music_id == 85:
            music_path = "ost\\87_Hopes_and_Dreams" 
        if music_id == 86:
            music_path = "ost\\88_Burn_in_Despair!" 
        if music_id == 87:
            music_path = "ost\\89_Save_the_World" 
        if music_id == 88:
            music_path = "ost\\90_His_Theme" 
        if music_id == 89:
            music_path = "ost\\91_Final_Power" 
        if music_id == 90:
            music_path = "ost\\92_Reunited" 
        if music_id == 91:
            music_path = "ost\\93_Menu_(Full)" 
        if music_id == 92:
            music_path = "ost\\94_Respite" 
        if music_id == 93:
            music_path = "ost\\95_Bring_It_In,_Guys!" 
        if music_id == 94:
            music_path = "ost\\97_But_the_Earth_Refused_to_Die" 
        if music_id == 95:
            music_path = "ost\\98_Battle_Against_a_True_Hero" 
        if music_id == 96:
            music_path = "ost\\99_Power_of_-Neo-" 
        if music_id == 97:
            music_path = "ost\\100_Megalovania" 
        if music_id == 98:
            music_path = "ost\\101_Good_Night" 

        voice.stop()
        voice.play(discord.FFmpegPCMAudio(source=music_path+".mp3"))

        embed=discord.Embed(title="Sans Muzykowanie", color=0x000000)
        embed.add_field(name="Odtwarzam utwór:", value=music_path, inline=True)
        embed.set_footer(text="by reversee | Sans Muzykowanie |")
        msgx = await message.channel.send(embed=embed)

client.run(os.getenv("TOKEN"))
