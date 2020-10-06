import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import os

client = commands.Bot(command_prefix = "!")
#answers with the ms latency
@client.command()
async def URI(ctx):
    url = 'https://www.urionlinejudge.com.br/repository/UOJ_1561.html'
    html_source = requests.get(url).text
    soup = BeautifulSoup(html_source, 'html.parser')
    problem = soup.find('div', {'class':'problem'})
    await ctx.send(problem.text)

token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)