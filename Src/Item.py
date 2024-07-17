class Item:
  def __init__(self, itemID=44105, name="Tacos Al Pastor", craft_amount=1, hq=False, home_server="Moogle",  job=0):

    self.cristalData = [
      "Wind Shard","Wind Crystal", "Wind Cluster",
      "Fire Shard", "Fire Crystal", "Fire Cluster",
      "Ice Shard","Ice Crystal","Ice Cluster", 
      "Earth Shard", "Earth Crystal", "Earth Cluster",
      "Lightning Shard","Lightning Crystal","Lightning Cluster",
      "Water Shard","Water Crystal","Water Cluster",
      ]

    self.details = {
      "home_server": home_server,
      "shopping_list": [
        {
          "itemID": itemID,
          "name": name,
          "craft_amount": craft_amount,
          "hq": hq,
          "job": job
        }
      ],
      "region_wide": True
      }
    