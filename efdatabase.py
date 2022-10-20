from tinydb import TinyDB, where
from tinydb.operations import increment, subtract, add, set

#Contains: Database functions

ef_players = TinyDB("./database/ef_players.json")



'''
	Retrieves a single passed attribute for a particular player
'''
def getPlayerAttribute(userid, attr):
  data = ef_players.search(where('id') == userid)
  if len(data) == 1:
	  return(data[0][attr])
  else:
    print("Failed to retrieve {} for player {}".format(attr, str(userid)))
    return False


'''
	Changes the attribute in the database for a particular player
'''
def setPlayerAttribute(userid, attr, value):
	try:
		ef_players.update(set(attr, value), where('id') == userid)
		return True
	except:
		print("Failed to set {} to {} for player {}".format(attr, str(value), str(userid)))
		return False


'''
	Creates a new "Row" in the database for a passed 
	GCUser class. Careful. Don't wanna give someone 
	multiple entries.
'''
def createEntry(gcuser):
	ef_players.insert({'id': gcuser.userid,
            'name': gcuser.name, #Discord users can change their names so never rely on this. It's only to make the database readable.
					  'location': gcuser.location,
            'slime':gcuser.slime})

'''
	Returns the dictionary of a player's stored data,
	if there are multiple or no entries, it returns 
	false.
'''
def getPlayerData(userid):
	data = ef_players.search(where('id') == userid)
	if len(data) == 1:
		return (data[0])
	else:
		return False


'''
Removes specified row from player db
'''
def deletePlayer(userid):
	deleted_ids = ef_players.remove(where("id") == userid)
	if len(deleted_ids) < 1:
		print("Failed to remove player with id {}".format(str(userid)))
	elif len(deleted_ids) > 1:
		print("Removed {} player with id {}".format(str(len(deleted_ids)), str(userid)))
