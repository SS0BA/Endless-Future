#Things that were once useful

'''
#Format all stored gameplay channel names the same
async def fixChannelNamesDB():
  print("[")
  for channel in gameplayChannels:
    fixedName = channel.replace(" ", "-")
    print("\"" + fixedName.lower() + "\",")
  print("]")


#Format all role names the same
async def fixRoleNames():
  print("Starting fixrolenames")
  for singleServer in efconfig.client.guilds:
    print("Checking " + singleServer.name)
    if (singleServer.name == "ENDLESS FUTURE"):
      for roleName in gameplayChannels:
          await singleServer.create_role(name=roleName)
          print(roleName)
  return

#Restrict gameplay channels to only people who have the role
async def restrictChannels():
  print("Starting restrictchannels")
  for singleServer in efconfig.client.guilds:
    print("Checking " + singleServer.name)
    if (singleServer.name == "ENDLESS FUTURE"):
      for singleChannel in singleServer.channels:
        for singleRole in singleServer.roles:
          if (singleRole.name == singleChannel.name):
            await singleChannel.set_permissions(singleServer.default_role, read_messages=False)
            await singleChannel.set_permissions(singleRole, read_messages=True)
            print("Allowed " + singleRole.name + " to view " + singleChannel.name)
  return

#Give everyone a database entry
async def generatePlayerDatabase():
  for singleServer in efconfig.client.guilds:
    if (singleServer.name == "ENDLESS FUTURE"):
      print(len(singleServer.members))
      for singlePlayer in singleServer.members:
        print(singlePlayer.name)
        query = Query()
        if efdatabase.ef_players.search(query.id == singlePlayer.id):
          print("User already exists")
        else:
          efdatabase.createEntry(efclasses.EFplayer(userid=singlePlayer.id, name=singlePlayer.name))
          await singlePlayer.add_roles(discord.utils.get(singleServer.roles, name="aether-beach"))
          print("User made")
  print("Finished")
  return
'''