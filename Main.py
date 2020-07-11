import discord
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix='!')


# Events
@client.event
async def on_ready():
    print('bot is ready')
    status_list = ['o zap na testa do bêbado', 'truco consigo mesmo',
                   'a mesa do bar pela janela', 'um 4 depois de ter pedido 12']  # |!help
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
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('Cheguei rapaziada!')
        break


@client.event
async def on_guild_channel_create(channel):
    try:
        await channel.send('Bora!')
        # play()
    except (ValueError, Exception):
        pass


# Commands
@client.command()
async def truco(ctx, *, member: discord.Member = None):
    if member is None:  # Transformar em lista de opções
        guild_categories, verified_txt_channels = [], []
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
            await guild.create_text_channel(f'Cartas do {ctx.message.author}', overwrites=overwrites,
                                            category=new_category)
            await ctx.send('Acha que ganha de mim? Não fode. Entre no canal de texto com seu nome, zé.')
        else:
            for channel in guild.text_channels:
                verified_txt_channels.append(channel.name)
            if f'cartas-do-{member.name.lower()}{member.discriminator}' not in verified_txt_channels:
                for category in guild.categories:
                    if category.name == 'Mesa de bar':
                        await guild.create_text_channel(f'Cartas do {ctx.message.author}', overwrites=overwrites,
                                                        category=category)
                        await ctx.send('Acha que ganha de mim? Não fode. Entre no canal de texto com seu nome, zé.')
            else:
                await ctx.send("Suas cartas já foram entregues! "
                               "Verifique a existência do canal de texto com seu nome!")
    else:
        print('*')


@client.command()
async def leave(ctx):
    cont2 = 0
    member = ctx.message.author
    channel = ctx.message.channel
    if channel.name == f'cartas-do-{member.name.lower()}{member.discriminator}':
        await channel.delete()
        for text_channel in ctx.message.guild.text_channels:
            if text_channel.category == channel.category:
                cont2 += 1
        if cont2 == 0:
            await channel.category.delete()


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Não sei o que fazer com isso, parça.')


client.run('Token')
