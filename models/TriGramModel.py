from collections import Counter
from nltk.tokenize import word_tokenize

class TriGram():
  def __init__(self, corpus):
    self.corpus = corpus

    self.SetupBiGram()
    self.SetupTriGram()

  def LaplaceNormalization(self, counter):
    counter = {key: value+1 for key, value in counter.items()}


  def SetupBiGram(self):
    self.biGram = Counter()

    entireCorpus = ''
    for sentence in self.corpus:
      entireCorpus += sentence + ' '

    words = word_tokenize(entireCorpus)
    for i in range(len(words)-1):
      self.biGram[(words[i], words[i+1])] += 1

    self.LaplaceNormalization(self.biGram)

  def SetupTriGram(self):
    self.triGram = Counter()

    entireCorpus = ''
    for sentence in self.corpus:
      entireCorpus += sentence + ' '

    words = word_tokenize(entireCorpus)
    for i in range(len(words)-2):
      self.triGram[(words[i], words[i+1], words[i+2])] += 1

    self.LaplaceNormalization(self.triGram)

  def ConditionalProbabilityTriGram(self, firstWord:str, secondWord:str, thirdWord:str):
    
    firstWord = firstWord.strip().lower()
    secondWord = secondWord.strip().lower()
    thirdWord = thirdWord.strip().lower()

    if (firstWord, secondWord, thirdWord) in self.triGram:
      return self.triGram[(firstWord, secondWord, thirdWord)] / self.biGram[(firstWord, secondWord)]
    print("Either words not present in the corpus")

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
