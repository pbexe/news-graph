
# Import required libs
from nltk.corpus import stopwords
from collections import Counter
from tqdm import tqdm


def generate(fp, lexicon):
    """Generate probabilities of a word belonging to a certain class
    """
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


def lexicon():
    """Build the lexicon of all recognized words
    Returns dictionary of all words as keys and 0s as values
    """
    stop_words = set(stopwords.words('english'))
    with open('pos.txt', 'r') as fp:
        pos = fp.read()
    with open('neg.txt', 'r') as fp:
        neg = fp.read()
    words = pos + neg
    lexicon = []
    [lexicon.append(word.replace('\n', '').lower()) for word in words.split(' ') if word not in stop_words and word not in ['.', ',', '--', '"']]
    lexicon_frequency = Counter(lexicon)
    lexicon_frequency = dict(lexicon_frequency)
    for key in lexicon_frequency:
        lexicon_frequency[key] = 0
    return lexicon_frequency


def sentiment(sentence, pos_lex, neg_lex):
    """Generate the sentiment of 'sentence' using Bayes' Theorum.

    >>> sentiment('That was good', generate('pos.txt', lexicon()), generate('neg.txt', lexicon()))
    1
    """
    s = sentence.split(' ')
    p_pos = 0.5
    p_neg = 0.5
    p_pos_sentiment = p_pos
    for word in s:
        if word in pos_lex and word not in set(stopwords.words('english')):
            p_pos_sentiment = p_pos_sentiment * pos_lex[word]
    p_neg_sentiment = p_neg
    for word in s:
        if word in neg_lex and word not in set(stopwords.words('english')):
            p_neg_sentiment = p_neg_sentiment * neg_lex[word]
    if p_pos_sentiment > p_neg_sentiment:
        return 1
    else:
        return 0

if __name__ == '__main__':
    pos_lex = generate('pos.txt', lexicon())
    neg_lex = generate('neg.txt', lexicon())
    correct = 0
    incorrect = 0
    with open('pos.txt', 'r') as fp:
            pos = fp.readlines()
            for line in tqdm(pos):
                if sentiment(line, pos_lex, neg_lex) == 1:
                    correct += 1
                else:
                    incorrect += 1
    with open('neg.txt', 'r') as fp:
        neg = fp.readlines()
        for line in tqdm(neg):
                if sentiment(line, pos_lex, neg_lex) == 0:
                    correct += 1
                else:
                    incorrect += 1
    print(correct/(correct+incorrect)*100)
    while 1:
        print(sentiment(input('Sentiment In >>> '), pos_lex, neg_lex))
