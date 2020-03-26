import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event
async def on_member_join(member):
    print(f'YAHYEET {member} has joined.')
    for channel in member.guild.channels:
        if str(channel) == "general_cancer":
            await channel.send(f"""YAHYEET {member} has joined.""")

@bot.event
async def on_member_remove(member):
    print(f'{member} is a fucking p00sy.')
    for channel in member.guild.channels:
        if str(channel) == "general_cancer":
            await channel.send(f"""{member} is a fucking p00sy.""")

@bot.event
async def on_message(message):
    id = bot.get_guild(178405015059169280)
    channels = ["bot_commands"]

    if str(message.channel) in channels:
        if message.content.find("!hello") != -1:
            await message.channel.send("What up little bitch")
        elif message.content == "!users":
            await message.channel.send(f"""# of Members {id.member_count}""")
        
bot.run('NjkyNjY3Mzg0MDQ0OTc4MjUw.Xnx2-g.7BR-r4YK8afv4jtRUTr3FjaPl1M')
