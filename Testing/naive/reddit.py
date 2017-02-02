import naivebayes
import praw
r = praw.Reddit(client_id='l-Gz5blkt7GCUg',
                client_secret='_xLEgNing89k6__sWItU1_j9aR8',
                user_agent='testscript by /u/pbexe')
pos_lex = naivebayes.generate('pos.txt', naivebayes.lexicon())
neg_lex = naivebayes.generate('neg.txt', naivebayes.lexicon())
while 1:
    total = 0
    n = 0
    for submission in r.subreddit('all').search('Trump', time_filter='day'):
        print(submission.id)
        submission.comments.replace_more(limit=10)
        comment_queue = submission.comments[:]  # Seed with top-level
        while comment_queue:
            comment = comment_queue.pop(0)
            n += 1
            total += naivebayes.sentiment(comment.body, pos_lex, neg_lex)
            comment_queue.extend(comment.replies)
    print(total/(n)*100)
