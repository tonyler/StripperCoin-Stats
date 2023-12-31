import discord
import asyncio
import os
from datetime import date, datetime
from discord.ext import commands, tasks
from datacollector import DataCollector
from human_readable import formatIt
import embed

intents = discord.Intents.all()
intents.typing = True
intents.presences = True
intents.message_content = True  

bot = commands.Bot(command_prefix="/", intents=intents)
strip = DataCollector()
saved_message = [[1131663427635523604,1131658164870320328]]



async def message_creation(strip):     
    today = date.today().strftime("%B %d, %Y")
    messageToBeSent = ':calendar: **' + today + '** :calendar:\n**__StripperCoin Stats - Update/2 minutes__**\n\n'
    messageToBeSent = messageToBeSent + ':dollar: `Price:` **$' + str(strip.price) + '**\n'+'<:cardano:1131689885124796416> `Price in Αda:` **₳' + str(strip.ada) +'**\n:moneybag: `Market Capitalization:` **$' + str(formatIt(strip.market_cap)) +'**\n<:minswap:1135312447264272487> `Total Value Locked:` **₳' + str(formatIt(strip.tvl)) +'**\n:gem: `Total Holders:` **' + str((strip.holders)) + '**'
    messageToBeSent = messageToBeSent + '```Supply Stats```:left_luggage: `Max Supply:` **' + '{:,}'.format(int(strip.supply)) + '**\n:briefcase: `Current Supply:` **' + '{:,}'.format(strip.supply) + '**\n:recycle: `Circulating Supply:` **' + '{:,}'.format(strip.supply) +'**\n'
    messageToBeSent = messageToBeSent + '```Resources```<:frost:1135528912592576672> [Blockfrost](<https://blockfrost.io/>) \n<:gecko:1135528843529166929> [CoinGecko](<https://www.coingecko.com/>) \n<:minswap:1135312447264272487> [MinSwap](<https://app.minswap.org/>)\n<:exxx:1135350359364227204> [StripperCoin](<https://www.strippercoin.io/>)\n'
    messageToBeSent = messageToBeSent +"\n***Coded and hosted by <@817451374811152474> :mountain: ***"
    messageToBeSent = messageToBeSent +"\n*Help me keep this bot online* :heart:"
    messageToBeSent = messageToBeSent +"\n*I'm just a community member!*☕"
    messageToBeSent = messageToBeSent+"\n Last update: "+(strip.update)
    return messageToBeSent


async def fixed_messages(saved_message):
    while True: 
        if saved_message:
            message_content = await message_creation(strip)
            channel = bot.get_channel(saved_message[1])
            message = await channel.fetch_message(saved_message[0])
            await message.edit(content=message_content)

            current_time = datetime.now()
            current_time_str = current_time.strftime('%H:%M:%S')
            print (f"Done updating post at {current_time_str}")
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            await asyncio.sleep(120)
                
                
@bot.event
async def on_ready():
    print(f'You have logged in as {bot.user}')
    update.start()
    await asyncio.sleep(5)
    for message in saved_message:
        await fixed_messages(message) #starts the loop for the pre-selected hard-coded messages that need to be online 24/7


@bot.event
async def on_message(message):
    await bot.process_commands(message)   
    if message.author == bot.user :      
        if message.content == "``This will take less than 2 minutes.``": 
            saved_message=[message.id,message.channel.id]
            await fixed_messages(saved_message)


@bot.command(name="stats_forever")
async def stats_247(ctx):
        await ctx.send ("``This will take less than 2 minutes.``")


embed_stats = embed.stats()
@bot.command(name="stats")
async def send_embed(ctx):
    print (f"Stats command by ~{ctx.author.name}")
    embed_stats.set_field_at(index=0,name='Current Price :dollar:', value=(f"{strip.price} $"), inline=False)
    embed_stats.set_field_at(index=1,name='Price in Ada <:cardano:1131689885124796416>', value=(f"{strip.ada} ₳"), inline=False)
    embed_stats.set_field_at(index=2,name="Market Cap :moneybag:",value=(f"{formatIt(strip.market_cap)} $"), inline=False)
    embed_stats.set_field_at(index=3,name="Holders :gem:",value=(f"{strip.holders}"),inline=False)
    await ctx.send(embed=embed_stats)
 

embed_nft = embed.nfts()  
@bot.command(name="nft")
async def nfts(ctx): 
    print (f"NFT command by ~{ctx.author.name}")
    await ctx.send(embed=embed_nft)


@tasks.loop(minutes = 2)
async def update():
        await strip.dynamic_data()
        print ("Updated data ✅")


BOT_TOKEN = os.environ.get("DISCORD_KEY")
bot.run(BOT_TOKEN)
