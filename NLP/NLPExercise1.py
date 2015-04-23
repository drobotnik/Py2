import os
from nltk import *
from nltk_data import *





class Exercise01(object):

	def __init__(self, path=None, corpus=None):
		self.corpus = NLTKCorpus(corpus)
		self.model = Model(path=path, corpus=self.corpus)

	def explore(self):
		print "Father is to boy as ? is to girl"
		print self.model.model.most_similar(['girl', 'father'], ['boy'], topn=3)
		print
		print "Mother is to boy as ? is to girl"
		print self.model.model.most_similar(['girl', 'mother'], ['boy'], topn=3)
		print
		print "King is to man as ? is to woman"
		print self.model.model.most_similar(positive=['woman', 'king'], negative=['man'], topn=10)
		print
		print "Odd one out of 'breakfast cereal dinner lunch' is ..."
		print self.model.model.doesnt_match("breakfast cereal dinner lunch".split())


if __name__ == '__main__':
	cwd = os.getcwd()
	ex = Exercise01(path=cwd + '/../models' + '/brown.bin', corpus=brown)
	ex.explore()