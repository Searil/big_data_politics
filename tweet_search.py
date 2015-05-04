# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from TwitterSearch import *
import datetime

# <codecell>

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['mhp', 'akp', 'chp']) # let's define all words we would like to have a look for
    tso.set_language('tr') # we want to see German tweets only
    #tso.set_until(datetime.date(2015, 4, 20))
    #tso.set_include_entities(False) # and don't give us all those entity information
    ts = TwitterSearch(
        consumer_key = 'mEnkTsYmvFGgzjV73SPOz084K',
        consumer_secret = 'YnQxTyFhTCG5KSGBeRq1qeVwUkxOhZ99amm6uauy8ett51UE3t',
        access_token = '301689344-MG8rknSLPC8dUXAjWE6Eo4DQTeS4JJGjNuTJ6i41',
        access_token_secret = 'vcjYSSekdT0O8qwMVhh9e6flVC1LaP5OlssIsU4nGWewh'
     )
        
        
except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)

# <codecell>

try:
    id = 0
    for tweet in ts.search_tweets_iterable(tso):
        id = id + 1
        print id, tweet['created_at'], "cordinates: ", tweet['coordinates'], tweet['text'],"geo:", tweet['geo'],"user location:" ,tweet['user']['location']
except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)

# <codecell>


# <codecell>


