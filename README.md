# FrUIT

Here, we introduce the FrUIT corpus (French Unfrozen Idioms in Tweets). This corpus was created to contribute to the research on multiword expressions (hereafter MWEs) and puns in multiwords expressions (PMWEs). We used a list of 217 MWEs to fetch tweets from Twitter daily for a period of over 3 years (october 2020 - february 2023). Therefore, each tweet is linked to the MWE that led to its extraction and each tweet is more or less likely to contain a MWE or a PMWE in it. In total, and after numerous filtering steps, 60,617 tweets and 77 MWEs remains.

## How to collect

As we are not authorised to distribute tweets as they are (see [here](https://www.ucl.ac.uk/data-protection/sites/data-protection/files/using-twitter-research-v1.0.pdf) for instance), we only share their ids along with the MWE that was used to fetch them. You can see those informations in **data/tweets_ids.json**.

First, run this command to install all the prerequisites:

```
pip install -r requirements.txt
```

To fetch the tweets of the FrUIT corpus from Twitter and put them in **data/tweets**, run the following command:

```
python main.py --getTweets
```

Then, you can sort each tweet according to its seed in **output** with the following:

```
python main.py --sort
```

To reproduce the same filtering steps as us, run those two commands:

```
python main.py --filterByTweets
python main.py --filterBySeeds
```

To parse the tweets the same way we did, run this command:

```
python main.py --parse
```

Finally, for some metadata, run:

```
python main.py --metadata
```

To run evetything at the same time, you can use:

```
python main.py --all
```