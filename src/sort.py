from .manageFile import *

def extractBySeeds(path,dict_seeds):
  "create a dic with seeds as keys and tweets+metadata as values"
  data = openJson(path)
  for entry in data:
    seed = entry["parenté"]["seed"]
    if seed not in dict_seeds:
      dict_seeds[seed] = []
    dict_seeds[seed].append(entry)
  return dict_seeds


def saveBySeeds(dict_seeds):
  "create a json file for each key (i.e. seeds) in extractSeed's dic"
  createFolder("output/")
  for key, value in dict_seeds.items():
    new_data_path = "output/" + "".join(x for x in key.replace(" ","_") if x.isalnum() or x == "_") + ".json"
    writeJson(new_data_path,value)


def sort():
    ""
    dict_seeds = {}
    for path in tqdm(glob.glob("data/tweets/*.json")):
        dict_seeds = extractBySeeds(path,dict_seeds)
    saveBySeeds(dict_seeds)