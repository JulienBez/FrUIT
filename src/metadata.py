import matplotlib.pyplot as plt
from .utils import *

def totalTweets():
    ""
    total = 0
    for path in glob.glob("output/*.json"):
        data = openJson(path)
        total += len(data)
    print(f"nombre total de tweets : {total}")


def totalSeeds():
    ""
    total =  len([path for path in glob.glob("output/*.json")])
    print(f"nombre total de seeds : {total}")


def medianTweetPerSeed():
    ""
    counter = []
    for path in glob.glob("output/*.json"):
        total = len(openJson(path))
        counter.append(total)
    counter = sorted(counter)
    x = int(len(counter)/2) + (len(counter) % 2 > 0)
    print(f"médiane de tweets par seed : {counter[x]}")


def minMaxTweets():
    ""
    counter = []
    for path in glob.glob("output/*.json"):
        total = len(openJson(path))
        counter.append(total)
    counter = sorted(counter)
    print(f"nb min de tweets pour une seed : {counter[0]}")
    print(f"nb max de tweets pour une seed : {counter[-1]}")


def getWordNumber():
    ""
    counter = 0
    for path in glob.glob("output/*.json"):
        tweets =  openJson(path)
        for tweet in tweets:
            total = len(tweet["sent"].split())
            counter += total
    print(f"nombre de mots : {counter}")


def getGraph(logscale=False):
    ""

    counter = []
    for path in glob.glob("output/*.json"):
        total = len(openJson(path))
        counter.append(total)
    counter = sorted(counter,reverse=True)

    width = 0.5
    fig, ax = plt.subplots()

    ax.bar([i for i in range(len(counter))], counter, label="tweets", width=width, color='blue')

    path = 'logs/metadata.png'
    if logscale:
        ax.set_yscale('log')
        path = 'logs/metadata_logscale.png'
        plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{int(y)}'))

    ax.legend()
    plt.tight_layout()
    plt.savefig(path,dpi=1000,bbox_inches='tight')
    plt.close()


def filteringStepsMetadata():
    ""
    data = openJson("logs/filters.json")
    total_inital = sum([v for k,v in data["initialNumbers"].items()])
    total_duplicates = sum([ 
        sum([v for k,v in data["deleteDuplicates"].items()]) , 
        sum([v for k,v in data["deleteContentDuplicates"].items()]) , 
        sum([v for k,v in data["deleteDuplicatesMore"].items()]) 
        ])
    total_seedsFiltered = sum([v for k,v in data["filterLowest"]["filtered"].items()])
    print(f"nb tweets avant filtres : {total_inital}")
    print(f"nb tweets après filtre duplicats : {total_duplicates}")
    print(f"nb tweets après filtre par seeds : {total_seedsFiltered}")


def metadata():
    ""
    totalSeeds()
    totalTweets()
    medianTweetPerSeed()
    getWordNumber()
    getGraph()
    getGraph(logscale=True)
    filteringStepsMetadata()