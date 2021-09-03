import discord
import os

testBot = discord.Client()
token = os.environ["botToken"]

@testBot.event
async def on_ready():
    print(f"logged in as {testBot.user}, ping: {round(testBot.latency() *1000)}ms")

testBot.run(token)
