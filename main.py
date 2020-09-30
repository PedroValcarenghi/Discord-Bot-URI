# -*- coding: utf-8 -*-
# author = Pedro Augusto
# version = 1.0
# Thanks to https://repl.it/@GarethDwyer1

# Flask 
from keep_alive import keep_alive
# 

# Discord Dependences
import discord
import os
# 

# Scraper Dependences
from bs4 import BeautifulSoup
import requests
# 


client = discord.Client()


@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
    if message.author != client.user:
        await client.send_message(message.channel, message.content[::-1])


url = 'https://www.urionlinejudge.com.br/repository/UOJ_1561.html'
html_source = requests.get(url).text

soup = BeautifulSoup(html_source, 'html.parser')

users = soup.find('div', {'class':'problem'})
print(users.text)


keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)