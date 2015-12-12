import nltk

def prepareForNLP(text):
	sentences = nltk.sent_tokenize(text)
	sentences = [nltk.word_tokenize(sent) for sent in sentences]
	sentences = [nltk.pos_tag(sent) for sent in sentences]
	return sentences

def chunk(sentence):
	chunkToExtract = """
	NP: {<NNP>*}
		{<DT>?<JJ>?<NNS>}"""
	parser = nltk.RegexpParser(chunkToExtract)
	result = parser.parse(sentence)
	result.draw()
	


sentences = prepareForNLP("Saudi Arabia is going to the polls for unprecedented elections in which women can cast a ballot for the first time.")
for sentence in sentences:
	chunk(sentence)