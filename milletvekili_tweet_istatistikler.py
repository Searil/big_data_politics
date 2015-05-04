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
import datetime
from __future__ import division

pd.options.display.max_columns = 50
pd.options.display.max_rows= 50
pd.options.display.width= 120

auth = tweepy.auth.OAuthHandler('mEnkTsYmvFGgzjV73SPOz084K', 'YnQxTyFhTCG5KSGBeRq1qeVwUkxOhZ99amm6uauy8ett51UE3t')
auth.set_access_token('301689344-MG8rknSLPC8dUXAjWE6Eo4DQTeS4JJGjNuTJ6i41', 'vcjYSSekdT0O8qwMVhh9e6flVC1LaP5OlssIsU4nGWewh')
api = tweepy.API(auth)

# <codecell>

milletvekilleri = {}
milletvekilleri['akp'] = 0
milletvekilleri['chp'] = 0
milletvekilleri['mhp'] = 0
milletvekilleri['bdp'] = 0
with open('milletvekil_twitter.txt', 'r') as f:
    read_data = f.read()
    read_data = read_data.strip()
    read_data = read_data.replace('\n',',')
    veri = read_data.split(",")
    print veri[0], veri[1]
    milletvekilleri[veri[1]] = milletvekilleri[veri[1]] + 1

# <codecell>

milletvekilleri = {}
milletvekilleri['akp'] = 0
milletvekilleri['chp'] = 0
milletvekilleri['mhp'] = 0
milletvekilleri['bdp'] = 0

akp_milletvekilleri = []
chp_milletvekilleri = []
mhp_milletvekilleri = []
bdp_milletvekilleri = []

with open("milletvekil_twitter", "r") as ins:
    for line in ins:
        line = line.strip()
        veri = line.split(",")
        parti = veri[1]
        if parti == "hdp":
            parti = "bdp"
        milletvekilleri[parti] = milletvekilleri[parti] + 1
        if parti == "akp":
            akp_milletvekilleri.append(veri[0])
        elif parti == "chp":
            chp_milletvekilleri.append(veri[0])
        elif parti == "mhp":
            mhp_milletvekilleri.append(veri[0])
        elif parti == "bdp":
            bdp_milletvekilleri.append(veri[0])

# <codecell>

milletvekilleri

# <codecell>

akp_toplam_follower = 0 
akp_toplam_retweet = 0
akp_toplam_favori = 0
akp_toplam_tweet = 0


for vekil in bdp_milletvekilleri:
    
    mart_tweet_sayisi = 0
    toplam_favori_sayisi = 0
    toplam_retweet_sayisi = 0
    if "@" in vekil:
        vekil = vekil.replace("@","")
    screen_name = vekil
    print screen_name
    new_tweets = api.user_timeline(screen_name = screen_name,count=50)
    alltweets = []	
    alltweets.extend(new_tweets)
    user = api.get_user(vekil)
    takipci_sayisi = user.followers_count
    akp_toplam_follower = akp_toplam_follower + takipci_sayisi
    
    d = datetime.datetime.strptime('2015-03-01', '%Y-%m-%d')
    for tweet in alltweets:
        if tweet.created_at > d:
            mart_tweet_sayisi = mart_tweet_sayisi + 1
            toplam_favori_sayisi = toplam_favori_sayisi + tweet.favorite_count
            toplam_retweet_sayisi = toplam_retweet_sayisi + tweet.retweet_count
    
    akp_toplam_tweet = akp_toplam_tweet + mart_tweet_sayisi
    akp_toplam_retweet = akp_toplam_retweet + toplam_retweet_sayisi
    akp_toplam_favori = akp_toplam_favori + toplam_favori_sayisi

# <codecell>

print akp_toplam_tweet
print akp_toplam_retweet
print akp_toplam_favori
print akp_toplam_follower
print float(akp_toplam_retweet / akp_toplam_follower)
print float(akp_toplam_favori / akp_toplam_follower)

# <codecell>

print "bdp tweet oranı(Kişi Başına) " , (197 + 41) / 9
print "bdp atılan tweetlerin retweet oranı(Tweet başına) ", (24764 + 3076) / (197 + 41)
print "bdp atılan tweelerin favorilenme oranı(Tweet başına) ", (13433 + 5894) / (197 + 41)
print "bdp follower ortalaması(Kişi Başına)", (1432812 + 884304) / 9
print "bdp follower toplamı", (1432812 + 884304)

# <codecell>

print "mhp tweet oranı(Kişi Başına) " , (108 + 100 + 68) / 16
print "mhp atılan tweetlerin retweet oranı(Tweet başına) ", (9225 + 35305 + 5362) / (108 + 100 + 68)
print "mhp atılan tweelerin favorilenme oranı(Tweet başına) ", (6626 + 55972 + 223 + 282) / (108 + 100 + 68)
print "mhp follower ortalaması(Kişi Başına)", (1432812 + 884304 + 84629) / 16
print "mhp follower toplamı", (1432812 + 884304 + 84629)

# <codecell>

