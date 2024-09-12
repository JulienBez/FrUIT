import glob
import time
from src.sort import *
from src.metadata import *
from src.getTweets import *
from src.manageFile import *
from src.filterBySeeds import *
from src.filterByTweets import *

def proceed(args):

  start = time.time()

  if args.getTweets:
    getTweets()

  if args.sort:
    sort()

  if args.filterByTweets:
    filterByTweets()

  if args.filterBySeeds:
    filterBySeeds()

  if args.metadata:
    metadata()

  end = time.time()
  print(f"executed in {round(end - start,2)}")


if __name__ == "__main__":
	
  import argparse
  parser = argparse.ArgumentParser()

  parser.add_argument("-g", "--getTweets", action="store_true", help="Get all tweets content and metadata from Twitter.")
  parser.add_argument("-s", "--sort", action="store_true", help="Sort tweets according to their seeds.")
  parser.add_argument("-ft", "--filterByTweets", action="store_true", help="Apply tweets-based filters on tweets.")
  parser.add_argument("-fs", "--filterBySeeds", action="store_true", help="Apply seeds-based filters on tweets.")
  parser.add_argument("-m", "--metadata", action="store_true", help="Get some metadatas.")

  parser.add_argument("--all", action="store_true", help="Execute all at once.")

  args = parser.parse_args()
  proceed(args)
