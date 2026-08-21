import discord
from discord.ext import commands
from gen_password import gen_psw, gen_email, doppia_lettera
import random
import os

# la variabile intents contiene i permessi al bot
intents = discord.Intents.default()
# abilita il permesso a leggere i contenuti dei messaggi
intents.message_content = True
# crea un bot e passa gli indents
bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {bot.user}')

@bot.command()
async def ciao(ctx,nome):
    await ctx.send(f'Ciao! {nome}')

@bot.command()
async def arrivederci(ctx):
    await ctx.send("\U0001f642")

@bot.command()
async def gen_pasw(ctx):
    password = gen_psw()
    await ctx.send(password)

@bot.command()
async def gioco(ctx,game):
    await ctx.send(f"il gioco migliore da giocare è {game}")

@bot.command()
async def doppia(ctx, s):
    lettera = doppia_lettera(s)
    await ctx.send(doppia_lettera(s))

@bot.command()
async def meme01(ctx):
    immagini = ['dev1.jpg', 'dev2.jpg', 'dev3.jpg']
    random_meme = random.choice(immagini)
    with open(f'meme/dev/{random_meme}', 'rb') as f:
        img_discord = discord.File(f)
        await ctx.send(file=img_discord)
    

@bot.command()
async def meme(ctx, tipo):
    if tipo == "scritti":
        cartella = "meme/meme scritti"
    elif tipo == "immagini":
        cartella = "meme/meme immagini"
    else:
        await ctx.send("Scrivi `meme scritti` oppure `meme immagini`")
        return

    immagini = os.listdir(cartella)
    random_meme = random.choice(immagini)

    with open(f"{cartella}/{random_meme}", "rb") as f:
        img_discord = discord.File(f)
        await ctx.send(file=img_discord)


bot.run("token")  # inserisci il token del tuo bot





