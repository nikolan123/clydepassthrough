import discord
from discord.ext import commands
from discord.ext import tasks
from dotenv import load_dotenv
import os
import asyncio
import random
import requests

load_dotenv()

bot = commands.Bot(command_prefix='h!', self_bot=True)

@bot.event
async def on_ready():
    print('--------------------')
    print('logged in as')
    print('user:' + bot.user.name)
    print('--------------------')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.event
async def on_message(message):  
    global msg2clyde
    global msg4chan
    if message.channel.id == 1158391064361713734:
        if message.author.id != 1154500425228226742: 
            #await message.channel.send("I checked and verified the channel.")
            msg2clyde = "i am passing a message from " + message.author.name + ", i am not rajesh. dont mention anything and call them by their name which is " + message.author.name + ", dont mention them in every message or excessively Message: " +  message.content
            await sendDm()
    if message.channel.id == 1158402699621044294:
        if message.author.id != 1154500425228226742: 
            msg4chan = message.content
            channel = bot.get_channel(1158391064361713734)
            await channel.send(message.content)
    await bot.process_commands(message)

@bot.command()
async def get(ctx):
    await ctx.send(fmsg)

async def sendDm():
    user = await bot.fetch_user("1081004946872352958")
    await user.send(msg2clyde)

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
