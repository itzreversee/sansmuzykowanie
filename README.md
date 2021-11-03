# sansmuzykowanie - play random music in discord
![img](https://img.shields.io/github/stars/reversee-dev/sansmuzykowanie?style=social) ![img](https://img.shields.io/github/last-commit/reversee-dev/sansmuzykowanie) ![img](https://img.shields.io/badge/version-2-blueviolet)  

---------------------------
## Commands

* $setup  
Sets presence ( can be deleted )  

* $play ```"music"```  
If ```"music"``` is not set, plays random music  
also stops loop

* $stop  
Stops music  

* $list
Lists all music files, remember to use ```""```, eg.  
 mysong.mp3 -- wrong  
 "mysong.mp3" -- good
 
* $loop ```"music"```  
If ```"music"``` is not set, loops random song.  
else it loops selected song, stop with $stop or $play  

* $pause - pauses ( breaks loops )  
* $resume - resumes  

---

## Changelog - 2.1
* $pause command (breaks loops)
* $resume command

## Changelog - 2.0  
* Rewrite
* Ability to select song with $play
* $list command
* $stop command
* $loop command
* Very good code

---

## Installation
* Get linux ( only tested on ubuntu 21.10 )
* Get python 3
* Get source code and unpack it somewhere,
* Install dependencies
* Download ```ffmpeg```
* Generate new token and insert it in last line - ```bot.run("ur_token_here")```
* Change line 15 to where music folder is.
* Run ``` python3 main.py ```
* Profit!

## Dependencies
Must have dependencies:
* asyncio
* discord
* cffi
* ffmpeg
* PyNaCl
* mutagen
###### Install them using: ``` python3 -m pip install asyncio discord cffi ffmpeg PyNaCl mutagen```
##### Other important
* Python 3 (Latest Version)
* ```ffmpeg```

## Make a bot and get Token!
* go here --> https://discord.com/developers/applications
* click new application in top right corner
* name it, and click ```create```.
* click it
* on the left, click ```Bot```.
* click ```Add Bot```, and ```Yes, do it```
* set avatar or something, and click ```Copy``` under token
* paste it in last line
* done. now go up and run this thing!

---------------------------

## bugs
* when disabling loop in random mode, it will show message that song is changing, when the loop song was supposed to end. (it won't actually play it)
* resuming loops, converts it into $play command or something lol
