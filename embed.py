import discord
from discord.ext import commands

# Initialize the bot
intents = discord.Intents.default()

def stats(): 
    embed_stats = discord.Embed(title='StripperCoin Stats',color=0xBF40BF )
    embed_stats.add_field(name='Current Price :dollar:', value="", inline=False)
    embed_stats.add_field(name='Price in Ada <:cardano:1131689885124796416>', value="", inline=False)
    embed_stats.add_field(name="Market Cap :moneybag:",value="", inline=False)
    embed_stats.add_field(name="Holders :gem:",value="",inline=False)
    
    embed_stats.set_footer(text='Powered by @tonyler', icon_url='https://pbs.twimg.com/profile_images/1698204398663372800/5qeTwmIS_400x400.jpg')
    return embed_stats

def nfts(): 
    embed_nft = discord.Embed(title="StripperCoin's NFTs",color=0xBF40BF,
                        description="[Box Girls](<https://www.jpg.store/collection/strippercoinboxgirls>) <:strip:1135350102349860937> \
                        \n[Casey NFTease](<https://www.jpg.store/collection/strippercoinnftease-caseycastille?tab=items>) <:exxx:1135350359364227204>"\
                        "\n[Emiline NFTease](<https://www.jpg.store/collection/strippercoinnftease-emiline>) <:exxx:1135350359364227204>")
    embed_nft.set_footer(text='Powered by @tonyler', icon_url='https://pbs.twimg.com/profile_images/1698204398663372800/5qeTwmIS_400x400.jpg')
    return embed_nft