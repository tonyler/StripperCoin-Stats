import discord
from discord.ext import commands

# Initialize the bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def send_embed(ctx):
    # Create an embed object
    embed = discord.Embed(
        title="Embedded Message Title",
        description="This is the description of the embedded message.",
        color=discord.Color.blue()  # You can choose the color
    )

    # Add fields to the embed
    embed.add_field(name="Field 1", value="Value 1", inline=True)
    embed.add_field(name="Field 2", value="Value 2", inline=True)
    embed.add_field(name="Field 3", value="Value 3", inline=False)

    # Set the author of the embed
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

    # Set the timestamp of the embed (optional)
    embed.timestamp = ctx.message.created_at

    # Send the embed as a message
    await ctx.send(embed=embed)

# Run the bot
bot.run('YOUR_BOT_TOKEN')
