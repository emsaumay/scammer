from discord.ext import commands
import discord
import requests as r


class Stats(commands.Cog):

  def __init__(self, client):
      self.client = client

  @commands.command(aliases=["cg"])
  async def stats(self, ctx, *, coin):
    try:

      response = r.get(f"https://api.coingecko.com/api/v3/coins/{coin}?localization=false&tickers=false&community_data=false&developer_data=false&sparkline=false").json()


      name = response['name']
      image = response['image']['small']
      current_price_in_usd = response['market_data']['current_price']['usd']
      current_price_in_inr = response['market_data']['current_price']['inr']
      all_time_high_in_usd = response['market_data']['ath']['usd']
      all_time_high_in_inr = response['market_data']['ath']['inr']
      ath_change_percentage = round(response['market_data']['ath_change_percentage']['usd'], 2)
      market_cap_in_usd = response['market_data']['market_cap']['usd']
      market_cap_in_inr = response['market_data']['market_cap']['inr']
      market_cap_rank = response['market_data']['market_cap_rank']
      high_24h_in_usd = response['market_data']['high_24h']['usd']
      high_24h_in_inr = response['market_data']['high_24h']['inr']
      low_24h_in_usd = response['market_data']['low_24h']['usd']
      low_24h_in_inr = response['market_data']['low_24h']['inr']

      
      embedVar=discord.Embed(title="Stats", url="https://saumay.dev", description=f"{name}", color=0x4eba26)
      embedVar.set_thumbnail(url=f"{image}")
      embedVar.add_field(name="Current Price", value=f"${current_price_in_usd}", inline=False)
      embedVar.add_field(name="Market Cap Rank", value=f"{market_cap_rank}", inline=False)
      embedVar.add_field(name="24h High", value=f"${high_24h_in_usd}", inline=True)
      embedVar.add_field(name="24h Low", value=f"${low_24h_in_usd}", inline=True)
      embedVar.add_field(name="ATH Price", value=f"${all_time_high_in_usd}", inline=False)
      embedVar.add_field(name="ATH % Change", value=f"{ath_change_percentage}%", inline=False)
      # embedVar.add_field(name="Market Cap", value=f"${market_cap_in_usd}", inline=True)
      
      
      await ctx.send(embed=embedVar)
    except:
      url = "https://media.tenor.com/images/1c77bac5a51111ade38d81de5250e563/tenor.gif"
      return url


def setup(client):
    client.add_cog(Stats(client))