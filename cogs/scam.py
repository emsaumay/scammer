from discord.ext import commands
import discord
import requests as r


class Scam(commands.Cog):

  def __init__(self, client):
      self.client = client

  @commands.command(aliases=['s'])
  async def scam(self, ctx, *, coin):
    try:
      response = getLatestPrice(coin)
      await ctx.send(response)
    except:
        url = "https://media.tenor.com/images/1c77bac5a51111ade38d81de5250e563/tenor.gif"
        return url

def setup(client):
    client.add_cog(Scam(client))


def getLatestPrice(coin, currency='usdt'):
    try:
        url = f"https://x.wazirx.com/api/v2/tickers/{coin.lower()}{currency.lower()}"
        response = r.get(url).json()
        LastPrice = response['ticker']['last']
        ReturnText = f"{coin.upper()} - {LastPrice} {currency.upper()}"
        return ReturnText
    except:
        url = "https://media.tenor.com/images/1c77bac5a51111ade38d81de5250e563/tenor.gif"
        return url