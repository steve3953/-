import discord
import asyncio
import os

client = discord.Client()
game = discord.Game("#명령어")

@client.event
async def on_ready():
    print('Bot Online')
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "#초대링크":
        await message.channel.send("https://discord.com/oauth2/authorize?&client_id=772280976574644234&scope=bot&permissions=37014592")
        

access_token - os.environ["BOT_TOKEN"]
client.run(access_token)
