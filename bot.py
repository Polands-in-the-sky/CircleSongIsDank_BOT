import praw
import pdb
import re
import os
import discord
import discord
from discord import client
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import time
import json
secrets_file=open("secrets.json")
secrets=secrets_file.read()
secret=json.loads(secrets)
embedcolor=0x64C13F
bot = commands.Bot(command_prefix=secret['command_prefix'])
csid_phrases=[
    "I have a 16 inch peenis and I use it to pee",
    "I have sex weed every day and you are all virgins",
    "I pee in girls and smoke a weed",
    "https://cdn.discordapp.com/attachments/422359065209995275/463351884153880577/image.jpg"
]

@bot.event
async def on_ready():
    print("Ready to meme your server!")
    print("I am running on"+bot.user.name)
    print("With the ID:"+bot.user.id)

@bot.command(pass_context=True)
async def ping():
    

@bot.command(pass_context=True)
async def csid(ctx):
    await bot.say(random.choice(csid_phrases))

bot.run(secret['token'])