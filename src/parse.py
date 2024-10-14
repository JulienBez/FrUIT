import re
import string as strii

import spacy
sp = spacy.load("fr_dep_news_trf") #fr_core_news_md

from .utils import *

def removePunct(string):
    """map punctuation to space, not used as for now"""
    return string.translate(str.maketrans(strii.punctuation, ' '*len(strii.punctuation)))


def spacePunct(string):
    """add spaces before and after punctuation to ease later treatments"""
    return string.translate(str.maketrans({key: " {0} ".format(key) for key in strii.punctuation}))


def repBadChar(string):
    """replace problematic characters / punctuation with space"""
    bad_char = ["'","’","-","\n","\r",";"]
    for bc in bad_char:
        string = string.replace(bc," ")
    return re.sub(' +', ' ', string)


def noEmpty(word):
    """check if a tag is empty or not"""
    return word if word else "_"


def tokenizer(spacy_object):
    """tokenize everything in a given spacy object"""
    return [noEmpty(word.text) for word in spacy_object]

    
def posTagger(spacy_object):
    """POS tag everything in a given spacy object"""
    return [noEmpty(word.pos_) for word in spacy_object]


def lemmatizer(spacy_object):
    """lemmatize everything in a given spacy object"""
    return [noEmpty(word.lemma_) for word in spacy_object]


def dependencies(spacy_object):
    """return list of dependancies ids for each token"""
    return [str(word.head) for word in spacy_object]


def myParser(text):
    """transform text into spacy object and tokenize it - for pre-alignment"""
    text_sp = [i for i in sp(spacePunct(repBadChar(text).lower())) if i.pos_ != "SPACE"]
    return {"TOK":tokenizer(text_sp),"LEM":lemmatizer(text_sp),"POS":posTagger(text_sp),"DEP":dependencies(text_sp)}


def parseSeeds():
    """create a log file with every seed and its NLP treatment if not exists"""
    seeds = openJson("logs/seeds.json")
    for seed,value in seeds.items(): 
        seeds[seed] = {**value,**myParser(seed)}
    writeJson("logs/seeds.json",seeds)


def parseTweets():
    """for each tweet do NLP treatment on it"""
    for path in tqdm(glob.glob("output/*.json")):
        data = openJson(path)
        for entry in data:
            tweet = entry["sent"]
            entry["parsing"] = myParser(tweet)
        writeJson(path,data)