from collections import Counter
from nltk.tokenize import word_tokenize

class BiGram():
    def __init__(self, corpus):
        self.corpus = corpus
        self.__SetupUnigram()
        self.__SetupBigram()

    def LaplaceNormalization(self, counter):
        counter = {key: value+1 for key, value in counter.items()}

    def __SetupUnigram(self):
        self.uniGram = Counter()

        for sentence in self.corpus:
            for word in word_tokenize(sentence):
                self.uniGram[word] += 1
        self.LaplaceNormalization(self.uniGram)

    def __SetupBigram(self):
        self.biGram = Counter()

        entireCorpus = ''
        for sentence in self.corpus:
            entireCorpus += sentence + ' '

        words = word_tokenize(entireCorpus)
        for i in range(len(words)-1):
            self.biGram[(words[i], words[i+1])] += 1

        self.LaplaceNormalization(self.biGram)
    
    def UniGramProbability(self, word:str):
        word = word.strip().lower()
        if word in self.uniGram:
            return self.uniGram[word] / sum(self.uniGram.values())
        print("Word doesn't exist in corpus")

    def ConditionalProbabilityBiGram(self, firstWord:str, secondWord:str):
        firstWord = firstWord.strip().lower()
        secondWord = secondWord.strip().lower()

        if (firstWord, secondWord) in self.biGram:
            return self.biGram[(firstWord, secondWord)] / self.uniGram[firstWord]
        print(f"Either words {firstWord} or {secondWord} not present in the corpus")
    
    def PredictNextWord(self, word:str):
        word = word.strip().lower()
        candidates = {w2: count for  (prev_w1, w2), count in self.biGram.items() if prev_w1 == word}

        if not candidates:
            print("No Bigrams found")
            return
        next_word = max(candidates, key=candidates.get)
        return next_word
    
    def PredictNWords(self, word:str, n:int):
        prevWord = word.strip().lower()

        sentence = prevWord + ' '
        for i in range(n):
            candidates = {w2 : count for (prev_w1, w2), count in self.biGram.items() if prev_w1 == prevWord}
            if not candidates:
                print("No more Bigrams Found")
                return sentence
            next_word = max(candidates, key = candidates.get)
            sentence += next_word + ' '
            prevWord = next_word
        return sentence
