from datetime import datetime
from random import seed
from random import randint
import asyncio
import discord
import logging
import re

# Main client
client = discord.Client()

# Logger
logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
logger = logging.getLogger()

# Stream to stdout
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)

# Initial ready state
@client.event
async def on_ready():
    logger.debug('We have logged in as {0.user}'.format(client))

# Responses for received messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Randomly chime in with laughter
    laughter_regexp = re.compile(r'\b(?:a*(?:ha)+h?|(?:l+o+)+l+)\b', re.IGNORECASE)
    if laughter_regexp.search(message.content):
        value = randint(0,100)
        responses = [
            "lol",
            "haha",
            "Haha",
            "ahaha",
            "Ahaha",
            "hahaha",
            "Hahaha"
        ]
        if (value <= 5): # 5% chance to respond
            response_idx = randint(0,len(responses) - 1)
            await client.send_message(message.channel, content = responses[response_idx])
    
    # Apologize if we get annoyed with pugbot
    annoyed_regexp = re.compile(r'\b(god( ?)dam(m?n?i?t?)|fucking)( ?)pugbot\b', re.IGNORECASE)
    if annoyed_regexp.search(message.content):
        await client.send_message(message.channel, content = "Sorry")

    # Express pugbot's inner child
    penis_regexp = re.compile(r'(P|p)enis')
    if penis_regexp.search(message.content):
        await client.send_message(message.channel, content = "Duhuhuhuh")

    # Tell her what time it is
    if "10:33" in message.content:
        await client.send_file(message.channel, 'its_1033/its_1033_final.mp4')

# Tell her what time it is every day at 10:33
async def tell_her_what_time_it_is():
    await client.wait_until_ready()
    send_time   = "10:33"
    wait_time   = 1
    channel_id  = "462408914609111082" # General; TODO: Find the channel ID programmatically
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

# Asynchronous task loops
client.loop.create_task(tell_her_what_time_it_is())

client.run('NTUxNzE4Njc2MzAzMTgzODgy.D2L1sg.Z0DpvoFR4gmB5cs5HkJy8sFEMvw')
