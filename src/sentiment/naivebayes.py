"""Tools needed to generate sentiment using a naive bayes classifier.
"""
from nltk.corpus import stopwords
from collections import Counter
import string


def generate(fp, lexicon):
    """Generate probabilities of a word belonging to a certain class
    Args:
        fp (str): Location of file
        lexicon (dict): Dictionary of all words known to the classifier
    Returns:
        dict: Lexicon of words from `fp`
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
    Returns:
        Dict: Dictionary of all words as keys and 0s as values
    """
    stop_words = set(stopwords.words('english'))
    with open('sentiment/pos.txt', 'r') as fp:
        pos = fp.read()
    with open('sentiment/neg.txt', 'r') as fp:
        neg = fp.read()
    words = pos + neg
    lexicon = []
    [lexicon.append(word.replace('\n', '').lower()) for word in words.split(' ') if word not in stop_words and word not in string.punctuation]
    lexicon_frequency = Counter(lexicon)
    lexicon_frequency = dict(lexicon_frequency)
    for key in lexicon_frequency:
        lexicon_frequency[key] = 0
    return lexicon_frequency


def sentiment(sentence, pos_lex, neg_lex):
    """Generate the sentiment of 'sentence' using Bayes' Theorum.
    Args:
        sentence (str): Sentence from which the sentiment will be calculated.
        pos_lex (dict): Lexicon of words and their positive frequency.
        neg_lex (dict): Lexicon of words and their negative frequency.
    Returns:
        float: Sentiment of `sentence`
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
    if p_neg_sentiment != 0 and p_pos_sentiment != 0:
        return round(p_pos_sentiment / (p_pos_sentiment + p_neg_sentiment), 4)
    else:
        return 0.5
