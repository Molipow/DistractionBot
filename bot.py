import discord
import os
import json
import time
from discord.ext import commands, tasks

# https://discord.com/oauth2/authorize?client_id=748946531805036584&permissions=3145728&scope=bot            Add bot with Admin permission

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("Bot working")
    await client.change_presence(status=discord.Status.online)

@client.command(aliases=["reset","restart", "reboot"])
@commands.has_permissions(administrator = True)
async  def _reset(ctx):
    await ctx.send("Restartowanie bota")
    await client.close()
    os.system("cls")
    os.system("echo Bot restarting")
    os.system("python bot.py")

@client.command()
@commands.has_permissions(administrator = True)
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Włączono moduł {extension}")

@client.command()
@commands.has_permissions(administrator = True)
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Wyłączono moduł {extension}")

@client.command()
@commands.has_permissions(administrator = True)
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Przeładowano moduł {extension}")

for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")


with open("token.txt") as file:
    token = file.readline()
client.run(token)