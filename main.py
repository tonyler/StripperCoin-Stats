import discord
import asyncio
import os
import pytz
from datetime import date, datetime
from discord.ext import commands

from datacollector import DataCollector

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='!', intents=intents)


#A custom function to to tranfrom numbers into human-readable formats with suffixes
def formatIt(hello):
    hello = str(hello)
    if hello.isalpha(): 
        return hello 
    else: 
        hello=int(hello)
        suffixes = ["", "K", "M", "B", "T"]
        hello = str("{:,}".format(hello))
        commas = 0
        x = 0
        while x < len(hello):
            if hello[x] == ',':
                commas += 1
            x += 1
        return hello.split(',')[0] + '.' + hello.split(',')[1][:-1] + suffixes[commas]


@bot.event
async def on_ready():
    print(f'You have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.content == "Start bot 2 boobz" 
        await message.channnel.send ("``Bot initializing\nGive me a minute``") 
    if message.author == bot.user : 
        messageID = message.id 
        channelID = message.channel.id 
        strip = DataCollector()
        while True:

            today = date.today().strftime("%B %d, %Y")
            utc_timezone = pytz.timezone('UTC')
            athens_timezone = pytz.timezone('Europe/Athens')
    
            await strip.dynamic_data()
    
            messageToBeSent = ':calendar: **' + today + '** :calendar:\n**__StripperCoin Stats - Update/2 minutes__**\n\n'
            messageToBeSent = messageToBeSent + ':dollar: `Price:` **$' + str(strip.price) + '**\n'+'<:cardano:1131689885124796416> `Price in Αda:` **₳' + str(strip.ada) +'**\n:moneybag: `Market Capitalization:` **$' + str(formatIt(strip.market_cap)) +'**\n<:minswap:1135312447264272487> `Total Value Locked:` **₳' + str(formatIt(strip.tvl)) +'**\n:gem: `Total Holders:` **' + str((strip.holders)) + '**'
            messageToBeSent = messageToBeSent + '```Supply Stats```:left_luggage: `Max Supply:` **' + '{:,}'.format(int(strip.supply)) + '**\n:briefcase: `Current Supply:` **' + '{:,}'.format(strip.supply) + '**\n:recycle: `Circulating Supply:` **' + '{:,}'.format(strip.supply) +'**\n'
            messageToBeSent = messageToBeSent + '```Resources```<:frost:1135528912592576672> [Blockfrost](<https://blockfrost.io/>) \n<:gecko:1135528843529166929> [CoinGecko](<https://www.coingecko.com/>) \n<:minswap:1135312447264272487> [MinSwap](<https://app.minswap.org/>)\n<:strip:1135350102349860937> [StripperCoin](<https://www.strippercoin.io/>)\n'
            messageToBeSent = messageToBeSent +"\n***Coded and hosted by <@817451374811152474> :mountain: ***"
            messageToBeSent = messageToBeSent +"\n*Help me keep this bot online* :heart:"
            messageToBeSent = messageToBeSent +"\n*I'm just a community member!*☕"
            messageToBeSent = messageToBeSent+"\n Last update: "+str(datetime.now(utc_timezone).strftime("%H:%M:%S")+" UTC")
    
            channel = bot.get_channel(channelID)
            message = await channel.fetch_message(messageID)
            await message.edit(content=messageToBeSent)
    
    
            print('Updated on: ' + str(datetime.now(athens_timezone).strftime("%H:%M:%S")))
            print ("__________________________")
            await asyncio.sleep(120) #execute again in 2 minutes

messageID = 1131663427635523604
channelID = 1131658164870320328
BOT_TOKEN = os.environ.get("DISCORD_KEY")

bot.run(BOT_TOKEN)
