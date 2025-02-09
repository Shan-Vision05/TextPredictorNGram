from collections import Counter
from nltk.tokenize import word_tokenize

class BiGram():
    def __init__(self, corpus):
        self.corpus = corpus
        self.__SetupUnigram()
        self.__SetupBigram()


    def __SetupUnigram(self):
        self.uniGram = Counter()

        for sentence in self.corpus:
            for word in word_tokenize(sentence):
                self.uniGram[word] += 1


    def __SetupBigram(self):
        self.biGram = Counter()

        entireCorpus = ''
        for sentence in self.corpus:
            entireCorpus += sentence + ' '

        words = word_tokenize(entireCorpus)
        for i in range(len(words)-1):
            self.biGram[(words[i], words[i+1])] += 1

    def __GetUnigramCount(self, word):

        if word in self.uniGram:
            return (self.uniGram[word] + 1)
        return 1
    
    def UniGramProbability(self, word:str):

        total_count = sum(self.uniGram.values()) + len(self.uniGram.values())
        word = word.strip().lower()

        return self.__GetUnigramCount(word) / total_count

    def __GetBigramCount(self, firstWord, secondWord):
        if (firstWord, secondWord) in self.biGram:
            return self.biGram[(firstWord, secondWord)] + 1
        return 1

    def ConditionalProbabilityBiGram(self, firstWord:str, secondWord:str):
        firstWord = firstWord.strip().lower()
        secondWord = secondWord.strip().lower()
        prior_counts = self.__GetUnigramCount(firstWord)

        if firstWord not in self.uniGram:
            prior_counts += len(self.uniGram.values())

        return self.__GetBigramCount(firstWord, secondWord) / prior_counts

    def GetBigramsForASentence(self, sentence):
        words = word_tokenize(sentence)
        bigrams = []
        for i in range(len(words)-1):
            bigrams.append((words[i], words[i+1]))

        return bigrams
    
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
