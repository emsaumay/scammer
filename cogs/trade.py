from discord.ext import commands
import discord
import requests as r
from pymongo import MongoClient
import datetime
import os

api_url = "https://x.wazirx.com/api/v2/tickers/"
cluster = MongoClient(os.environ['DATABASE_URI'])

db = cluster["TestData"]
UserData = db["UserData"]
OrderHistory = db["OrderHistory"]
Portfolio = db["Portfolio"]

class Trade(commands.Cog):

  def __init__(self, client):
      self.client = client

  @commands.command()
  async def buy(self, ctx, coin, quantity):

    myquery = { "_id": ctx.author.id }
    user_data = UserData.find_one(myquery)
    portfolio_data = Portfolio.find_one(myquery)

    coin_data = r.get(api_url+coin.lower()+"usdt")

    if coin_data.status_code == 200:

      coin_data = coin_data.json()['ticker']
      OrderAmount = float(coin_data['last']) * float(quantity)
      FundsAvailable = float(user_data['FundsLeft'])

      if FundsAvailable >= OrderAmount:
        FundsLeft = FundsAvailable - OrderAmount
        TotalTrades = user_data['TotalTrades'] + 1
        orderData = {
          "userId": ctx.author.id,
          "userName": ctx.author.name,
          "coin": coin.upper(),
          "quantity": float(quantity),
          "AtPrice": coin_data['last'],
          "OrderAmount": OrderAmount,
          "FundsBefore": FundsAvailable,
          "FundsAfter": FundsLeft,
          "Timestamp": datetime.datetime.now(),
        }
        OrderHistory.insert_one(orderData)
        UserData.update(
          {"_id": ctx.author.id},
          {"$set":{
              "TotalTrades": TotalTrades,
              "FundsLeft": FundsLeft,
              "LastUpdated": datetime.datetime.now(),}})

        if str(portfolio_data[coin.upper()]) == int:
          new_quantity = portfolio_data[coin.upper()] + quantity
          coin = str(coin.upper())
          Portfolio.update(
            {"_id": ctx.author.id},
            {"$set": {
              coin: new_quantity,
            }})
        else:
          Portfolio.update(
            {"_id": ctx.author.id},
            {"$set": {
              str(coin.upper()): int(quantity)
            }})

        await ctx.send(f"Bought `{quantity} {coin.upper()}` for `${OrderAmount}`. Funds Left: `${FundsLeft}`")
      else:
        await ctx.send("Not Enough Funds.")

  # @commands.command()
  # async def sell(self, ctx, coin, quantity):

  

def setup(client):
    client.add_cog(Trade(client))