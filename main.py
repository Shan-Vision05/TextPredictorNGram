from PreProcessText import Corpora
from models.BiGramModel import BiGram
from models.TriGramModel import TriGram

from nltk.corpus import brown, webtext, reuters


def main():
    corpora = Corpora()

    brownCorpus = corpora.GetCorpus(brown)
    webtextCorpus = corpora.GetCorpus(webtext)
    reutersCorpus = corpora.GetCorpus(reuters)

    biGram_Brown = BiGram(brownCorpus)
    biGram_Webtext = BiGram(webtextCorpus)

    triGram_Brown = TriGram(brownCorpus)
    triGram_Webtext = TriGram(webtextCorpus)

    print(triGram_Brown.PredictNextWord("He", "said"))
    print(triGram_Brown.PredictNWords("He", "said", 10))


if __name__ == '__main__':
    main()