import efclasses
import efconfig
import efdatabase
import efloader
import discord
from tinydb import Query
import time

#Contains: Gameplay functions,  command dictionary

client = efconfig.client
gameplayChannels = efconfig.fullGameplayChannels
allServersChannelDic = efloader.allServersChannelDic
allServersRoleDic = efloader.allServersRoleDic
    

async def sendMessage(message, content):
  await message.channel.send(content)
  return

#For most gameplay commands, check that the player is in a gameplay channel
async def isInGameplayChannel(message):
  for validChannel in gameplayChannels:
    if message.channel.name == validChannel:
      return True
  await sendMessage(message, "You must be in a gameplay channel to do a gameplay command")
  return False

#Create new users
async def newUser(message):
  query = Query()
  if efdatabase.ef_players.search(query.id == message.author.id):
    await sendMessage(message, "User already exists")
    return
  efdatabase.createEntry(efclasses.EFplayer(userid=message.author.id))
  await sendMessage(message, "User made")
  return

#Clear the database
async def clearDatabase(message):
  efdatabase.ef_players.truncate()
  await sendMessage(message, "Database cleared")
  return

async def movePlayer(message):
  messageSplit = message.content.split(" ")
  if (await isInGameplayChannel(message)):
    if (message.channel.name == efdatabase.getPlayerAttribute(message.author.id, "location")):
      if(messageSplit[1] in gameplayChannels):
        moveTime = 1
        await sendMessage(message, "You start going to " + messageSplit[1] + " in " + str(moveTime) + " seconds.")
        time.sleep(moveTime)
        await message.author.remove_roles(allServersRoleDic[message.guild.name][efdatabase.getPlayerAttribute(message.author.id, "location")])
        await message.author.add_roles(allServersRoleDic[message.guild.name][messageSplit[1]])
        efdatabase.setPlayerAttribute(message.author.id, "location", messageSplit[1])
        
      else:
        await sendMessage(message, "That's not a channel you can move to.")
        return
    else:
      await sendMessage(message, "You are trying to move in a channel you are not located in.")
      return
  return

async def sendSpotifyPlaylists(message):
  SpotifyPlaylists = ["Noise Head Radio https://open.spotify.com/playlist/4Cj74lnnkMOxOysg8VZBXF?si=8e03f7f1591d499c", 
 "33.LT Cyber Shocker Radio https://open.spotify.com/playlist/45pOiWCd0IiOQ236RzIFpS? si=3bcc57043c5b47cf", 
 "D.34D 41R https://open.spotify.com/playlist/5PPCRIG5a4kJFNtIBQvvOg?si=1153471a28804dd6",
 "99.9 GT college radio https://open.spotify.com/playlist/6UsYmABbpIkN5jEsQ0wn6a?si=a3ee2ce407ed48c7",
 "Mandela Radio https://open.spotify.com/playlist/6aYRMQ0RRISh3wGcWsoPNs?si=0a04a65db7834dc1"
 "S.08 Classic Radio https://open.spotify.com/playlist/6IKpYDvV6ij2Tjjcu3X4x5?si=80225d590fc8417e"]

  for playlist in SpotifyPlaylists:
    await sendMessage(message, playlist)
  return

ef_cmd_dic = {
  ("newuser", "nu") : newUser,
  ("cleardatadase", "cdb") : clearDatabase,
  ("goto") : movePlayer,
  ("radio") : sendSpotifyPlaylists
}