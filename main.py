import discord
import os
import re

client = discord.Client()
#numbers = re.compile(r'^([\s\d]+)$');

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    

  
  messageIn = message.content
  messageIn = messageIn.replace(" ","")
  if re.search(r"\([0-9]+,[0-9]+\)", messageIn):
      finalMessage = ("Looks like you are talking about cordinates on r/Place! Allow me to link them! https://www.reddit.com/r/place/?cx="+messageIn[messageIn.find('(') + 1:messageIn.find(',')]+"&cy="+messageIn[messageIn.find(',') +1:messageIn.find(')')]+"&px=10")
      await message.channel.send(finalMessage)
  return

client.run(os.getenv("apikey"))