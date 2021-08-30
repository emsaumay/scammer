from discord.ext import commands
import discord
import requests as r
from pymongo import MongoClient
import datetime


cluster = MongoClient(os.environ['DATABASE_URI'])

db = cluster["TestData"]
collection = db["UserData"]
PortfolioDB = db["Portfolio"]

class Portfolio(commands.Cog):

  def __init__(self, client):
      self.client = client

  @commands.command()
  async def initiate(self, ctx):

    myquery = { "_id": ctx.author.id }

    if (collection.count_documents(myquery) == 0):
      post = {
        "_id": ctx.author.id, 
        "FundsIssued": 1000, 
        "FundsLeft": 1000,
        "TotalTrades": 0,
        "Account Created": datetime.datetime.now(),
        "LastUpdated": datetime.datetime.now(),
         }

      collection.insert_one(post)

      embedVar=discord.Embed(title=f"✅ Account Created Successfully.", color=0x4eba26)
      embedVar.add_field(name="Funds Issued", value=f"${post['FundsIssued']}", inline=False)

      portfolio_data = {
        "_id": ctx.author.id,
      }
      PortfolioDB.insert_one(portfolio_data)

      await ctx.send(embed=embedVar)

    else:
      await ctx.send("Account Already Exists.")

  @commands.command()
  async def portfolio(self, ctx):
    myquery = { "_id": ctx.author.id }
    data = collection.find_one(myquery)

    embedVar=discord.Embed(title=f"Portfolio", color=0x4eba26)
    embedVar.add_field(name="User", value=f"{ctx.author.mention}", inline=False)
    embedVar.add_field(name="Funds Available", value=f"${data['FundsLeft']}", inline=False)
    embedVar.add_field(name="Funds Issued", value=f"${data['FundsIssued']}", inline=False)
    embedVar.add_field(name="Total Trades", value=f"{data['TotalTrades']}", inline=False)

    await ctx.send(embed=embedVar)

  
def setup(client):
    client.add_cog(Portfolio(client))