import os
from .manageFile import *

def loadFilters():
  createFolder("logs")
  "simple function to create a filter metadata file if not exists"
  if not isFile("logs/filters.json"):
    filters = {}
  else:
    filters = openJson("logs/filters.json")
  return filters


def initialNumbers():
  "get initial values for each seeds"
  filters = loadFilters()
  filters["initialNumbers"] = {}
  for path in glob.glob("output/*.json"):
    data = openJson(path)
    filters["initialNumbers"][data[0]["parenté"]["seed"]] = len(data)
  writeJson("logs/filters.json",filters)


def deleteIdsDuplicates():
  "delete duplicates inside all output/*.json file"

  filters = loadFilters()
  filters["deleteDuplicates"] = {}

  for path in glob.glob("output/*.json"):

    data = openJson(path)
    seed = data[0]["parenté"]["seed"]
    filters["deleteDuplicates"][seed] = 0

    seedsCheck = []
    new_data = []

    for entry in data:
      
      tweet_id = entry["metadata"]["id"]

      if tweet_id not in seedsCheck:
        seedsCheck.append(tweet_id)
        new_data.append(entry)

      else:
        filters["deleteDuplicates"][seed] += 1  

    writeJson(path,new_data)
  writeJson("logs/filters.json",filters)


def deleteContentDuplicates():
  "delete tweets with the same content"

  filters = loadFilters()
  filters["deleteContentDuplicates"] = {}

  for path in glob.glob("output/*.json"):

    data = openJson(path)
    seed = data[0]["parenté"]["seed"]
    filters["deleteContentDuplicates"][seed] = 0

    tweetCheck = []
    new_data = []

    for entry in data:
      
      tweet = entry["tweet"]

      if tweet not in tweetCheck:
        tweetCheck.append(tweet)
        new_data.append(entry)

      else:
        filters["deleteContentDuplicates"][seed] += 1

    writeJson(path,new_data)
  writeJson("logs/filters.json",filters)


def deleteDuplicatesMore():
  "delete remaining duplicates that are in different .json files"

  filters = loadFilters()
  filters["deleteDuplicatesMore"] = {}

  doublons = []
  seeds = []

  for path in glob.glob("output/*.json"):

    data = openJson(path)
    seed = data[0]["parenté"]["seed"]

    if seed not in filters["deleteDuplicatesMore"]:
      filters["deleteDuplicatesMore"][seed] = 0

    for entry in data:
      
      tweet_id = entry["metadata"]["id"] 
      
      if tweet_id not in seeds:
        seeds.append(tweet_id)

      else:
        db = [tweet_id,path]
        doublons.append(db)
        filters["deleteDuplicatesMore"][seed] += 1

  doublons_set = [list(d) for d in set(tuple(row) for row in doublons)]
  for d in doublons_set:
    data = openJson(d[1])

    for i,entry in enumerate(data):
      if entry["metadata"]["id"] == d[0]:
        del data[i]

    writeJson(d[1],data)
  writeJson("logs/filters.json",filters)


def filterLowest(size=10):
  "filter seeds with a number of tweets inferior to indicated size"
  filters = loadFilters()
  filters["filterLowest"] = {"kept":{},"filtered":{}}
  for path in glob.glob("output/*.json"):
    data = openJson(path)
    if len(data) < size:
      filters["filterLowest"]["filtered"][data[0]["parenté"]["seed"]] = len(data)
      os.remove(path)
    else:
      filters["filterLowest"]["kept"][data[0]["parenté"]["seed"]] = len(data)
  writeJson("logs/filters.json",filters)


def filterByTweets():
  ""
  initialNumbers()
  deleteIdsDuplicates()
  deleteContentDuplicates()
  deleteDuplicatesMore()
  filterLowest()
