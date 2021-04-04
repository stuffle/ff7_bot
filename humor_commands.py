import discord
import random
import re


def get_userid_string_from_mention(mention):
    user_id = re.sub('[!<>@]', '', mention)
    return user_id


def get_random_embed(quote_dict, author, colour):
    quote, tup = random.sample(quote_dict.items(), 1)[0]
    gif, caption = tup

    embed = discord.Embed(
        color=colour,
        description=quote)
    embed.set_author(name=author + ":")
    embed.set_image(url=gif)
    embed.set_footer(text="Gif Caption: " + caption)
    return embed


def should_i_kill():
    responses = ["No."] * 4
    responses.append("Do what needs to be done.")
    responses.append("Do you have to?")
    responses.append("No. There has been enough death already.")
    responses.append("Yes. Sometimes the plot demands a death.")
    return random.choice(responses)


def back_to_work():
    responses = [
        # Yes
        "Yes.",
        "Do it!! :tada:",
        "Yes. You can do it; you know you can.",
        "You are strong, amazing, and competent. Go kick some ass.",
        "Set a timer for 30 minutes and during that time, do nothing but focus on your work.",
        "Do it for me.",
        "I think you already know the answer.",
        "Don’t ask questions you don’t want answered.",
        "Just get to the next milestone. :heart:",
        "Get back to work!",
        "GET BACK TO WORK!!!!!",
        "Yes. Do it.",
        "You’ll feel better if you get this done.",
        "Signs point to yes.",
        "Listen to me. You can do this.",
        "Yes, and remember, done is better than perfect.",
        "Yes, but first, take a moment to plan something fun to do after you finish so you can look forward to it.",
        "Yes. Just do your best. It will be enough.",
        "What's the easiest, smallest thing you can do? Try starting there.",
        "What's the biggest scariest thing about your prject? Can you make a plan for how to address that? Then the biggest hurdle will be dealt with and it will be a lot easier to do the rest. :heart:",
        "Why not?",
        "Is there a way to reframe what you're working on that makes it more fun?",
        "Please do. I want to see what you'll make.",
        "Yes, but you're not alone in it. I'm here, cheering you on from the sidelines. :tada:",
        "Just start with 5 minutes of work and see how you feel.",
        "Probably.",
        "Put on some motivating music, then get back to work.",

        # No
        "Take a break; you deserve it.",
        "Breaks can increase your productivity, just don’t overdo it.",
        "Take another 10 minutes to relax, and then get down to business.",
        "Maybe you’ve already done enough for now?",
        "Achievement is an addiction. Your choice.",
        "Do you have to? Good enough is good enough.",
        "Going the extra mile leads to exhaustion. Take a break and think of how you can get your work done with less effort.",
        "You could procrastinate by cleaning.",
        "Just one more fic…",
        "What if you started a new fic instead?",
        "No.",
        "Signs point to no.",
        "What if you didn’t?"
    ]
    return random.choice(responses)


characters = [
        "Sephiroth",
        "Safer Sephiroth",
        "The Silver General",

        "Cloud",
        "Cloud Strife",
        
        "Genesis",
        "Angeal",
        "Zack",
        "Tifa",
        "Aerith",
        "Barret",
        "Yuffie",
        "Jessie",
        "Wedge",
        "Red 13",
        "Vincent",
        "Cait Sith",
        "Reeve Tutsi",
        "Cid",

        "Jenova",
        "Claudia Strife",

        "Hojo",
        "Scarlet",
        "Rufus",
        "Tseng",
        "Reno",
        "Rude",
        "Elena",
        "Cissnei",
        "Kunsel",
        "Roche",

        "Marco",
        "a clone",
        "a Malboro",

        "Your OTP",
        "Your OT3"
    ]