print "chp tweet oranı(Kişi Başına) " , (190 + 213 + 50 +56+160) / 30
print "chp atılan tweetlerin retweet oranı(Tweet başına) ", (28237 + 13355 + 826+81166+21174) / (190 + 213 + 50 +56+160)
print "chp atılan tweelerin favorilenme oranı(Tweet başına) ", (7231 + 13833 + 425 +309)  / (190 + 213 + 50 +56+160)
print "chp follower ortalaması(Kişi Başına)", (1711910 + 3094203 + 40975 +31508+328479) / 30
print "chp follower toplamı", (1711910 + 3094203 + 40975 +31508+328479)

# <codecell>

print "akp tweet oranı(Kişi Başına) " , (725 + 245 + 58 +150+50+128) / 53
print "akp atılan tweetlerin retweet oranı(Tweet başına) ", (222477 + 28513 + 5595+13479+15955+32161) / (725 + 245 + 58 +150+50)
print "akp atılan tweelerin favorilenme oranı(Tweet başına) ", (139904 + 32422 + 5648 +5334+702+1505)  / (725 + 245 + 58 +150+50)
print "akp follower ortalaması(Kişi Başına)", (8003814 + 3198140 + 3005126 +1586243+108890+232784) / 53
print "akp follower toplamı", (8003814 + 3198140 + 3005126 +1586243+108890+232784)

# <codecell>

print "bdp %", 116/(116 + 180 + 216 + 260)
print "mhp %", 180/(116 + 180 + 216 + 260)
print "chp %", 216/(116 + 180 + 216 + 260)
print "akp %", 260/(116 + 180 + 216 + 260)

# <codecell>

BDP
---
197
24764
13433
1432812
0.0172834956714
0.0093752704472
---
41
3076
5894
884304
0.00347844180282
0.00666512873401

MHP
---
108
9225
6626
315650
0.0292254078885
0.0209916046254
---
100
35305
55972
2175574
0.0162279012343
0.025727463189
---
0
0
0
223
0.0
0.0
---
68
5362
282
84629
0.0633588958868
0.00333219109289

CHP
----
190
28237
7231
1711910
0.0164944418807
0.00422393700603
---
213
13355
13833
3094203
0.00431613568987
0.0044706181204
---
50
826
413
40975
0.020158633313
0.0100793166565
---
56
81166
12
31508
2.57604417926
0.000380855655706
---
160
21174
309
328479
0.0644607417826
0.000940699405441
---
burdada sildim

print akp_toplam_tweet
print akp_toplam_retweet
print akp_toplam_favori
print akp_toplam_follower
print float(akp_toplam_retweet / akp_toplam_follower)
print float(akp_toplam_favori / akp_toplam_follower)
725
222477
139904
8003814
0.0277963730791
0.017479666569
---
245
28513
32422
3198140
0.00891549463125
0.0101377675774
---
58
5595
5648
3005126
0.00186181877232
0.00187945530404
---
150
13479
5334
1586243
0.00849743702573
0.00336266259331
---
50
15955
702
108890
0.146524015061
0.00644687299109
---
128
32161
1505
232784
0.138158120833
0.00646522097739

# <codecell>

screen_name = "RT_Erdogan"
new_tweets = api.user_timeline(screen_name = screen_name,count=20)
alltweets = []	
alltweets.extend(new_tweets)

# <codecell>

alltweets = []	
alltweets.extend(new_tweets)

# <codecell>

d = datetime.datetime.strptime('2015-03-17', '%Y-%m-%d')
for tweet in alltweets:
    if tweet.created_at > d:
        print tweet.created_at, "favorite count", tweet.favorite_count, "retweet_count", tweet.retweet_count

# <codecell>


# Get information about the user
data = api.get_user('RT_Erdogan')

print 'Followers: ' + str(data.followers_count)
print 'Tweets: ' + str(data.statuses_count)
print 'Favouries: ' + str(data.favourites_count)
print 'Friends: ' + str(data.friends_count)
print 'Appears on ' + str(data.listed_count) + ' lists'
print data.screen_name
# Get information about the user
data = api.get_user('idrisgulluce')

print 'Followers: ' + str(data.followers_count)
print 'Tweets: ' + str(data.statuses_count)
print 'Favouries: ' + str(data.favourites_count)
print 'Friends: ' + str(data.friends_count)
print 'Appears on ' + str(data.listed_count) + ' lists'
print data.screen_name

# <codecell>

