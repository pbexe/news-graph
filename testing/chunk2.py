import nltk

def prepareForNLP(text):
	sentences = nltk.sent_tokenize(text)
	sentences = [nltk.word_tokenize(sent) for sent in sentences]
	sentences = [nltk.pos_tag(sent) for sent in sentences]
	return sentences

def chunk(sentence):
	chunkToExtract = """
	NP: {<NNP>*}
		# {<DT>?<JJ>?<NNS>}
		{<NN><NN>}"""
	parser = nltk.RegexpParser(chunkToExtract)
	result = parser.parse(sentence)
	for subtree in result.subtrees():
		if subtree.label() == 'NP':
			t = subtree
			t = ' '.join(word for word, pos in t.leaves())
			print(t)



sentences = prepareForNLP("France's Laurent Fabius says new climate draft would be legally binding and aims to keep temperature rises 'well below 2C'")
for sentence in sentences:
	chunk(sentence)