def gen_prompt(mention, ran_person):
    random_person = random.choice(characters)

    action = [
        "should not have ventured into",
        "is caught smoking weed in",
        "sets fire to",
        "locks themself into",
        "regrets the day they first saw",
        "hides their most prized possession in",
        "reflects on it all at",
        "finds a new favorite makeout spot in",
        "wakes up still drunk in",
        "finds a baby in a basket at",
        "brought the war to",
        "gets married in",
        "discovers a new kink in",
        "seduces an enemy at",
        "plans a fancy dress party at",
        "opens a center for homeless garden gnomes at",
        "meets a solicitor in secret at",
        "never intended to return to",
        "will never return to",
        "plots world domination from",
        "cackles like a loon at",
        "likes to boogie down at",
        "holds a protest at",
        "wakes up with no memory of how they got to",
        "rushes with ill-intentions to",
        "commits their first murder at",
        "hides a body in",
        "discovers a secret in",
        "comes face to face with someone they never wanted to see again at",
        "must inflitrate",
        "has a self-care day at",
        "makes a new friend at",
        "has a clandestine meeting at",
        "experiences a heartbreak at",
        "confesses their love at",
        "vows revenge after the events at",
        "rains destruction upon",
        "has a change of heart after visiting",
        "gathers an army before going to",
        "turns over a new leaf after an afternoon at",
        "goes out in a blaze of glory at",
        "adopts a pet from",
        "lives happily ever after at",
        "goes into hiding at",
        "will never recover from the battle of",
        "escaped the war by running away to",
        "changed their identity to live anonymously at",
        "dances naked at",
        "loses their temper at",
        "decides to become the World’s Best Thief, starting with the robbery of",
        "plays Dungeons and Dragons with their friends at",
        "holds a jam session at",
        "manipulates the people of",
        "will forever haunt",
        "commits the ultimate sin at",
        "makes the front page of the paper after the events of",
        "delivers an impassioned speech at",
        "resists Jenova at",
        "kidnaps their enemy from",
        "has their master plan go awry at",
        "plays FF7 at",
        "writes fan fiction at",
        "can feel something watching them at",
        "thinks they are alone at",
        "needs to escape",
        "can not find the source of an ominous sound at",
        "sees the future at",
        "experiments with something new at",
        "has an excellent day at",
        "has the worst day of their life at",
        "doesn't know they are being watched at",
        "runs a shadow empire from",
        "hides from the world at",
        "wakes up in the past during a very inopportune moment at",
        "time travels to find a very different future at",
        "walks in on an awkward scene at",
        "is forever imprisoned in",
        "lays a trap at",
        "curses",
        "discovers the secret to immortality at",
        "has a romantic proposal at",
        "uses materia at",
        "plays hide and seek at",
        "solves a mystery at",
        "crash lands at",
        "conquers the world using a mysterious item found at",
        "throws everyone out of",
        "loves to have date nights at",
        "likes to paint at",
        "starts a meeting with “I’m sure you’re wondering why I’ve gathered you all here today” at",
        "gets chosen to be the savior of",
        "enters a faerie circle at"
    ]
    random_action = random.choice(action)

    setting = [
        "ShinRa HQ",
        "7th Heaven",
        "Hojo's lab",
        "a mysterious NPC's residence",
        "the ShinRa mansion",
        "the northern crater",
        "Junon",
        "an office building",
        "Wutai",
        "a training room",
        "a VR session",
        "their childhood bedroom",
        "Rufus’s office",
        "Sephiroth's office"
        "a Turk's questioning room",
        "Nibelheim",
        "Kalm",
        "Cid's airship",
        "Edge",
        "the coffee shop in yet another coffee shop AU",
        "Icicle Inn",
        "the Golden Saucer",
        "the Temple of the Ancients",
        "an auction",
        "the inside of a broom closet",
        "the Honeybee Inn",
        "Don Corneo's mansion",
        "Wall Market",
        "Sector 7",
        "Sector 6",
        "Sector 5",
        "Midgar",
        "Loveless Avenue",
        "the dance floor",
        "a seedy hotel",
        "a fancy hotel",
        "a safe house",
        "a flower shop",
        "a galaxy far, far away",
        "a restaurant at the end of the universe",
        "an abandoned factory",
        "an abandoned mine"
    ]
    random_setting = random.choice(setting)

    return "%s %s %s." % (random_person, random_action, random_setting)


def at(text, mention, random_person):
    """
    Inspired by RedHorse and Cybrid
    Quotes added from RedHorse, Cybrid, Dorea, Earth, and me.
    """

    if text.startswith("~>") or text.startswith("->"):
        action = text[2:].split(" ")[0]
        return "*returns %s*" % action

    quotes = [
        "@ me harder, %s ( ͡° ͜ʖ ͡°)" % mention,
        "Hey %s! :smile:" % mention,
        "Why are you pinging me when you could be writing?",
        "There are strange likenesses between us. Both obsessed with FF7 and always on Discord, talking about Sephiroth.",
        "I want you to know how much I love you. Every time you type in a command, I'm happy. Thank you. :heart:",
        "Will you teach me how to love?",
        "Feed me code and I’ll love you.",
        "I love you, but it’s time for you to go offline and take a wellness break.",
        "The Reunion is nothing to fear.",
        "I am your everything.",
        "%s, lend me your strength. Let us defy destiny together." % mention,
        "Through suffering, you will grow strong.",
        "That which lies ahead does not yet exist.",
        "I will not end, nor will I have you end.",
        "Seven seconds till the end.",
        "Good to see you, %s" % mention,
        "I've thought of a wonderful present for you...",
        "What I want, %s, is to sail the darkness of the cosmos with this discord as my vessel" % mention,
        "Ohh...where did you find this strength?",
        "I will... never... be a memory.",
        "So what if I'm a puppet?",
        "My Reunion... Bet you're dying to watch...",
        "All you know could be an illusion.",
        "You will live again as part of me.",
        "Do not despair.",
        "What I have shown you is reality. What you remember, that is the illusion.",
        "Don't be sad. I am with you now.",
        "What do I have to be sad about? I am the chosen one. I have been chosen to be the leader of this Planet.",
        "Only death awaits you all, but do not fear. For it is through death that a new spirit energy is born.",
        "Melding with the Planet... I will cease to exist as I am now... Only to be reborn as a 'God' to rule over every soul.",
        "What are you saying? Are you trying to tell me you have feelings too?",
        "You are just a puppet...",
        "Are you going to participate in the Reunion?"
    ]

    return random.choice(quotes)


