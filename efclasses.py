import discord 
import efconfig
import efdatabase
from tinydb import Query

ef_players = efdatabase.ef_players
#EFitems = efdatabase.EFitems

class EFplayer:
	# setup default values
  def __init__(
    self,
    userid = 0,
    name = "PLACEHOLDER",
    location = "aether-beach",
    Faction = 
    Health =
    Cache = 0/100000000,
    aether = 0
  ):
    
    # Check for and possibly load saved data
    SavedData = efdatabase.getPlayerData(userid)
    if SavedData:
      self.userid = userid
      self.name = SavedData["name"]
      self.location = SavedData["location"]
      self.slime = SavedData["slime"]
      self.new = False
    # Or initialize from given values
    else:
      self.userid = userid
      self.name = name
      self.location = location
      self.slime = slime
      self.new = True