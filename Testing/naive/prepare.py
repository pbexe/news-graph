# Import required libs
from nltk.corpus import twitter_samples, stopwords
from nltk.tokenize import word_tokenize
import re
from collections import Counter
from nltk.stem import WordNetLemmatizer
import numpy
import random
import pickle
from datadiff import diff

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
    with open('pos2.txt', 'r') as fp:
        pos = fp.read()
    with open('neg2.txt', 'r') as fp:
        neg = fp.read()
    words = pos + neg
    # Before and after filtering arrays
    lexicon = []
    lexicon_filtered = []
    # Create list of words from data set
    [lexicon.append(word.replace('\n', '').lower()) for word in words.split(' ') if word not in stop_words and word not in ['.', ',', '--', '"']]
    # Make each item unique
    lexicon_frequency = Counter(lexicon)
    lexicon_frequency = dict(lexicon_frequency)
    for key in lexicon_frequency:
        lexicon_frequency[key] = 0
    return lexicon_frequency

def generate(fp, lexicon):
    lex = lexicon
    with open(fp, 'r') as fp:
        words = fp.read().lower().replace('\n', ' ').split(' ')
        for word in words:
            if word in lex:
                lex[word] += 1
        total_pos_words = sum(lex.values())
        for key in lex:
            lex[key] = (lex[key] + 1) / (total_pos_words + len(lex))
    return lex

if __name__ == '__main__':
    lex = lexicon()
    p_pos = 0.5
    p_neg = 0.5
    pos_lex = generate('pos.txt', lexicon())
    neg_lex = generate('neg.txt', lexicon())
    while 1:
        s = input('>>> ').split(' ')
        p_pos_sentiment = p_pos
        for word in s:
            if word in pos_lex:
                p_pos_sentiment = p_pos_sentiment * pos_lex[word]
        p_neg_sentiment = p_neg
        for word in s:
            if word in neg_lex:
                p_neg_sentiment = p_neg_sentiment * neg_lex[word]
        if p_pos_sentiment > p_neg_sentiment:
            print('Positive')
        else:
            print('Negative')