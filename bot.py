import nest_asyncio
nest_asyncio.apply()
# bot.py
import os

import discord
from dotenv import load_dotenv

import random

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from pprint import pprint

import pafy
from discord import FFmpegPCMAudio, PCMVolumeTransformer
import nacl


FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
PAFY_BACKEND = "internal"

client = discord.Client()

client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server! Here we play Minecraft, other silly games and we watch Nine-Nine!'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
        'Terry loves yogurt!'
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

    elif message.content == 'Spranga!':
        response = 'http://www.spranga.xyz'
        await message.channel.send(response)

    elif message.content == 'Podcast!':
        search_str = 'Il Podcast di Alessandro Barbero'
        response = sp.search(search_str)
        await message.channel.send(response)

    elif message.content == 'test_play':
        for guild in client.guilds:
            if guild.name == GUILD:
                break
        if message.author.voice == None:
            await message.channel.send(embed=Embeds.txt("No Voice Channel", "You need to be in a voice channel to use this command!", author))
            return

        channel = message.author.voice.channel

        voice = discord.utils.get(guild.voice_channels, name=channel.name)

        voice_client = discord.utils.get(client.voice_clients, guild=guild)

        if voice_client == None:
            voice_client = await voice.connect()
        else:
            await voice_client.move_to(channel)

        #search = search.replace(" ", "+")

        #html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search)
        #video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())


        #await message.channel.send("https://spranga.xyz/sounds/pestifero.mp3")

        #song = pafy.new("https://spranga.xyz/sounds/pestifero.mp3")  # creates a new pafy object

        #audio = song.getbestaudio()  # gets an audio source

        #source = FFmpegPCMAudio(song.url, **FFMPEG_OPTIONS)  # converts the youtube audio source into a source discord can use

        # json = 'spranga.xyz/soundboard.json'
        #os.popen('wget https://spranga.xyz/sounds/pestifero.mp3').read()
        player = guild.voice_client
        player.play(FFmpegPCMAudio("pestifero.mp3"))
        #os.popen('rm pestifero.mp3').read()
        #voice_client.play(source)  # play the source

# @client.event
# async def test(self, ctx):
#
#     #search = "morpheus tutorials discord bot python"
#
#     if ctx.message.author.voice == None:
#         await ctx.send(embed=Embeds.txt("No Voice Channel", "You need to be in a voice channel to use this command!", ctx.author))
#         return
#
#     channel = ctx.message.author.voice.channel
#
#     voice = discord.utils.get(ctx.guild.voice_channels, name=channel.name)
#
#     voice_client = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
#
#     if voice_client == None:
#         voice_client = await voice.connect()
#     else:
#         await voice_client.move_to(channel)
#
#     #search = search.replace(" ", "+")
#
#     #html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search)
#     #video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
#
#
#     await ctx.send("https://spranga.xyz/sounds/pestifero.mp3")
#
#     song = pafy.new("https://spranga.xyz/sounds/pestifero.mp3")  # creates a new pafy object
#
#     #audio = song.getbestaudio()  # gets an audio source
#
#     source = FFmpegPCMAudio(song.url, **FFMPEG_OPTIONS)  # converts the youtube audio source into a source discord can use
#
#     voice_client.play(source)  # play the source

client.run(TOKEN)
