import discord
from discord import app_commands
import asyncio

client = discord.Client(intents = discord.Intents.all())
guild = discord.Object(id = ID BOT)

@client.event
async def on_ready():
    print("Bot en ligne")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    check_channel = client.get_channel(1214989362778087484)
    if message.channel == check_channel:
        if "https://www.themoviedb.org" in message.content or "https://themoviedb.org" in message.content:
                suggestion_channel = client.get_channel(1214989425717551156)
                suggestion_message = f"**{message.author.mention} te suggère de regarder :**\n\n{message.content}"
                await suggestion_channel.send(suggestion_message)
                reponse_bon_format = await message.channel.send(f"Merci pour ta suggestion {message.author.mention} !")
                await message.delete()
                await asyncio.sleep(5)
                await reponse_bon_format.delete()
        else:
            reponse_mauvais_format = await message.channel.send(f"Format Incorrect {message.author.mention} \n \n Le Format à respecter est le suivant : \n Titre : titre (année) \n Genre : \n Lien infos : https://www.themoviedb.org/movie/xxxxxx")
            await message.delete()
            await asyncio.sleep(5)
            await reponse_mauvais_format.delete()


client.run("TOKEN PRIVE")
