import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

def check_list(name):
    with open("FirstDiscordBot/whitelist.txt", "r") as list_file: 
        flag = False
        for line in list_file.readlines():
            if str(name) in line:
                flag = True
        list_file.close()
        return flag
    
def add_list(name):
    with open("FirstDiscordBot/whitelist.txt", "a") as list_file: 
        list_file.write(f'\n{str(name)}')

def remove_list(name):
    with open("FirstDiscordBot/whitelist.txt", "r") as f: 
        lines = f.readlines()
    with open("FirstDiscordBot/whitelist.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != str(name):
                f.write(line)

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event
async def on_member_join(member):
    print(f'{member} has joined.')
    for channel in member.guild.channels:
        if str(channel) == "general_cancer":
            await channel.send(f"""Welcome {member} to the server!""")

@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server.')
    for channel in member.guild.channels:
        if str(channel) == "general_cancer":
            await channel.send(f"""{member} has left the server.""")

# @bot.command()
# async def help(ctx)

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency * 1000)}ms')

@bot.command()
async def users(ctx):
    await ctx.send(f'The server has: {ctx.guild.member_count} users')

@bot.command()
async def clear(ctx, amount=1):
    perm = check_list(str(ctx.author))
    if perm:
        await ctx.channel.purge(limit=amount+1)
    else:
        await ctx.send(f'You do not have permission to do that')

@bot.command()
async def add_to_whitelist(ctx, *, name):
    perm = check_list(str(ctx.author))
    exists = check_list(str(name))

    if perm and not(exists):
        add_list(str(name))
        await ctx.send(f'{name} has been whitelisted.')
    elif perm and exists:
        await ctx.send(f'{name} is already whitelisted')
    else:
        await ctx.send(f'You do not have permission to do that')

@bot.command()
async def remove_from_whitelist(ctx, *, name):
    perm = check_list(str(ctx.author))
    exists = check_list(str(name))

    if perm and exists:
        remove_list(str(name))
        await ctx.send(f'{name} has been removed from the whitelist.')
    elif perm and not(exists):
        await ctx.send(f'{name} is not on the whitelist')
    else:
        await ctx.send(f'You do not have permission to do that')

@bot.command(aliases =['Hey','Hello','hey'])
async def hello(ctx):
    responses = ['Hello!',
    'Welcome to the server!',
    'Hi how have you been!',
    'Whats up!'
    ]
    await ctx.send(f'{random.choice(responses)}')

@bot.command(aliases=['8ball', '8Ball'])
async def _8ball(ctx, *, question): # Asterik takes in all following arguments
    responses = ['It is certain.',
                'It is decidedly so.',
                'Without a doubt.',
                'Yes – definitely.',
                'You may rely on it.',
                'As I see it, yes.',
                'Most likely.',
                'Outlook good.',
                'Yes.',
                'Signs point to yes.',
                'Reply hazy, try again.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                'Don’t count on it.',
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Very doubtful.',
    ]  
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
   
bot.run('NjkyNjY3Mzg0MDQ0OTc4MjUw.Xn7LAg.zpUYFdJewF6GiEWyNG-gCh9yPuY')
