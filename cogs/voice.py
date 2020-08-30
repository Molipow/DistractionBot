import discord
import asyncio
from discord.ext import commands

class Voice(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Voice module loaded')

    @commands.command()
    async def distraction(self, ctx):
        song = discord.FFmpegPCMAudio(executable = "D:\\Program Files\\ffmpeg-20200216-8578433-win64-static\\bin\\ffmpeg.exe", source = "voice/distraction.mp3")
        vc_connection = await ctx.author.voice.channel.connect()
        vc_connection.play(song)
        await asyncio.sleep(5)
        await vc_connection.disconnect()

def setup(client):
    client.add_cog(Voice(client))