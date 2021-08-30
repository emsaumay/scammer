from discord.ext import commands
import discord
import requests as r


class History(commands.Cog):

  def __init__(self, client):
      self.client = client

  @commands.command(aliases=['1h'])
  async def _1h(self, ctx, *, coin):
    try:
      response = r.get(f"https://api.coingecko.com/api/v3/coins/{coin}?localization=false&tickers=false&community_data=false&developer_data=false&sparkline=false").json()
      change = round(response['market_data']['price_change_percentage_1h_in_currency']['usd'], 2)
      data = f"{change}%"
      await ctx.send(data)
    except:
        url = "https://media.tenor.com/images/1c77bac5a51111ade38d81de5250e563/tenor.gif"
        return url


  @commands.command(aliases=['1d'])
  async def _1d(self, ctx, *, coin):
    try:
      response = r.get(f"https://api.coingecko.com/api/v3/coins/{coin}?localization=false&tickers=false&community_data=false&developer_data=false&sparkline=false").json()
      change = round(response['market_data']['price_change_percentage_24h_in_currency']['usd'], 2)
      data = f"{change}%"
      await ctx.send(data)
    except:
        url = "https://media.tenor.com/images/1c77bac5a51111ade38d81de5250e563/tenor.gif"
        return url


  @commands.command(aliases=['7d'])
  async def _7d(self, ctx, *, coin):
    try:
      response = r.get(f"https://api.coingecko.com/api/v3/coins/{coin}?localization=false&tickers=false&community_data=false&developer_data=false&sparkline=false").json()
      change = round(response['market_data']['price_change_percentage_7d_in_currency']['usd'], 2)
      data = f"{change}%"
      await ctx.send(data)
    except:
        url = "https://media.tenor.com/images/1c77bac5a51111ade38d81de5250e563/tenor.gif"
        return url


  @commands.command(aliases=['1y'])
  async def _1y(self, ctx, *, coin):
    try:
      response = r.get(f"https://api.coingecko.com/api/v3/coins/{coin}?localization=false&tickers=false&community_data=false&developer_data=false&sparkline=false").json()
      change = round(response['market_data']['price_change_percentage_1y_in_currency']['usd'], 2)
      data = f"{change}%"
      await ctx.send(data)
    except:
        url = "https://media.tenor.com/images/1c77bac5a51111ade38d81de5250e563/tenor.gif"
        return url

def setup(client):
    client.add_cog(History(client))