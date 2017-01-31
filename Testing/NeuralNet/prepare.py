# Import required libs
from nltk.corpus import twitter_samples, stopwords
from nltk.tokenize import word_tokenize
import re
from collections import Counter
from nltk.stem import WordNetLemmatizer
import numpy
import random
import pickle

print(twitter_samples.fileids())
# Init the lemmatizer
lemmatizer = WordNetLemmatizer()


# Build the lexicon
def lexicon_old():
    # Stop words to ignore
    stop_words = set(stopwords.words('english'))
    # Load the tweets
    tweets = twitter_samples.strings('tweets.20150430-223406.json')
    # Before and after filtering arrays
    lexicon = []
    lexicon_filtered = []
    # Create list of words from data set
    [[lexicon.append(lemmatizer.lemmatize(x)) for x in [w for w in word_tokenize(re.sub(r'RT |@\S*|#\S+|http\S+|\n-|w/|[\.]{2,}', '', tweet)) if w not in stop_words]] for tweet in tweets]
    # Make each item unique
    lexicon_frequency = Counter(lexicon)
    for word in lexicon_frequency:
        if (len(lexicon) * 0.8) > lexicon_frequency[word]:
            lexicon_filtered.append(word)
    with open('lex.data','wb') as fp:
        pickle.dump(lexicon_filtered, fp)
    return lexicon_filtered

# Build the lexicon
def lexicon():
    # Stop words to ignore
    stop_words = set(stopwords.words('english'))
    with open('pos.txt', 'r') as fp:
        pos = fp.read()
    with open('neg.txt', 'r') as fp:
        neg = fp.read()
    words = pos + neg
    # Before and after filtering arrays
    lexicon = []
    lexicon_filtered = []
    # Create list of words from data set
    [lexicon.append(lemmatizer.lemmatize(word)) for word in words.split(' ') if word not in stop_words]
    # Make each item unique
    lexicon_frequency = Counter(lexicon)
    for word in lexicon_frequency:
        if (len(lexicon) * 0.8) > lexicon_frequency[word]:
            lexicon_filtered.append(word)
    with open('lex.data','wb') as fp:
        pickle.dump(lexicon_filtered, fp)
    return lexicon_filtered

def parse_sample(sample, sentiment, lexicon):
    oppinion_sentence_with_sentiment = []
    with open(sample, 'r') as fp:
        for line in fp.readlines():
            line = word_tokenize(line.lower())
            line = [lemmatizer.lemmatize(word) for word in line]
            lexicon_mask = numpy.zeros(len(lexicon))
            for word in line:
                if word.lower() in lexicon:
                    index_value = lexicon.index(word.lower())
                    lexicon_mask[index_value] += 1
            oppinion_sentence_with_sentiment.append([list(lexicon_mask), sentiment])
    return oppinion_sentence_with_sentiment


def create_training_data(lexicon):
    data = []
    data += parse_sample('pos.txt', [1, 0], lexicon)
    data += parse_sample('neg.txt', [0, 1], lexicon)
    random.shuffle(data)
    test_data = int(len(data)*0.1)
    x_training_data = []
    for item in data[:-test_data]:
        x_training_data.append(item[0])
    y_training_data = []
    for item in data[:-test_data]:
        y_training_data.append(item[1])
    x_test_data = []
    for item in data[-test_data:]:
        x_test_data.append(item[0])
    y_test_data = []
    for item in data[-test_data:]:
        y_test_data.append(item[1])
    return x_training_data, y_training_data, x_test_data, y_test_data
