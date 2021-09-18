import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
      if message.content.startswith('Poll activated - Topic:'):
        emojis = ['👍', '👎']
        for emoji in emojis:
          await message.add_reaction(emoji)

    elif message.content.startswith('poll'):
      member = message.author
      print (member)
      poll = message.content[4: ]
      await message.channel.send("Poll activated - Topic: " + poll)

client.run(os.getenv('TOKEN'))
