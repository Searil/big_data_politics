from BeautifulSoup import BeautifulSoup
from pprint import pprint
import MySQLdb
import urllib2
import json
import sys


def parser(baslangic_yil, bitis_yil):
	db = MySQLdb.connect("localhost","root","","wiki")
	lines = open('wiki_article_name.txt').read().splitlines()
	for line in lines:
		cursor = db.cursor()
		for yil in range(int(baslangic_yil),int(bitis_yil)+1):
			for ay in range(1,13):
				#print str(ay) + " " + str(yil)
				url_line = line.replace(" ","%20")
				if ay < 10:
					ay = "0" + str(ay)

				url = "http://stats.grok.se/json/en/"+str(yil)+str(ay)+"/"+url_line
				print url
				page = urllib2.urlopen(url)
				soup = BeautifulSoup(page.read())

				context = json.loads(str(soup))
				day_list = context['daily_views']
				print type(day_list)
				if len(day_list) > 0:
					for day in day_list:
						print day, day_list[day]
						sql = "INSERT INTO wiki (article_name, date_, view) VALUES ('%s', '%s', '%d')" % (line,day,day_list[day])
						cursor.execute(sql)
				print len(day_list)

				try:
	   				# Commit your changes in the database
	 				db.commit()
				except:
	   				# Rollback in case there is any error
	   				db.rollback()
	db.close()
		
if __name__ == "__main__":
	baslangic_yil = sys.argv[1]
	bitis_yil = sys.argv[2]
	parser(baslangic_yil, bitis_yil)

	#f = open(sys.argv[1],'r')
	#out = f.read().splitlines() # will append in the list out
