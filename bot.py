import discord

from gen_password import gen_psw, gen_email


# la variabile intents contiene i permessi al bot
intents = discord.Intents.default()
# abilita il permesso a leggere i contenuti dei messaggi
intents.message_content = True
# crea un bot e passa gli indents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$ciao'):
        await message.channel.send("Ciao!")
    elif message.content.startswith('$arrivederci'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith("sono triste"):
        await message.channel.send("\U0001F622")
    elif message.content.startswith("migliori giochi da giocare"):
            await message.channel.send("i migliori giochi da giocare sono: Forza Horizon 6, il survival horror Resident Evil Requiem, l'avventura retrò Mina the Hollower, e la novità creativa Pokémon Pokopia.")
    elif message.content.startswith("genera password"):
        password = gen_psw()
        await message.channel.send(password)
    elif message.content.startswith("genera email"):
        email = gen_email()
        await message.channel.send(email+"@gmail.com")
    else:
        await message.channel.send(message.content)

client.run("token")  # inserisci il token del tuo bot
