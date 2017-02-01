
# Import required libs
from nltk.corpus import stopwords
from collections import Counter
from nltk.stem import WordNetLemmatizer


# Init the lemmatizer
lemmatizer = WordNetLemmatizer()


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
    # Create list of words from data set
    [lexicon.append(word.replace('\n', '').lower()) for word in words.split(' ') if word not in stop_words and word not in ['.', ',', '--', '"']]
    # Make each item unique
    lexicon_frequency = Counter(lexicon)
    lexicon_frequency = dict(lexicon_frequency)
    for key in lexicon_frequency:
        lexicon_frequency[key] = 0
    return lexicon_frequency


if __name__ == '__main__':
    p_pos = 0.5
    p_neg = 0.5
    pos_lex = generate('pos.txt', lexicon())
    neg_lex = generate('neg.txt', lexicon())
    while 1:
        s = input('>>> ').split(' ')
        p_pos_sentiment = p_pos
        for word in s:
            if word in pos_lex and word not in set(stopwords.words('english')):
                print(pos_lex[word])
                p_pos_sentiment = p_pos_sentiment * pos_lex[word]
        p_neg_sentiment = p_neg
        for word in s:
            if word in neg_lex and word not in set(stopwords.words('english')):
                print(neg_lex[word])
                p_neg_sentiment = p_neg_sentiment * neg_lex[word]
        if p_pos_sentiment > p_neg_sentiment:
            print('Positive')
        else:
            print('Negative')
