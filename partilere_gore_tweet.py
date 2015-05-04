# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# -*- coding: utf-8 -*-
#!/usr/bin/python
import tweepy
import pandas as pd
import matplotlib.pyplot as plt
import csv
import time 

pd.options.display.max_columns = 50
pd.options.display.max_rows= 50
pd.options.display.width= 120

auth = tweepy.auth.OAuthHandler('mEnkTsYmvFGgzjV73SPOz084K', 'YnQxTyFhTCG5KSGBeRq1qeVwUkxOhZ99amm6uauy8ett51UE3t')
auth.set_access_token('301689344-MG8rknSLPC8dUXAjWE6Eo4DQTeS4JJGjNuTJ6i41', 'vcjYSSekdT0O8qwMVhh9e6flVC1LaP5OlssIsU4nGWewh')
api = tweepy.API(auth)

# <codecell>

partiler = {}
partiler["akp"] = 0
partiler["chp"] = 0
partiler["mhp"] = 0
partiler["bdp"] = 0 
counter = 0
general_counter = 0
try:  
    for tweet in tweepy.Cursor(api.search, q="akp OR chp OR mhp OR bdp OR hdp",lang="tr", since="2015-03-19", until="2015-03-20").items(999999999):
        counter = counter + 1
        twit = tweet.text
        if '\n' in twit:
            twit = twit.replace('\n', ' ')
            twit = twit.replace('\t', ' ')
            twit = twit.replace('"', ' ')
        print counter, "--", tweet.id, tweet.created_at, twit.encode('utf-8')
        if ("AKP" or "akp") in tweet.text:
            partiler["akp"] = partiler["akp"] + 1
        if ("CHP" or "chp") in tweet.text:
            partiler["chp"] = partiler["chp"] + 1
        if ("MHP" or "mhp") in tweet.text:
            partiler["mhp"] = partiler["mhp"] + 1 
        if ("BDP" or "bdp") in tweet.text:
            partiler["bdp"] = partiler["bdp"] + 1
        if ("HDP" or "hdp") in tweet.text:
            partiler["bdp"] = partiler["bdp"] + 1 
        with open('tweets.csv', 'a') as csvfile:
            fieldnames = ['id', 'date', 'tweet','coordinates','user_location']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)    
            writer.writerow({'id': tweet.id, 'date': tweet.created_at, 'tweet': twit.encode('utf-8'), 'coordinates': tweet.coordinates, 'user_location': tweet.author.location.encode('utf-8') })
        if counter == 15:
            time.sleep(5)
            counter = 0
            general_counter = general_counter + 1
        if general_counter == 20:
            time.sleep(60)
            general_counter = 0
except BaseException, e:
    print 'failed ondata,', str(e)
    time.sleep(5) 

# <codecell>


