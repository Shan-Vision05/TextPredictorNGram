from PreProcessText import Corpora
from models.BiGramModel import BiGram
from models.TriGramModel import TriGram

from Perplexity import PerplexityScore

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

    perplexityBi = PerplexityScore(biGram_Brown)

    print(f"Perplexity BiGram: {perplexityBi.GetScore(reutersCorpus[0])}")

    perplexityTri = PerplexityScore(triGram_Brown)

    print(f"Perplexity TriGram: {perplexityTri.GetScore(reutersCorpus[0])}")




if __name__ == '__main__':
    main()