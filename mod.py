import discord
import random
import datetime
import pytz
import mimetypes

from constants import *


utc = pytz.UTC


class HouseCupException(Exception):
    pass


def is_mod(user, channel):
    user_is_mod = user.permissions_in(channel).administrator
    role_names = [role.name.lower() for role in user.roles]
    mod_role = "mod" in role_names
    return user_is_mod or mod_role or user.id == STUFFLE_ID


async def get_channel_and_message(client, channel_id, message_id):
    channel = client.get_channel(channel_id)
    if not channel:
        raise HouseCupException(
            "I can't find that channel. Please try again.")

    message = None
    try:
        message = await channel.fetch_message(message_id)
    except Exception:
        raise HouseCupException("Invalid message ID. Please try again")
    if not message:
        raise HouseCupException(
            "I can't find that message. Please try again.")

    return channel, message


async def pick_winner(text, client):
    args = text.split()[1:]
    proper_format = "Proper formatting for this function is `~pickwinner MESSADE_ID CHANNEL_ID`"
    if len(args) != 2:
        raise HouseCupException(proper_format)
    if not args[0].isdigit() or not args[1].isdigit():
        raise HouseCupException(proper_format)

    message_id = int(args[0])
    channel_id = int(args[1])

    channel, message = await get_channel_and_message(client, channel_id, message_id)

    unique_users = []
    reactions = message.reactions
    for reaction in reactions:
        users = await reaction.users().flatten()
        for user in users:
            if user not in unique_users:
                unique_users.append(user)

    if len(unique_users) == 0:
        return "No one reacted to that message, so there is no winner."

    winner = random.choice(unique_users).name
    return "The winner is %s!" % winner


async def delete_history(client, message, all_history=True):
    topic_keyword = "~deletesomehistory exempt"

    channel = message.channel
    if not is_mod(message.author, channel):
        raise HouseCupException("Only mods may run this command.")

    if len(message.mentions) != 1:
        raise HouseCupException(
            "Mention one user to delete their history.")
    member = message.mentions[0]
    mention = member.mention
    print("Running deletehistory for %s" % mention)

    command_str = "all"
    if not all_history:
        command_str = "some"
    explanation_str = "This will delete *every* message by %s." % mention
    if not all_history:
        explanation_str = "This will delete every message by %s, except messages that are pinned or in channels with `%s` in the topic." % (
            mention, topic_keyword)

    await channel.send(
        "Running delete %s history for %s. %s\n"
        "I'll let you know when it's complete. "
        "This could take a while." % (
            command_str, mention, explanation_str))

    for channel in message.guild.text_channels:
        save_in_delete_some = channel.topic and (topic_keyword in channel.topic)
        if all_history or not save_in_delete_some:
            try:
                delete_check = lambda msg: msg.author.id == member.id
                if not all_history:
                    delete_check = lambda msg: msg.author.id == member.id and not msg.pinned
                await channel.purge(
                    limit=None,
                    check=delete_check)
            except Exception as ex:
                print("Unable to purge %s." % channel.name)
                print(str(ex))
    print("Deleted history for %s" % member.name)
    msg = "Finished running delete history for %s." % mention
    return msg


async def clear_channel_now(client, message):
    channel = message.channel
    if not is_mod(message.author, channel):
        raise HouseCupException("Only mods may run this command.")
    await channel.send(
        "Deleting all messages in this channel that aren't pinned...")

    await channel.purge(
        limit=None,
        check=lambda msg: not msg.pinned)

    return "Deleted non-pinned messages in this channel!"
