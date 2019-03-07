import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await client.send_message(message.channel, content = "Hello!")

client.run('NTUxNzE4Njc2MzAzMTgzODgy.D2L1sg.Z0DpvoFR4gmB5cs5HkJy8sFEMvw')
