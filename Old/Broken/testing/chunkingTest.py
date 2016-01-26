import nltk
def prepareForNLP(text):
	sentences = nltk.sent_tokenize(text)
	sentences = [nltk.word_tokenize(sent) for sent in sentences]
	sentences = [nltk.pos_tag(sent) for sent in sentences]
	for i in sentences:
		for x in i:
			if x[1] == "VBD":
				print(x[0])
	# print(sentences)

with open("text.txt", "r") as fp:
	prepareForNLP(fp.read())