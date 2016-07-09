from nltk.corpus import twitter_samples, stopwords
from nltk.tokenize import word_tokenize
import re
from collections import Counter
import plotly.plotly as py
import plotly.graph_objs as go

print twitter_samples.fileids()
stop_words = set(stopwords.words('english'))
negTweets = twitter_samples.strings('negative_tweets.json')
posTweets = twitter_samples.strings('positive_tweets.json')
negWords = []
posWords = []
for tweet in posTweets:
	[posWords.append(x) for x in [w for w in word_tokenize(re.sub(r'RT |@\S*|#\S+|http\S+|\n-|w/|[\.]{2,}','',tweet)) if not w in stop_words]]
for tweet in negTweets:
	[negWords.append(x) for x in [w for w in word_tokenize(re.sub(r'RT |@\S*|#\S+|http\S+|\n-|w/|[\.]{2,}','',tweet)) if not w in stop_words]]

results = {}
posWords=Counter(posWords)
negWords=Counter(negWords)
for word in posWords:
	if word in negWords:
		results[word] = posWords[word] - negWords[word]
	else:
		results[word] = posWords[word]
for word in negWords:
	if not word in results:
		results[word] = 0 - negWords[word]

print results

X = []
Y = []

for item in results:
	if results[item] > 5 or results[item] < -5:
		X.append(item)
		Y.append(results[item])

YX = zip(Y,X)
YX.sort()

Ynew = [Y for Y,X in YX]
Xnew = [X for Y,X in YX]

trace1 = go.Bar(
    x=Xnew,
    y=Ynew,
    name='Tweets'
)
data = [trace1]
layout = go.Layout(
    barmode='group'
)

fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='twitter-sentiment-keywords')