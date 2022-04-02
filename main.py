import discord
import os
import re

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    

  
  messageIn = message.content #imports message
  messageIn = messageIn.replace(" ","") #removes spaces
  if re.search(r"\([0-9]+,[0-9]+\)", messageIn): #checks if message matches format
      match = re.search(r"\([0-9]+,[0-9]+\)", messageIn)
      messageIn = messageIn[messageIn.find(match.group()):]  
      finalMessage = ("Looks like you are talking about coordinates on r/Place! Allow me to link them! https://www.reddit.com/r/place/?cx="+messageIn[messageIn.find('(') + 1:messageIn.find(',')]+"&cy="+messageIn[messageIn.find(',') +1:messageIn.find(')')]+"&px=10") #Generates message
      await message.channel.send(finalMessage) #sends message
  return

client.run(os.getenv("apikey"))