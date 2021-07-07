import discord
import os
from discord import channel
import requests
import json
import random


client = discord.Client()

# Fuction to use an api to retrieve information formatted in json and then pull one item out of the info thats returned.
def get_fact():
    response = requests.get("https://catfact.ninja/fact")
    json_data = json.loads(response.text)
    fact = json_data['fact']
    return fact

# Same as above function just more data returned in this one
def get_breed():
    response = requests.get("https://catfact.ninja/breeds")
    json_data = json.loads(response.text)
    breed = json_data['data'][random.randint(0, 24)]['breed']
    return breed

# Notification that the bot is up and running correctly
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# Listens for a specific type of message in discord and responds based on that message
@client.event
async def on_message(message):
    if message.content.startswith('!cat fact'):
        fact = get_fact()
        await message.channel.send(fact)
    if message.content.startswith('!cat breed'):
        breed = get_breed()
        await message.channel.send(breed)

# CATBOTTOKEN is in the envrionment variables for my computer and is being accessed via this method.
client.run(os.environ.get('CATBOTTOKEN'))

