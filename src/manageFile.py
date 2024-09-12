import os
import json
import glob
import shutil
from tqdm import tqdm

def openJson(path):
  "open a json file"
  with open(path,'r',encoding='utf-8') as f:
    data = json.load(f)
  return data
  

def writeJson(path,data):
  "create a json file"
  with open(path,"w",encoding='utf-8') as f:
    json.dump(data,f,indent=4,ensure_ascii=False)


def createFolder(path):
  "create an empty folder"
  if not os.path.exists(path):
      os.mkdir(path)


def isFile(path):
  "check if a file exists"
  return os.path.isfile(path)