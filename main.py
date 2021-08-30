from discord.ext import commands, tasks
import discord
import os

client = commands.Bot(command_prefix='.')
TOKEN = os.environ['DISCORD_TOKEN']

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="your gurl in bed beside me."))

  print('We have logged in as {0.user}'.format(client))

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


@client.command(aliases=['p'])
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(TOKEN)