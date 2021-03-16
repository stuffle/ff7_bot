# Work with Python 3.6
import discord
import asyncio
import apscheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import ast
import os
import re
import random
import time
from calendar import monthrange
import datetime
import pickle

from humor_commands import *
from actions import *
from inspire import *
from help import *
from mod import *
from constants import *
from message_extras import *
import mod


IS_TEST_ENV = os.environ.get("IS_TEST_ENV")
PREFIX = "~"
if IS_TEST_ENV:
    PREFIX = "$"
DATA_FILE = "data.json"
if IS_TEST_ENV:
    DATA_FILE = "test_data.json"


client = discord.Client(status="~help")
scheduler = AsyncIOScheduler()
participants = {}
servers = {}
CAN_JOIN = False


class HouseCupException(Exception):
    pass


def load_participants():
    global participants
    global servers

    with open(DATA_FILE, 'rb') as f:
        data = pickle.load(f)
        servers = data["servers"]


def save_participants():
    with open(DATA_FILE, 'wb') as f:
        data = {
            "servers": servers
        }
        pickle.dump(data, f)


def get_userid_from_mention(mention):
    user_id = re.sub('[!<>@]', '', mention)
    return int(user_id)


def format_name(number, name):
    formatted_number = "**" + str(number) + "** "
    formatted_name = "`" + name.capitalize() + "`: "
    return formatted_number + formatted_name


def make_backup(when):
    with open("data_backup_" + str(when), 'w', encoding='utf-8') as f:
        f.write(str(participants))


@client.event
async def on_message(message):
    channel = message.channel
    user = message.author
    user_id = user.id
    guild_id = 0
    if message.guild:
        guild_id = message.guild.id
    mention = user.mention
    text = message.content.lower()
    msg = ""

    # Prevent the bot from replying to itself
    if user == client.user:
        return

    try:
        await parse_for_lols(message)
    except Exception as ex:
        print(str(ex))
        print("Caught exception in %s server and %s channel" % (message.guild.name, message.channel.name))

    try:
        # msg will be overwritten if @sigmabot is an argument to another command
        if client.user.mentioned_in(message) and message.mention_everyone is False:
            if "i love you" in text:
                msg = "I love you too."
            elif text[1:].startswith("fuck"):
                # Why do people keep doing this? :weary:
                msg = "I'm sorry. :("
            else:
                msg = at(text, mention, "Cloud")

        if message.channel.type.name in ["private", "group"]:
            raise HouseCupException(
                "Please communicate with me in a server we share.")

        # Ignore all messages not directed at bot unless it was a mention
        if not message.content.startswith(PREFIX) and msg == "":
            return

        text = text[1:]
        args = text.split(" ")
        if len(args) == 0:
            return
        command = args[0]

        if text.startswith("help"):
            embed = help_command(message, PREFIX)
            await channel.send(embed=embed)
            return

        if len(args) > 1 and "help" in args:
            raise HouseCupException(
                "Use `~help %s` or `~help` to see the help information "
                "for %s or a list of all commands." % (command, command)
            )

        # Mod only commands
        elif text.startswith("echo"):
            if user.id != STUFFLE_ID:
                raise HouseCupException("Only stuffle can use echo.")
            msg = " ".join(text.split(" ")[1:])
        elif text.startswith("pickwinner"):
            msg = await pick_winner(text, client)
        elif text.startswith("deleteallhistory"):
            msg = await delete_history(client, message, True)
        elif text.startswith("deletesomehistory"):
            msg = await delete_history(client, message, False)
        elif text.startswith("deletehistory"):
            msg = "Please use `~deleteallhistory` or `~deletesomehistory`.\n\n" \
                  "`~deleteallhistory` deletes every message by the person it's being run on.\n" \
                  "`~deletesomehistory` does not delete pinned messages or messages in channels " \
                  "with `~deletesomehistory exempt` in the channel topic."
        elif text.startswith("clearchannelnow"):
            msg = await clear_channel_now(client, message)


        # Action commands
        elif text.startswith("hug") or text.startswith("grouphug"):
            embed = hug(user.mention, message.mentions, text)
            await channel.send(embed=embed)
            return
        elif text.startswith("cheer"):
            embed = cheer(user.mention, message.mentions, text)
            await channel.send(embed=embed)
            return
        elif text.startswith("kidnap"):
            embed = kidnap(user.mention, message.mentions, text)
            await channel.send(embed=embed)
            return

        # Inspiration Commands
        elif text.startswith("shouldikill"):
            msg = "%s: %s" % (mention, should_i_kill())
        elif text.startswith("shouldigetbacktowork"):
            msg = "%s: %s" % (mention, back_to_work())
        elif text.startswith("randompair") or text.startswith("rarepair"):
            msg = "%s: %s" % (mention, random_pair())
        elif text.startswith("kink"):
            msg = "%s: %s" % (mention, kink())
        elif text.startswith("whenshouldtheyfuck"):
            msg = "%s: %s" % (mention, when_should_they_fuck())
        elif text.startswith("inspireme"):
            msg = "%s: %s" % (mention, inspireme())
        elif text.startswith("prompt"):
            msg = "%s: %s" % (mention, gen_prompt(mention, "Sephiroth"))
        elif text.startswith("iloveyou"):
            msg = "%s: %s" % (mention, i_love_you("Sephiroth"))

    except (HouseCupException, mod.HouseCupException) as ex:
        msg = "Error: " + str(ex)
    except Exception as ex:
        msg = "Oh no! Something went wrong and I couldn't complete your "\
              " command. I'm so sorry! :sob: Ping sephirise if you need " \
              "help."
        print(user.name + ": " + repr(ex) + "\nMessage: " + text)
        print("Caught exception in %s server and %s channel" % (message.guild.name, message.channel.name))

    if msg:
        await channel.send(msg.format(message))


async def list_recs():
    await client.wait_until_ready()
    print("Current servers:")
    for server in client.guilds:
        print(server.name)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    game = discord.Game("~help")
    await client.change_presence(activity=game)


if __name__ == '__main__':
    client.loop.create_task(list_recs())
    token = os.environ.get("FF7_BOT_SECRET")

    # If there is a problem loading data, make a backup and abort start up
    try:
        load_participants()
    except Exception as ex:
        now = datetime.datetime.now(datetime.timezone.utc)
        print("Making backup at %s" % str(now))
        make_backup(str(now))
        raise ex

    now = datetime.datetime.now(datetime.timezone.utc)
    _, days_in_month = monthrange(now.year, now.month)

    scheduler.start()
    client.run(token)
