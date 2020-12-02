from datetime import datetime
from random import seed
from random import randint
import asyncio
import configparser
import discord
import logging
import re
import sys

##############
### Config ###
##############

config = configparser.ConfigParser()
config.read('pugbot.cfg')
bot_token = config['DEFAULT']['BOT_TOKEN']

##############
### Logger ###
##############

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Set stream handler to stdout and print debug messages
consoleHandler = logging.StreamHandler(sys.stdout)
consoleHandler.setLevel(logging.DEBUG)

# Set format for debug logs
logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
consoleHandler.setFormatter(logFormatter)

# Add the handler
logger.addHandler(consoleHandler)

###################
### Main client ###
###################

# Client object
client = discord.Client()

# Initial ready state
@client.event
async def on_ready():
    logger.debug('We have logged in as {0.user}'.format(client))

# Responses for received messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    ######################
    ### AUTO RESPONSES ###
    ######################

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

    # Respond curiously if we mention pugbot only by name
    pugbot_regexp = re.compile(r'^(?:hey\s|yo\s|sup\s)?pugbot[.!?]*$', re.IGNORECASE)
    if pugbot_regexp.search(message.content):
        responses = [
            "gif/simpsons-you-rang.gif",
            "gif/pug-look-back.gif",
            "gif/pug-tip-hat.gif",
            "gif/pug-oh-no-you-didnt.gif",
            "img/lee-pug.png",
            "img/colin-pug.png"
        ]
        response_idx = randint(0,len(responses) - 1)
        await client.send_file(message.channel, responses[response_idx])
   
    # Apologize if we get annoyed with pugbot
    annoyed_regexp = re.compile(r'\b(god( ?)dam(m?n?i?t?)|fucking)( ?)pugbot\b', re.IGNORECASE)
    if annoyed_regexp.search(message.content):
        await client.send_message(message.channel, content = "Sorry")

    # Respond to thank yous
    thankyou_regexp = re.compile(r'\b(thanks|thank you)( ?)pugbot\b', re.IGNORECASE)
    if thankyou_regexp.search(message.content):
        responses = [
            "img/fingerguns.png",
            "img/lionking-pug.png",
            "👌"
        ]
        response_idx = randint(0,len(responses) - 1)
        if responses[response_idx].startswith("img"):
            await client.send_file(message.channel, responses[response_idx])
        else:
            await client.send_message(message.channel, content = responses[response_idx])

    # Express pugbot's inner child
    penis_regexp = re.compile(r'(P|p)enis')
    if penis_regexp.search(message.content):
        await client.send_message(message.channel, content = "Duhuhuhuh")

    sixtynine_regexp = re.compile(r'\b69(th)?(ing)?\b')
    if sixtynine_regexp.search(message.content):
        responses = [
            "Nice",
            "_Nice_"
        ]
        response_idx = randint(0,len(responses) - 1)
        await client.send_message(message.channel, content = responses[response_idx])

    ################
    ### COMMANDS ###
    ################

    # Commands and responses; responses ending with a supported video extension are sent as files
    commands = {
        "!1033":    "video/its_1033/its_1033_final.mp4",
        "!whirl":   "video/whirl/whirl.gif",
        "!laugh":   "Duhuhuhuh"
    }

    # List all commands
    available_commands = list(commands.keys())
    help_text = 'List of available commands:\n\n'
    for command in available_commands:
        help_text = help_text + command + '\n'
    if message.content == "!commands" or message.content == "!help":
        await client.send_message(message.channel, content = help_text)

    # Parse input, determine if it's a file or text, and respond accordingly
    command_regex = re.compile(r'^\!\w+') # Command starts with '!'?
    command = command_regex.search(message.content)
    if command is not None:
        for key, val in commands.items():
            if key == command.group():
                extension_regex = re.compile(r'([a-zA-Z0-9\s_\\.\-\(\):])+(.mp4|.gif|.gifv)$') # Value for command is a video/gif?
                is_video = extension_regex.search(val)
                if is_video is not None:
                    await client.send_file(message.channel, val)
                else:
                    await client.send_message(message.channel, content = val)

# Tell her what time it is every day at 10:33
async def tell_her_what_time_it_is():
    await client.wait_until_ready()
    send_time   = "10:33"
    wait_time   = 1
    channel     = discord.utils.get(client.get_all_channels(), name="general")
    mp4_file    = 'video/its_1033/its_1033_final.mp4'
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

client.run(bot_token)
