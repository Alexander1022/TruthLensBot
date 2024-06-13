import discord
from discord.ext import commands
from request_manager import RequestManager

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)
rm = RequestManager()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

@bot.tree.command(name="get_info", description="Връща колко достоверна е дадена новина.")
async def slash_command(interaction: discord.Interaction, prompt: str):    
    await interaction.response.defer() 
    print("User asked : " + prompt)
    response = rm.get_user_info(prompt)
    response = rm.get_beatiful_info(response)
    await interaction.followup.send(response)

bot.run('abc123')
