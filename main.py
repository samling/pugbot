from datetime import datetime
from random import seed
from random import randint
import asyncio
import discord
import re

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    regexp = re.compile(r'\b(?:(A|a)*(?:(H|h)(A|a))+h?|(?:(L|l)+(O|o)+)+(L|l)+)\b')
    if regexp.search(message.content):
        value = randint(0,1000)
        responses = [
            "lol",
            "haha",
            "Haha",
            "ahaha",
            "Ahaha",
            "hahaha",
            "Hahaha"
        ]
        print("Detected laughter: {}".format(value))
        print(value)
        if (value >= 950):
            print("Laughing in unison...")
            response_idx = randint(0,len(responses) - 1)
            await client.send_message(message.channel, content = responses[response_idx])

    if "penis" in message.content:
        await client.send_message(message.channel, content = "Duhuhuhuh")

    if "10:33" in message.content:
        await client.send_file(message.channel, 'its_1033/its_1033_final.mp4')

async def tell_her_what_time_it_is():
    await client.wait_until_ready()
    send_time   = "10:33"
    wait_time   = 1
    channel_id  = "462408914609111082"
    channel     = client.get_channel(channel_id)
    mp4_file    = 'its_1033/its_1033_final.mp4'
    while not client.is_closed:
        now = datetime.strftime(datetime.now(), "%H:%M")
        if now == send_time:
            await client.send_file(channel, mp4_file)
            wait_time = 90
        else:
            wait_time = 1
        await asyncio.sleep(wait_time)

client.loop.create_task(tell_her_what_time_it_is())

client.run('NTUxNzE4Njc2MzAzMTgzODgy.D2L1sg.Z0DpvoFR4gmB5cs5HkJy8sFEMvw')
