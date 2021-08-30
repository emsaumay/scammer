from discord.ext import commands
import discord
import requests as r
import random


class Custom(commands.Cog):

  def __init__(self, client):
      self.client = client
  
  @commands.command(aliases=['pp'])
  async def ayush(self, ctx):
    
    coins = ['link', 'dot', 'btc', 'eth', 'matic', 'vet', 'waves', 'ltc', 'etc', 'bch', 'xrp', 'Band', 'atom']

    res = r.get('https://x.wazirx.com/api/v2/tickers').json()

    for name, value in res.items():
      for coin in coins:
        coin = f"{coin}usdt"
        if name == coin:
          coin_name = coin.upper()
          await ctx.send(f"{coin_name} - {value['last']} USDT")


  @commands.command()
  async def aryan(self, ctx):
    msgs = [
      'https://tenor.com/view/britney-spears-wink-toxic-sexy-britney-winking-gif-12117809',
      'https://tenor.com/view/toxic-in-chat-mda-toxic-mda-gif-20220000',
      'https://tenor.com/view/gay-pride-gif-7223984',
      'https://tenor.com/view/baby-face-palm-really-sigh-stupid-gif-12738431',
      'https://tenor.com/view/ethan-discord-mod-mods-discord-mods-discord-gif-18698937',
      'https://tenor.com/view/pissed-monkey-angry-ignoring-gif-9452975',
      'https://tenor.com/view/go-away-bye-ignored-no-gif-5264896',
      
      ]
    await ctx.send(random.choice(msgs))


  @commands.command(aliases=['v'])
  async def valo(self, ctx):
    gif = 'https://tenor.com/view/heisen-valorant-liam-thomas-gif-18947441'
    await ctx.send(f'<@&801032309771075615> {gif}')


def setup(client):
    client.add_cog(Custom(client))