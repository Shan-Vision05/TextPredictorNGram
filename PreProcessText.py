import nltk
import nltk
from nltk.corpus import brown, webtext, reuters


corpora = ['brown', 'webtext', 'reuters', 'punkt']

class Corpora():
    def __init__(self):
        self.corpora = ['brown', 'webtext', 'reuters', 'punkt']

        self.__DownloadRequiredCorpora()

    def __DownloadRequiredCorpora(self):
        for corpus in self.corpora:
            try:
                nltk.data.find(f"corpora/{corpus}")
            except LookupError:
                print(f"Downloading {corpus}...")
                nltk.download(corpus)

    def GetCorpus(self, nltk_corpus, max_sentences=5000):
        corpus = [" ".join(sentence) for sentence in nltk_corpus.sents()]
        corpus = ["<s> " + sentence + " </s>" for sentence in corpus][:max_sentences]
        return corpus  

        