import discord

client = discord.Client()


@client.event
async def on_ready():
    print('The discord bot is now online and ready to troll')


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content == 'Hello':
        await message.channel.send('Welcome to the discord server')


client.run('')