counter = 0
def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler('mEnkTsYmvFGgzjV73SPOz084K', 'YnQxTyFhTCG5KSGBeRq1qeVwUkxOhZ99amm6uauy8ett51UE3t')
	auth.set_access_token('301689344-MG8rknSLPC8dUXAjWE6Eo4DQTeS4JJGjNuTJ6i41', 'vcjYSSekdT0O8qwMVhh9e6flVC1LaP5OlssIsU4nGWewh')
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=10)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	print len(new_tweets)
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)
		counter = counter + 1
        print counter
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print "...%s tweets downloaded so far" % (len(alltweets))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	
	#write the csv	
	with open('%s_teeeee.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)
	
	pass

# <codecell>

get_all_tweets("RT_Erdogan")

# <codecell>

import xlsxwriter
import tweepy 
 
#https://github.com/tweepy/tweepy
 
consumer_key = "mEnkTsYmvFGgzjV73SPOz084K"
consumer_secret = "YnQxTyFhTCG5KSGBeRq1qeVwUkxOhZ99amm6uauy8ett51UE3t"
access_key = "301689344-MG8rknSLPC8dUXAjWE6Eo4DQTeS4JJGjNuTJ6i41"
access_secret = "vcjYSSekdT0O8qwMVhh9e6flVC1LaP5OlssIsU4nGWewh"



def get_all_tweets(screen_name):
    counter = 0
  
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
 
    alltweets = []  
    new_tweets = []
    outtweets = []
 
    new_tweets = api.user_timeline(screen_name = screen_name,count=10)
 
    alltweets.extend(new_tweets)
 
	#save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
 
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        counter = counter + 1
        print counter
        print "getting tweets before %s" % (oldest)
 
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)
 
        #save most recent tweets
        alltweets.extend(new_tweets)
 
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
 
        print "...%s tweets downloaded so far" % (len(alltweets))
 
    #transform the tweepy tweets into a 2D array
    outtweets = [[tweet.id_str, tweet.created_at, tweet.coordinates,tweet.geo,tweet.source,tweet.text] for tweet in alltweets]
 
    return outtweets
 
def write_worksheet(twitter_name):
 
	#formating for excel
	format01 = workbook.add_format()
	format02 = workbook.add_format()
	format03 = workbook.add_format()
	format04 = workbook.add_format()
	format01.set_align('center')
	format01.set_align('vcenter')
	format02.set_align('center')
	format02.set_align('vcenter')
	format03.set_align('center')
	format03.set_align('vcenter')
	format03.set_bold()
	format04.set_align('vcenter')
	format04.set_text_wrap()
 
	out1 = []
	header = ["id","created_at","coordinates-x","coordinates-y","source","text"]
 
	worksheet = workbook.add_worksheet(twitter_name)
 
	out1 = get_all_tweets(twitter_name)
	row = 0
	col = 0
 
	worksheet.set_column('A:A', 20)
	worksheet.set_column('B:B', 18)
	worksheet.set_column('C:C', 13)
	worksheet.set_column('D:D', 13)
	worksheet.set_column('E:E', 20)
	worksheet.set_column('F:F', 120)
 
	for h_item in header:
		worksheet.write(row, col, h_item, format03)
		col = col + 1
 
	row += 1
	col = 0
	
	for o_item in out1:
		write = []
		cord1 = 0
		cord2 = 0
		write = [o_item[0], o_item[1], o_item[4], o_item[5]]
 
		if o_item[2]:
			cord1 = o_item[2]['coordinates'][0]
			cord2 = o_item[2]['coordinates'][1]
		else:
			cord1 = ""
			cord2 = ""
 
		format01.set_num_format('yyyy/mm/dd hh:mm:ss')
		worksheet.write(row, 0, write[0], format02)
		worksheet.write(row, 1, write[1], format01)
		worksheet.write(row, 2, cord1, format02)
		worksheet.write(row, 3, cord2, format02)
		worksheet.write(row, 4, write[2], format02)
		worksheet.write(row, 5, write[3], format04)
		row += 1
		col = 0
 
workbook = xlsxwriter.Workbook('Twitter_timeline.xlsx')
 
 
write_worksheet('RT_Erdogan') 
workbook.close()

# <codecell>

from rauth import OAuth1Service

# Get a real consumer key & secret from https://dev.twitter.com/apps/new
twitter = OAuth1Service(
    name='twitter',
    consumer_key = "mEnkTsYmvFGgzjV73SPOz084K",
    consumer_secret = "YnQxTyFhTCG5KSGBeRq1qeVwUkxOhZ99amm6uauy8ett51UE3t",
    access_key = "301689344-MG8rknSLPC8dUXAjWE6Eo4DQTeS4JJGjNuTJ6i41",
    access_secret = "vcjYSSekdT0O8qwMVhh9e6flVC1LaP5OlssIsU4nGWewh",
    authorize_url='https://api.twitter.com/oauth/authorize',
    base_url='https://api.twitter.com/1/')

request_token, request_token_secret = twitter.get_request_token()

authorize_url = twitter.get_authorize_url(request_token)

print 'Visit this URL in your browser: ' + authorize_url
pin = raw_input('Enter PIN from browser: ')

session = twitter.get_auth_session(request_token,
                                   request_token_secret,
                                   method='POST',
                                   data={'oauth_verifier': pin})

params = {'screen_name': 'github',  # User to pull Tweets from
          'include_rts': 1,         # Include retweets
          'count': 10}              # 10 tweets

r = session.get('statuses/user_timeline.json', params=params)

for i, tweet in enumerate(r.json(), 1):
    handle = tweet['user']['screen_name'].encode('utf-8')
    text = tweet['text'].encode('utf-8')
    print '{0}. @{1} - {2}'.format(i, handle, text)