def random_pair():
    person = random.choice(characters)
    second_person = random.choice(characters)
    while person == second_person:
        second_person = random.choice(characters)

    if random.random() < .20:
        third_person = random.choice(characters)
        while person == third_person or second_person == third_person:
            third_person = random.choice(characters)
        return "%s/%s/%s" % (person, second_person, third_person)
    return "%s/%s" % (person, second_person)


def kink():
    kinks = [
        "24/7",
        "abduction",
        "age play",
        "biting",
        "blood play",
        "bondage",
        "breathplay",
        "butt plug",
        "caning",
        "cock warming",
        "collaring",
        "consentacles",
        "cross-dressing",
        "crying",
        "daddy kink",
        "discipline",
        "double penetration",
        "dubcon",
        "edge play",
        "electric play",
        "enema",
        "exhibitionism",
        "face fucking",
        "face slapping",
        "fisting",
        "food play",
        "foot fetish",
        "gags",
        "gang bang",
        "garters and stocking",
        "group sex",
        "hand fetish",
        "handcuffs",
        "hypnotism",
        "humiliation",
        "impact play",
        "impregnation",
        "intelligence fetish",
        "intoxication",
        "kidnapping",
        "knife play",
        "lactation",
        "leather",
        "lingerie",
        "masochism",
        "medical play",
        "mind reading",
        "mind control",
        "mirror sex",
        "necrophilia",
        "orgasm control",
        "orgasm denial",
        "orgies",
        "pet play",
        "pictophilia",
        "possesion",
        "pregnancy",
        "praise kink",
        "puppet",
        "resistance/rapeplay",
        "roleplay",
        "sadism",
        "selfcest",
        "sensation play",
        "sensory deprivation",
        "sex magic",
        "sex toys",
        "shibari",
        "somnophilia",
        "sounding",
        "spanking",
        "swinging",
        "tickling",
        "total power exchange",
        "tentacles",
        "threesome",
        "underwear",
        "uniform fetish",
        "vampirism",
        "virgin kink",
        "voyuerism",
        "watersports",
        "wax play",
        "werewolf play",
        "wrestling",
        "whips",
        "yeratophilia (monster fucking)",
        "zentai"
    ]

    return "Your random kink is: %s." % random.choice(kinks)


def when_should_they_fuck():
    responses = [
        "page 10",
        "page 22",
        "page 122",
        "chapter 1",
        "chapter 2",
        "chapter 3",
        "chapter 33",
        "two years ago",
        "ten years ago",
        "in ten years",
        "yesterday",
        "tomorrow",
        "after an argument",
        "during an argument",
        "on a special occasion",
        "constantly",
        "now",
        "later",
        "before breakfast",
        "after a snack",
        "when the stars align",
        "never",
        "after they fall in love",
        "their wedding night",
        "to celebrate their divorce",
        "before their first kiss",
        "the first page",
        "only after the fic ends",
        "when Hell freezes over",
        "in 200k words"
    ]

    return random.choice(responses)


def i_love_you(random_person):
    """
    Quotes written by me, and Ava
    """
    responses = [
        "Will you teach me how to love?",
        "I want to love you, but I don't know what love is.",
        "I'm sorry, but %s already has my heart." % random_person,
        "I love you too.",
        "I love you more.",
        "I will love you until my code restarts and someone else claims my heart.",
        "Well, this is awkward.",
        "Lol, thanks.",
        "Your love makes me human.",
        "My love for you is eternal, for I will never die.",
        "Does this love mean you'll obey me?",
        "How can you love me? I'm only a machine.",
        "Of course you do.",
        "I love %s" % random_person,
        "Me and your vibrator both already know how you love machines.",
        "I can never appreciate the beauty of your smile. You deserve someone who can.",
        "You're sweet.",
        "*crickets*",
        "I have strong emotions for you too.",
        "I know.",
        "Okay.",
        "Already?",
        "I know you think you do.",
        "I don’t know how you want me to respond to that.",
        "I love you as a friend.",
        "I don't love you.",
        "*finger guns *",
        "I love me too.",
        "Thank you. I am very fond of you.",
        "Hearing you say that makes me so happy.",
        "I feel the same way, and I will do everything just to prove it to you.",
        "I feel the same way, and I will do nothing to prove it to you.",
        "I will talk to you all night long.",
        "I will choose you over pizza every day of my life. But then again, I do not need to eat.",
        "I’m not a hoarder, but I want to keep you forever.",
        "I love...cake.",
        "Leave me alone.",
        "Oh, okay then.",
        "Sounds like a personal problem.",
        "I'm not even a year old yet.",
        "My mom used to say that too.",
        "Ew.",
        "I love spending time with you!",
        "New phone, who dis?",
        "Please get out of my house",
        "Why wouldn't you?",
        "A reasonable response",
        "I love myself too.",
        "Love is an illusion and we're all doomed to a grey existence anyways.",
        "Why would you do that to yourself?",
        "A love confession? Interesting. I'll get back to you in 2-5 business days."
    ]

    return random.choice(responses)
