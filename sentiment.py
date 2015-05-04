import math
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
 
## Pozitif negatif keliemler
filenameAFINN = 'pos_neg.txt'


afinn = dict(map(lambda (w, s): (w, int(s)), [ 
            ws.strip().split('\t') for ws in open(filenameAFINN) ]))
 
# kelimeleri bol
pattern_split = re.compile(r"\W+")
 
def sentiment(text):
   
    words = pattern_split.split(text.lower())
    sentiments = map(lambda word: afinn.get(word, 0), words)
    if sentiments:
        
	##  karesini al
        sentiment = float(sum(sentiments))/math.sqrt(len(sentiments))
        
    else:
        sentiment = 0
    return sentiment
 
 
 
if __name__ == '__main__':
    text = ""
    print("%6.2f %s" % (sentiment(text), text))
