import discord
import random
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix='!')


# Events
@client.event
async def on_ready():
    print('bot is ready')
    status_list = ['o zap na testa do bêbado', 'truco consigo mesmo',
                   'a mesa do bar pela janela', 'um 4 depois de ter pedido 12']
    cont = 0
    while True:
        status = status_list[cont]
        await client.change_presence(status=discord.Status.online, activity=discord.Game(status))
        await asyncio.sleep(10)
        if cont < len(status_list) - 1:
            cont += 1
        else:
            cont = 0


@client.event
async def on_member_join(member):
    print(f'{member} has joined the served.')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Não sei o que fazer com isso, parça.')


# Commands
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


@client.command(aliases=['8ball', 'eightball'])
async def _8ball(ctx, *, question):
    responses = ['Probably',
                 'I would not be so sure about that.',
                 'My answer is no.',
                 'Probably not',
                 'Of course!',
                 'Why not?',
                 'My answer is yes.',
                 'This is true, and it will stay like that.',
                 'Not even in a million years.',
                 'I mean, I do not see the point in saying no.',
                 'Why this question? The answer is a definitive no.',
                 'As my grandma used to say... no.',
                 'As my great great grandfather used to say... what even is this question?',
                 'I do not know.',
                 'Sources say no.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@_8ball.error
async def _8ball_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Falta a pergunta, cabeção.')


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount + 1)


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('Lhe falta poder!')


@client.command()
async def porn(ctx):
    pages_list = ['xvideos', 'beeg', 'pornhub']
    sufix_list = ['/new/', '/page/', '/video?page=']
    page = random.choice(pages_list)
    sufix = 0
    for element in pages_list:
        if page == element:
            await ctx.send(f'https://{page}.com{sufix_list[sufix]}{random.randint(1, 100)}')
        else:
            sufix += 1


@client.command()
async def truco(ctx):
    guild_categories = []
    guild = ctx.message.guild
    member = ctx.message.author
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        member: discord.PermissionOverwrite(read_messages=True)
    }
    for category in guild.categories:
        guild_categories.append(category.name)
    if "Mesa de bar" not in guild_categories:
        new_category = await guild.create_category('Mesa de bar')
        await guild.create_text_channel(f'Cartas do {ctx.message.author}', overwrites=overwrites, category=new_category)
    else:
        for category in guild.categories:
            if category.name == 'Mesa de bar':
                await guild.create_text_channel(f'Cartas do {ctx.message.author}', overwrites=overwrites,
                                                category=category)


"""
@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked: {member.mention}')
    

@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned: {member.mention}')
    
    
@client.command()
async def unban(ctx, *, member):  # esse membro não está no servidor
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return
"""

client.run('')

"""
Aula 7 - Cogs
Aula 8 - First comment interessante
Aula 12 - Prefixos personalizáveis
"""
