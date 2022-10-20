import discord
import efconfig


#Contains: Loading functions


allServersChannelDic = {}
async def loadChannelsDic():
  for singleServer in efconfig.client.guilds:
    allServersChannelDic[singleServer.name] = {}
    print("Loading channels from " + singleServer.name)
    for singleChannel in singleServer.channels:
      allServersChannelDic[singleServer.name][singleChannel.name] = singleChannel
    #print(allServersChannelDic)
    return

allServersRoleDic = {}
async def loadRolesDic():
  for singleServer in efconfig.client.guilds:
    allServersRoleDic[singleServer.name] = {}
    print("Loading roles from " + singleServer.name)
    for singleRole in singleServer.roles:
      modifiedRoleName = singleRole.name.casefold()
      modifiedRoleName = modifiedRoleName.replace(" ", "-")
      allServersRoleDic[singleServer.name][modifiedRoleName] = singleRole
    #print(allServersRolesDic)
    return
