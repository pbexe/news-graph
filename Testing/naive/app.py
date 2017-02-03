from flask import Flask, request
import naivebayes


app = Flask(__name__)
pos_lex = naivebayes.generate('pos.txt', naivebayes.lexicon())
neg_lex = naivebayes.generate('neg.txt', naivebayes.lexicon())


@app.route("/")
def hello():
    msg = ''

    if len(request.args.get('text', '')) != 0:
        if naivebayes.sentiment(request.args.get('text', ''), pos_lex, neg_lex) == 1:
            msg = 'Positive'
        else:
            msg = 'Negative'

    return '<form action="/" method="GET"><input name="text" autofocus><input type="submit" value=">"></form><br>' + msg


if __name__ == "__main__":
    app.run()
