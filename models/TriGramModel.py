from collections import Counter
from nltk.tokenize import word_tokenize

class TriGram():
  def __init__(self, corpus):
    self.corpus = corpus

    self.SetupUnigram()
    self.SetupBiGram()
    self.SetupTriGram()

  def SetupUnigram(self):
        self.uniGram = Counter()

        for sentence in self.corpus:
            for word in word_tokenize(sentence):
                self.uniGram[word] += 1

  def SetupBiGram(self):
    self.biGram = Counter()

    entireCorpus = ''
    for sentence in self.corpus:
      entireCorpus += sentence + ' '

    words = word_tokenize(entireCorpus)
    for i in range(len(words)-1):
      self.biGram[(words[i], words[i+1])] += 1


  def SetupTriGram(self):
    self.triGram = Counter()

    entireCorpus = ''
    for sentence in self.corpus:
      entireCorpus += sentence + ' '

    words = word_tokenize(entireCorpus)
    for i in range(len(words)-2):
      self.triGram[(words[i], words[i+1], words[i+2])] += 1

  def __GetUnigramCount(self, word):

        if word in self.uniGram:
            return (self.uniGram[word] + 1)
        return 1
  
  def __GetBigramCount(self, firstWord, secondWord):
        if (firstWord, secondWord) in self.biGram:
            return self.biGram[(firstWord, secondWord)] + 1
        return 1

  def __GetTrigramCount(self, firstWord:str, secondWord:str, thirdWord:str):

    if (firstWord, secondWord, thirdWord) in self.triGram:
      return self.triGram[(firstWord, secondWord, thirdWord)] + 1
    return 1
  
  def BiGramProbability(self, firstWord:str, secondWord:str):
        firstWord = firstWord.strip().lower()
        secondWord = secondWord.strip().lower()
        prior_counts = self.__GetUnigramCount(firstWord)

        if firstWord not in self.uniGram:
            prior_counts += len(self.uniGram.values())

        return self.__GetBigramCount(firstWord, secondWord) / prior_counts
  
  def ConditionalProbabilityTriGram(self, firstWord:str, secondWord:str, thirdWord:str):
    
    firstWord = firstWord.strip().lower()
    secondWord = secondWord.strip().lower()
    thirdWord = thirdWord.strip().lower()

    prior_counts = self.__GetBigramCount(firstWord, secondWord)

    if (firstWord, secondWord) not in self.biGram:
      prior_counts += len(self.uniGram.values())
    
    return self.__GetTrigramCount(firstWord, secondWord, thirdWord)/prior_counts

  def GetTrigramsForASentence(self, sentence):
    words = word_tokenize(sentence)
    trigrams = []
    for i in range(len(words)-2):
      trigrams.append((words[i], words[i+1], words[i+2]))

    return trigrams

  def PredictNextWord(self, firstWord:str, secondWord:str):
    firstWord = firstWord.strip().lower()
    secondWord = secondWord.strip().lower()

    candidates = {w3: count for  (prev_w1, prev_w2, w3), count in self.triGram.items() if prev_w1 == firstWord and prev_w2 == secondWord}

    if not candidates:
      print("No Bigrams found")
      return
    next_word = max(candidates, key=candidates.get)
    return next_word

  def PredictNWords(self, firstWord:str, secondWord:str, n:int):
    firstWord = firstWord.strip().lower()
    secondWord = secondWord.strip().lower()

    sentence = firstWord + ' ' + secondWord + ' '

    for i in range(n):
      candidates = {w3 : count for (prev_w1, prev_w2, w3), count in self.triGram.items() if prev_w1 == firstWord and prev_w2 == secondWord}
      if not candidates:
        print("No more Bigrams Found")
        return sentence
      next_word = max(candidates, key = candidates.get)
      sentence += next_word + ' '

      firstWord = secondWord
      secondWord = next_word

    return sentence
