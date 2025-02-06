from PreProcessText import Corpora
from nltk.corpus import brown, webtext, reuters


def main():
    corpora = Corpora()

    brownCorpus = corpora.GetCorpus(brown)
    webtextCorpus = corpora.GetCorpus(webtext)
    reutersCorpus = corpora.GetCorpus(reuters)