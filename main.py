import os
import discord
import efclasses
import efconfig
import efdatabase
import effunctions
import efloader

cmdp = efconfig.cmd_prefix
client = efconfig.client


@client.event #When logging in
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  await efloader.loadChannelsDic()
  await efloader.loadRolesDic()

#When seeing a new message
@client.event #When reading for commands
async def on_message(message):
  
  #Do not respond to self messages
  if message.author == client.user:
    return

  
  for command in effunctions.ef_cmd_dic:
    for commandAlias in command:
      #print("Checking against " + commandAlias)
      if message.content[0:len(cmdp+commandAlias)] == (cmdp + commandAlias):
        await effunctions.ef_cmd_dic[command](message)
        return



TOKEN = os.environ['bot_token']
client.run(TOKEN)