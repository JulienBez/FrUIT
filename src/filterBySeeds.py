import os
from .manageFile import *

def getPath(seed):
  ""
  return "output/"+"".join(x for x in seed.replace(" ","_") if x.isalnum() or x == "_")+".json"


def removeUnwantedSeeds():
  "check the annotated seeds file and apply filters to the dataset by deleting unwanted seeds"
  seeds = openJson("logs/seeds.json")
  for seed,values in seeds.items():
    path = getPath(seed)
    if values["kept"] == False and isFile(path):
      os.remove(path)


def correctSeeds():
  "check the annotated seeds file and apply filters to the dataset by correcting/modifying seeds"
  seeds = openJson("logs/seeds.json")
  for seed,values in seeds.items():     
    if values["correction"] != "NO":
      data = openJson(getPath(seed))
      for entry in data:
        entry["parenté"]["seed"] = values["correction"]
      new_path = "output/" + "".join(x for x in values["correction"].replace(" ","_") if x.isalnum() or x == "_") + ".json"
      os.remove(getPath(seed))
      writeJson(new_path,data)


def count():
  "count the number of seeds after our manual filters were applied"
  seeds = openJson("logs/seeds.json")
  kept = len([path for path in glob.glob("output/*.json")])
  notKept = len(seeds)-kept
  corrected = len([k for k,v in seeds.items() if v["correction"]!="NO"])
  print("kept seeds : ", kept)
  print("not kept seeds : ", notKept)
  print("corrected seeds : ",corrected)


def filterBySeeds():
  ""
  removeUnwantedSeeds()
  correctSeeds()
  count()