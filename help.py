import discord


CAPTION_DOC_LINK = "https://docs.google.com/document/d/1VXoi-oesHpQ1l3payu" \
                   "NtEeQFfD_Dht3Emc3JIznOZXU/edit?usp=sharing"
COLOR = 6095788


def help_command(message, prefix):
    guild_id = message.guild.id
    text = message.content.lower()
    args = text.split()

    if len(args) == 1:
        return general_help(prefix, guild_id)

    arg = args[1]
    embed = None

    # Mod Only commands
    if arg == "mod":
        msg = "These are all commands that can only be used by mods."
        embed = discord.Embed(
            title="Mod Only Commands Help",
            color=COLOR,
            description=msg)
        embed.add_field(
            name="Utility Commands:",
            value="`pickwinner`",
            inline=False)
        embed.add_field(
            name="Server Management Commands",
            value="`deleteallhistory`, `deletesomehistory`, `clearchannelnow`",
            inline=False)

    elif arg == "pickwinner":
        msg = "Pick a random person that reacted to a given message. " \
              "This will work no matter how many times a person has reacted with equal probability." \
              "\n\n Example `%spickwinner MESSADE_ID CHANNEL_ID`" % prefix
        embed = discord.Embed(
            title="Pick Winner Help",
            color=COLOR,
            description=msg)
    elif arg == "deleteallhistory":
        msg = "Delete every message by the mentioned person in the server. " \
              "\n\n Example `%sdeleteallhistory @person`" % prefix
        embed = discord.Embed(
            title="Delete All History Help",
            color=COLOR,
            description=msg)
    elif arg == "deletesomehistory":
        msg = "Delete every message by the mentioned person in the server except " \
              "pinned messages or messages in channels " \
              "with `~deletesomehistory exempt` in the channel topic." \
              "\n\n Example `%sdeletesomehistory @person`" % prefix
        embed = discord.Embed(
            title="Delete Some History Help",
            color=COLOR,
            description=msg)
    elif arg == "deletehistory":
        msg = "Please use `~deleteallhistory` or `~deletesomehistory`.\n\n" \
              "`~deleteallhistory` deletes every message by the person it's being run on.\n" \
              "`~deletesomehistory` does not delete pinned messages or messages in channels " \
              "with `~deletesomehistory exempt` in the channel topic."
        embed = discord.Embed(
            title="Delete History Help",
            color=COLOR,
            description=msg)
    elif arg == "clearchannels":
        msg = "Delete all messages that are more than a week old in " \
              " the personal channels, except for the ones that are pinned. " \
              "\n\n Example `%sclearchannels`" % prefix
        embed = discord.Embed(
            title="Clear Channels Help",
            color=COLOR,
            description=msg)
    elif arg == "clearchannelnow":
        msg = "Delete all messages in the channel this is called from " \
              "that aren't pinned." \
              "\n\nExample: `%sclearchannelnow`"
        embed = discord.Embed(
            title="Clear Channels Help",
            color=COLOR,
            description=msg)

    # Fun Commands
    elif arg == "grouphug" or arg == "group_hug" or arg == "hug":
        msg = "Give someone or a group of people a hug! " \
              "Examples: `%shug @catyPi @stuffle`, `%shug chukar`" \
              "\n\nGifs and captions by Stuffle, Chukar, and Caty Pi." % (
                  prefix, prefix)
        embed = discord.Embed(
            title="Hug Help",
            color=COLOR,
            description=msg)
    elif arg == "cheer":
        msg = "Cheer someone on!\n " \
              "Examples: `%scheer person`" % prefix
        embed = discord.Embed(
            title="Cheer Help",
            color=COLOR,
            description=msg)
    elif arg == "kidnap":
        msg = "Kidnap someone!\nExample: `%skidnap @cloud`" % prefix
        embed = discord.Embed(
            title="Kidnap Help",
            color=COLOR,
            description=msg)

    # Writing Commands
    elif arg == "prompt":
        msg = "Get a randomly generated prompt. Example: `%sprompt`" \
              "\n\nPrompt options written by RedHorse, Stuffle, " \
              "Aubry, Essa, Mik, and DarkBlue\n" % prefix
        embed = discord.Embed(
            title="Prompt Help",
            color=COLOR,
            description=msg)
    elif arg == "inspireme":
        msg = "Get some inspiration! Example: `%sinspireme`" \
              "\n\nResponses written by Caty, Dorea, Red, Essa, and Stuffle." % prefix
        embed = discord.Embed(
            title="InspireMe Help",
            color=COLOR,
            description=msg)
    elif arg.startswith("shouldikill"):
        msg = "Have some help deciding if you should kill your character. " \
              "Example: `%sshouldikillmycharacter`" % prefix
        embed = discord.Embed(
            title="ShouldIKillMyCharacter Help",
            color=COLOR,
            description=msg)
    elif arg == "shouldigetbacktowork":
        msg = "Have some help deciding if you should get back to work.\n\n" \
              "Example: `%sshouldigetbacktowork`" % prefix
        embed = discord.Embed(
            title="shouldIGetBacktoWork Help",
            color=COLOR,
            description=msg)
    elif arg == "whenshouldtheyfuck":
        msg = "Have some help deciding when your characters should fuck. " \
              "Most responses written by Red.\n\n" \
              "Example: `%swhenshouldtheyfuck`" % prefix
        embed = discord.Embed(
            title="WhenShouldTheyFuck Help",
            color=COLOR,
            description=msg)
    elif arg == "shouldifinishmywip":
        msg = "Have some help deciding if you should finish your WIP. " \
              "Most responses written by Tocasia, with some by Munchkin, Keta, and Sephirise.\n\n" \
              "Example: `%sshouldifinishmywip`" % prefix
        embed = discord.Embed(
            title="shouldIFinishMyWIP Help",
            color=COLOR,
            description=msg)
    elif arg == "randompair":
        msg = "Get a random pairing.\n\n" \
              "Example: `%srandompair`" % prefix
        embed = discord.Embed(
            title="RandomPair Help",
            color=COLOR,
            description=msg)
    elif arg == "kink":
        msg = "Get a random kink.\n\n" \
              "Example: `%skink`" % prefix
        embed = discord.Embed(
            title="Kink Help",
            color=COLOR,
            description=msg)

    elif embed is None:
        msg = "Sorry! This command is unrecognized. View the general help " \
              "for a list of commands with `%shelp`." % prefix
        embed = discord.Embed(
            title="Unrecognized Command",
            color=COLOR,
            description=msg)

    return embed


def general_help(prefix, guild_id):
    msg = "Commands list. For help on a specific command, run " \
          "`~help COMMAND`."

    embed = discord.Embed(
        title="Help",
        color=COLOR,
        description=msg)

    embed.add_field(
        name="Action Commands:",
        value="`hug`, `cheer`, `kidnap`",
        inline=False)
    embed.add_field(
        name="Inspiration Commands:",
        value="`inspireme`, `prompt`, `randomPair`, `kink`, `shouldIKillMyCharacter`, `shouldIGetBackToWork`, `shouldIFinishMyWIP`, `whenShouldTheyFuck`",
        inline=False)
    embed.add_field(
        name="For More Commands:",
        value="Mod only commands: `help mod`",
        inline=False)

    return embed
