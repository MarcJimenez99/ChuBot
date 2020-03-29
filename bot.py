import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

def check_list(name):
    with open("whitelist.txt", "r") as list_file: 
        flag = False
        for line in list_file.readlines():
            if str(name) in line:
                flag = True
        list_file.close()
        return flag
    
def add_list(name):
    with open("whitelist.txt", "a") as list_file: 
        list_file.write(f'\n{str(name)}')

def remove_list(name):
    with open("whitelist.txt", "r") as f: 
        lines = f.readlines()
    with open("whitelist.txt", "w") as f:
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

@bot.command()
async def help(ctx):
    embed = discord.Embed(color = discord.Color.orange())

    embed.set_author(name='Help:')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/178405015059169280/693425554627493898/chubot.jpg')
    embed.add_field(name='!help_commands', value='List of commands', inline=False)
    embed.add_field(name='!help_mod_commands', value='List of whitelisted commands', inline=False)
    
    await ctx.send(embed=embed)

@bot.command()
async def help_commands(ctx):
    embed = discord.Embed(color = discord.Color.orange())
    embed.set_author(name='Commands:')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/178405015059169280/693425554627493898/chubot.jpg')
    embed.add_field(name='!ping', value='Returns bot latency(ms)', inline=True)
    embed.add_field(name='!users', value='Returns # of users', inline=True)
    embed.add_field(name='!hello', value='Says hi!', inline=False)
    embed.add_field(name='!8ball', value='Answers the tough questions!', inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def help_mod_commands(ctx):
    embed = discord.Embed(color = discord.Color.orange())
    embed.set_author(name='Commands:')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/178405015059169280/693425554627493898/chubot.jpg')
    embed.add_field(name='!add_to_whitelist', value='Adds a user to the whitelist', inline=False)
    embed.add_field(name='!remove_from_whitelist', value='Removes a whitelisted user', inline=True)
    embed.add_field(name='!clear', value='Clears a number of messages', inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency * 1000)}ms')

@bot.command()
async def users(ctx):
    await ctx.send(f'The server has: {ctx.guild.member_count} users')

@bot.command(aliases=['HMPH', 'HMMPH'])
async def hmph(ctx):
    await ctx.send(f'You are a dumb bitch {ctx.message.author}!')


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
    responses = ['Hello {ctx.message.author}!',
    'Welcome to the server {ctx.message.author}!',
    'Hi {ctx.message.author}, how have you been!',
    'Whats up {ctx.message.author}!'
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
   
bot.run('Bot token goes here')
