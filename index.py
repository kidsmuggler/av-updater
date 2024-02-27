import discord

client = discord.Client(intents=discord.Intents.all())

Token = input("Bot Token::  ")
Filename = input("GIF File Name::  ")

@client.event
async def on_ready():
    try:
        with open(Filename, 'rb') as avatar:
            await client.user.edit(avatar=avatar.read())
        print('Done ☑️')
    except Exception as e:
        print(e)

client.run(Token)
