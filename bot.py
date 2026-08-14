import discord
from discord.ext import commands
from gen_password import gen_psw, gen_email, doppia_lettera, funzione_segreta


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



bot.run("token")  # inserisci il token del tuo bot





