# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# -*- coding: utf-8 -*-
import tweepy
import pandas as pd
import matplotlib.pyplot as plt
import csv
import time 

pd.options.display.max_columns = 50
pd.options.display.max_rows= 50
pd.options.display.width= 120

ckey = 'mEnkTsYmvFGgzjV73SPOz084K'
csecret = 'YnQxTyFhTCG5KSGBeRq1qeVwUkxOhZ99amm6uauy8ett51UE3t'
atoken = '301689344-MG8rknSLPC8dUXAjWE6Eo4DQTeS4JJGjNuTJ6i41'
asecret = 'vcjYSSekdT0O8qwMVhh9e6flVC1LaP5OlssIsU4nGWewh'

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

# <codecell>

results = api.search(q="akp OR chp OR mhp OR bdp OR hdp", lang="tr")

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
        with open('names.csv', 'a') as csvfile:
            fieldnames = ['id', 'date', 'tweet','coordinates','user_location']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)    
            writer.writerow({'id': tweet.id, 'date': tweet.created_at, 'tweet': twit.encode('utf-8'), 'coordinates': tweet.coordinates, 'user_location': tweet.author.location.encode('utf-8') })
        if counter == 5:
            time.sleep(30)
            counter = 0
            general_counter = general_counter + 1
        if general_counter == 5:
            time.sleep(60)
            general_counter = 0
except BaseException, e:
    print 'failed ondata,', str(e)
    time.sleep(5) 

# <codecell>

print partiler

# <codecell>

for tweet in tweepy.Cursor(api.search,q="akp OR chp OR mhp OR bdp OR hdp", lang="tr").items(10000):
     print tweet.created_at

# <codecell>

len(results)

# <codecell>

def print_tweet(tweet):
    print "@%s - %s (%s)" % (tweet.user.screen_name, tweet.user.name, tweet.created_at)
    print tweet.text

tweet=results[1]
print_tweet(tweet)

# <codecell>

partiler = {}
partiler["akp"] = 0
partiler["chp"] = 0
partiler["mhp"] = 0
partiler["bdp"] = 0 

def process_results(results):
    id_list = [tweet.id for tweet in results]
    data_set = pd.DataFrame(id_list, columns=["id"])
   
    # Processing Tweet Data

    data_set["text"] = [tweet.text for tweet in results]
    data_set["created_at"] = [tweet.created_at for tweet in results]
    data_set["retweet_count"] = [tweet.retweet_count for tweet in results]
    data_set["favorite_count"] = [tweet.favorite_count for tweet in results]
    data_set["source"] = [tweet.source for tweet in results]
    data_set["geo"] = [tweet.geo for tweet in results]
    data_set["coordinates"] = [tweet.coordinates for tweet in results]
    data_set["place"] = [tweet.place for tweet in results]
    
    # Processing User Data
    #data_set["user_id"] = [tweet.author.id for tweet in results]
    data_set["user_screen_name"] = [tweet.author.screen_name for tweet in results]
    data_set["user_name"] = [tweet.author.name for tweet in results]
    data_set["user_created_at"] = [tweet.author.created_at for tweet in results]
    #data_set["user_description"] = [tweet.author.description for tweet in results]
    #data_set["user_followers_count"] = [tweet.author.followers_count for tweet in results]
    #data_set["user_friends_count"] = [tweet.author.friends_count for tweet in results]
    data_set["user_location"] = [tweet.author.location for tweet in results]
    for tweet in results:
        print tweet.text
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
    return data_set
data_set = process_results(results)

# <codecell>

partiler

# <codecell>

data_set

# <codecell>

import csv

with open('names.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

# <codecell>

status = twitter.get_application_rate_limit_status(resources = ['statuses'])

# <codecell>


