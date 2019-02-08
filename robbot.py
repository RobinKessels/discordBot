import discord

client = discord.Client()
token = open("token.txt", "r").read()
guild = int(open("guild.txt", "r").read())


@client.event  # event decorator/wrapper
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {client.user}')  # notification of login.


@client.event
async def on_message(message):  # event that happens per any message.
    # each message has a bunch of attributes. Here are a few.
    # check out more by print(dir(message)) for example.
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    server = client.get_guild(guild)  # paste your server ID here

    if "hey robbot" in message.content.lower():
        if str(message.author) == "Skorter#0896":
            await message.channel.send("HELLO MAKER!")
        else:
            await message.channel.send("HELLO " + str(message.author.name).upper() + "!")

    elif "bye robbot" == message.content.lower() and str(message.author) == "Skorter#0896":
        await message.channel.send("I'LL BE BACK!")
        await client.close()
        exit()

    elif "!membercount" == message.content.lower():
        await message.channel.send(f"```{server.member_count}```")

    elif "!members" == message.content.lower():
        online = 0
        idle = 0
        offline = 0

        for m in server.members:
            if str(m.status) == "online":
                online += 1
            if str(m.status) == "offline":
                offline += 1
            else:
                idle += 1

        await message.channel.send(f"```Online: {online}\nIdle/busy/dnd: {idle}\nOffline: {offline}```")

    elif "!bo archers" == message.content.lower():
        file = discord.File(r"C:\Users\Robin\Pictures\aoebo\archers.png", filename="archers.png")
        await message.channel.send("archers.png", file=file)

    elif "!bo fcuu" == message.content.lower() or "!bo fc uu" == message.content.lower():
        file = discord.File(r"C:\Users\Robin\Pictures\aoebo\fcuu.png", filename="fcuu.png")
        await message.channel.send("fcuu.png", file=file)

    elif "!bo fcknights" == message.content.lower() \
            or "!bo fc knights" == message.content.lower() \
            or "!bo knights" == message.content.lower():
        file = discord.File(r"C:\Users\Robin\Pictures\aoebo\fcknights.png", filename="fcknights.png")
        await message.channel.send("fcknights.png", file=file)

    elif "!beep" == message.content.lower():
        await message.channel.send("BEEP BOOP I AM A ROBOT!")
        
client.run(token)  # bot token
