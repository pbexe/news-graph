# Import required libs
from nltk.corpus import twitter_samples
import nltk
import plotly.plotly as py
import plotly.graph_objs as go
from tqdm import tqdm

# These are corpus files. One positive, one negative and one mixed
print twitter_samples.fileids()

# Empty dictionaries to store the collected tags
posTags = {}
negTags = {}

# The corpuses are already POS tagged

# Load the positive tweets and load the POS tags into 'posTags'
tokenized = twitter_samples.tokenized('positive_tweets.json')
print "Loaded"
for toks in tqdm(tokenized):
	toks = nltk.pos_tag(toks)
	for word in toks:
		if word[1] in posTags:
			posTags[word[1]] += 1
		else:
			posTags[word[1]] = 1

# Load the negative tweets and load the POS tags into 'negTags'
tokenized = twitter_samples.tokenized('negative_tweets.json')
for toks in tqdm(tokenized):
	toks = nltk.pos_tag(toks)
	for word in toks:
		if word[1] in negTags:
			negTags[word[1]] += 1
		else:
			negTags[word[1]] = 1

# Subtract the frequencies of negative tags from the positive tags
allTags = {}
for tag in posTags:
	if tag in negTags:
		allTags[tag] = posTags[tag] - negTags[tag]
	else:
		allTags[tag] = posTags[tag]
for tag in negTags:
	if tag not in allTags:
		allTags[tag] = 0 - negTags[tag]

print "Done"

# Build the plot.ly graph
X = []
Y = []

for key in allTags:
	X.append(key)
	Y.append(allTags[key])

YX = zip(Y,X)
YX.sort()

Ynew = [Y for Y,X in YX]
Xnew = [X for Y,X in YX]
# print Xnew
# print Ynew

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

    