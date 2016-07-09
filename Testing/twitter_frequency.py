from nltk.corpus import twitter_samples
import nltk
import plotly.plotly as py
import plotly.graph_objs as go

print twitter_samples.fileids()

posTags = {}
negTags = {}

tokenized = twitter_samples.tokenized('positive_tweets.json')
for toks in tokenized:
	toks = nltk.pos_tag(toks)
	for word in toks:
		if word[1] in posTags:
			posTags[word[1]] += 1
		else:
			posTags[word[1]] = 1

tokenized = twitter_samples.tokenized('negative_tweets.json')
for toks in tokenized:
	toks = nltk.pos_tag(toks)
	for word in toks:
		if word[1] in negTags:
			negTags[word[1]] += 1
		else:
			negTags[word[1]] = 1

allTags = {}
for tag in posTags:
	if tag in negTags:
		allTags[tag] = posTags[tag] - negTags[tag]
	else:
		allTags[tag] = posTags[tag]
for tag in negTags:
	if tag not in allTags:
		allTags[tag] = 0 - negTags[tag]

X = []
Y = []

for key in allTags:
	X.append(key)
	Y.append(allTags[key])

YX = zip(Y,X)
YX.sort()

Ynew = [Y for Y,X in YX]
Xnew = [X for Y,X in YX]
print Xnew
print Ynew

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
py.plot(fig, filename='twitter-sentiment-POS')

    