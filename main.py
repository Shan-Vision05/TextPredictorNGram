from PreProcessText import Corpora
from models.BiGramModel import BiGram

from nltk.corpus import brown, webtext, reuters


def main():
    corpora = Corpora()

    brownCorpus = corpora.GetCorpus(brown)
    webtextCorpus = corpora.GetCorpus(webtext)
    reutersCorpus = corpora.GetCorpus(reuters)

    biGram_Brown = BiGram(brownCorpus)
    biGram_Webtext = BiGram(webtextCorpus)


if __name__ == '__main__':
    main()