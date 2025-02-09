from models.BiGramModel import BiGram
from models.TriGramModel import TriGram
from nltk.tokenize import word_tokenize
import numpy as np

class PerplexityScore():
    def __init__(self, model):
        self.model = model

    def GetScore(self,sentence):
        
        if isinstance(self.model, BiGram):
            return self.__BiGramScore(sentence)
        return self.__TriGramScore(sentence)
    
    def __BiGramScore(self, sentence):
        tokens = word_tokenize(sentence)
        lengthTokens = len(tokens)
        probabilities = []
        
        probabilities.append(self.model.UniGramProbability(tokens[0]))

        for i in range(1,len(tokens)-1):
            cond_prob = self.model.ConditionalProbabilityBiGram(tokens[i], tokens[i+1])
            probabilities.append(cond_prob)

        logProbabilities = np.log(probabilities)

        perplexity = (-1/lengthTokens) * (sum(logProbabilities))

        return np.exp(perplexity)
        



    def __TriGramScore(self, sentence):
        tokens = word_tokenize(sentence)
        lengthTokens = len(tokens)
        probabilities = []
        
        probabilities.append(self.model.BiGramProbability(tokens[0], tokens[1]))

        for i in range(2,len(tokens)-2):
            cond_prob = self.model.ConditionalProbabilityTriGram(tokens[i], tokens[i+1], tokens[i+2])
            probabilities.append(cond_prob)
        
        logProbabilities = np.log(probabilities)

        perplexity = (-1/lengthTokens) * (sum(logProbabilities))

        return np.exp(perplexity)