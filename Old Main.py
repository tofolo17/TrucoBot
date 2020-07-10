import random
import discord
import asyncio

client = discord.Client()


@client.event
async def on_ready():
    print('-- BOT ONLINE! --')
    print(f'O nome do bot é: {client.user.name}')
    print(f'O ID do bot é: {client.user.id}')
    print(client.guilds)


@client.event
async def on_message(message):
    # Mensagens no console e ignorando envios do bot
    if message.author == client.user:
        return
    else:
        print(f'Message from {message.author} content: {message.content}')

    # Respondendo
    if message.content.lower().startswith('!truco'):
        await message.channel.send("TRUCO PORRA!")
        guild = client.get_guild(724488722459918358)
        await discord.Guild.create_text_channel(guild, 'TrucoRoom')
        # await client.get_guild(id).delete()

    # Permissão e adição de reação
    if message.content.lower().startswith('!moeda'):
        if message.author.id == 645313554001428511:
            escolha = random.randint(1, 2)
            if escolha == 1:
                await message.add_reaction('😀')
            if escolha == 2:
                await message.add_reaction('👑')
            else:
                await message.channel.send("Você não tem permissão, otário!")


client.run('TOKEN')
