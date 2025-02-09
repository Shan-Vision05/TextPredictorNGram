from PreProcessText import Corpora
from models.BiGramModel import BiGram
from models.TriGramModel import TriGram

from Perplexity import PerplexityScore

import random
from nltk.corpus import brown, webtext, reuters

corpora = Corpora()

brownCorpus = corpora.GetCorpus(brown)
webtextCorpus = corpora.GetCorpus(webtext)
reutersCorpus = corpora.GetCorpus(reuters)

biGram_Brown = BiGram(brownCorpus)
biGram_Webtext = BiGram(webtextCorpus)
triGram_Brown = TriGram(brownCorpus)
triGram_Webtext = TriGram(webtextCorpus)

    # corpora = Corpora()

    # brownCorpus = corpora.GetCorpus(brown)
    # webtextCorpus = corpora.GetCorpus(webtext)
    # reutersCorpus = corpora.GetCorpus(reuters)

    # biGram_Brown = BiGram(brownCorpus)
    # biGram_Webtext = BiGram(webtextCorpus)

    # triGram_Brown = TriGram(brownCorpus)
    # triGram_Webtext = TriGram(webtextCorpus)

    # print(triGram_Brown.PredictNextWord("He", "said"))
    # print(triGram_Brown.PredictNWords("He", "said", 10))

    # perplexityBi = PerplexityScore(biGram_Brown)

    # print(f"Perplexity BiGram: {perplexityBi.GetScore(reutersCorpus[0])}")

    # perplexityTri = PerplexityScore(triGram_Brown)

    # print(f"Perplexity TriGram: {perplexityTri.GetScore(reutersCorpus[0])}")

############### FUNCTIONS AS REQUESTED IN THE ASSIGNMENT ###############

# Function to get the Unigram Probability of a word

def prob(word: str):
    choice = int(input('Enter 1 for Brown and 2 for WebText: '))
    model = GetModel((choice, 1))

    return model.UniGramProbability(word)
    
# Functions to get Bigrams & Trigrams in a sentence

def GetBigramsInSentence(sentence: str):
    model = GetModel((1, 1)) # Gives a BiGram Model

    return model.GetBigramsForASentence(sentence)

def GetTrigramsInSentence(sentence: str):
    model = GetModel((1,2)) # Gives a TriGram Model
    return model.GetTrigramsForASentence(sentence)

# Function Conditional Probability BiGram
def GetConditionalProbability(firstWord, secondWord):
    choice = int(input('Enter 1 to use Brown corpus and 2 for WebText: '))
    model = GetModel((choice, 1))

    return model.ConditionalProbabilityBiGram(firstWord, secondWord)

def GetConditionalProbability(firstWord, secondWord, thirdWord):
    choice = int(input('Enter 1 to use Brown corpus and 2 for WebText: '))
    model = GetModel((choice, 2))
    return model.ConditionalProbabilityTriGram(firstWord, secondWord, thirdWord)

# Function to Predict Next word BiGram
def GetNextWordBiGram(word:str):
    choice = int(input('Enter 1 to use Brown corpus and 2 for WebText: '))
    model = GetModel((choice, 1))

    return model.PredictNextWord(word)

def GetNextWordTriGram(firstWord:str, secondWord:str):
    choice = int(input('Enter 1 to use Brown corpus and 2 for WebText: '))
    model = GetModel((choice, 2))

    return model.PredictNextWord(firstWord, secondWord)

# Function to Generate N Words BiGram
def GenerateNWordsBiGram(word:str, n:int):
    choice = int(input('Enter 1 to use Brown corpus and 2 for WebText: '))
    model = GetModel((choice, 1))

    return model.PredictNWords(word, n)

def GenerateNWordsTriGram(firstWord, secondWord, n):
    choice = int(input('Enter 1 to use Brown corpus and 2 for WebText: '))
    model = GetModel((choice, 2))

    return model.PredictNWords(firstWord, secondWord, n)

def GetChoices():
    
    corpus_no = int(input("Enter , 1 for Brown, 2 for WebText"))
    model_no = int(input("Enter,  1 for Bigram 2 for Trigram"))
    print('Wrong choice will default to Trigram Model with WebText')

    return (corpus_no, model_no)

def GetModel(choice = None):

    if choice is None:
        choice = GetChoices()
    model = None

    if  choice == (1,1):
        model = biGram_Brown
    elif choice == (1,2):
        model = triGram_Brown
    elif choice == (2,1):
        model = biGram_Webtext
    else:
        model = triGram_Webtext

    return model

def AveragePerplixity(ps, indxs):
    perplixity = 0
    for indx in indxs:
        perplixity += ps.GetScore(reutersCorpus[indx])
    
    return perplixity / len(indxs)


def main():
    ###### Question 1 Block ######
    print("\n \nQuestion 1: \n Finding Unigram Probability of a Word\n \n")
    word = input("Enter Word: ")
    print(f"Unigram Probability of the word is : {prob(word):.5f}")
    ###### Question 1 Block End ######

    ###### Question 2 BiGram Block ######
    print('\n\n Question 2: BiGram Functions \n \n')

    ######
    sentence = input('Q2 (i) \nEnter the Sentence to get Bigrams: ')
    print(f"Bigrams are: {GetBigramsInSentence(sentence)} \n")
    ######

    ######
    twoWords = input('Q2 (ii) \n Enter Two words (seperated by space) to get thier conditional prob: \n')
    firstWord, secondWord = twoWords.split(' ')
    prob = GetConditionalProbability(firstWord, secondWord)
    print(f"The Conditional Prob of ({firstWord}, {secondWord}) is {prob:.5f}.")
    ######

    ######
    word = input("Q2 (iii) \nEnter The word to get next word")
    print(f"The next word is: {GetNextWordBiGram(word)}")
    ######

    ######
    word = input('Q2 (iv) \nEnter First to start sentence Generation')
    n = int(input('Enter number or words to predict: '))
    print(f"\nSentence: {GenerateNWordsBiGram(word, n)}")
    ######

    ##### Question 2 TriGram Block ######
    print('\n\n Question 2: TriGram Functions \n \n')

    ######
    sentence = input('Q2 (i) \nEnter the Sentence to get TriGrams: ')
    print(f"Bigrams are: {GetTrigramsInSentence(sentence)} \n")
    ######

    ######
    threeWords = input('Q2 (ii) \n Enter Three words (seperated by space) to get thier conditional prob: \n')
    firstWord, secondWord, thirdWord = threeWords.split(' ')
    prob = GetConditionalProbability(firstWord, secondWord, thirdWord)
    print(f"The Conditional Prob of ({firstWord}, {secondWord}, {thirdWord}) is {prob:.5f}.")
    ######

    ######
    word = input("Q2 (iii) \nEnter Two words separated by space to get next word")
    firstWord, secondWord = word.split(' ')
    print(f"The next word is: {GetNextWordTriGram(firstWord, secondWord)}")
    ######

    ######
    word = input("Q2 (iv) \Enter First Two words to start sentence Generation")
    firstWord, secondWord = word.split(' ')
    n = int(input('Enter number or words to predict: '))
    print(f"\nSentence: {GenerateNWordsTriGram(firstWord, secondWord, n)}")
    ######

    ######
    while True:
        print('\n \n Perplexity Score')
        choice = GetChoices()
        model = GetModel(choice)

        sentence = input('Enter sample sentence to find Perplexity')
        ps = PerplexityScore(model)

        print(f"Perplexity Score: {ps.GetScore(sentence):.2f}")

        inp = input('Enter y/n to continue/stop:')
        if inp == 'n':
            break
    ######

    ######
    print("Average Perplexity on Reuters, by picking 25 random sentences:")
    idxs = random.sample(range(len(reutersCorpus)), 25)

    model = GetModel((1,1)) # Brown BiGram 
    ps = PerplexityScore(model)
    print(f"Brown BiGram: {AveragePerplixity(ps, idxs)}")

    model = GetModel((2,1)) # WebText BiGram 
    ps = PerplexityScore(model)
    print(f"WebText BiGram : {AveragePerplixity(ps, idxs)}")

    model = GetModel((1,2)) # Brown TriGram 
    ps = PerplexityScore(model)
    print(f"Brown TriGram: {AveragePerplixity(ps, idxs)}")

    model = GetModel((2,2)) # WebText TriGram 
    ps = PerplexityScore(model)
    print(f"WebText TriGram : {AveragePerplixity(ps, idxs)}")
    ######







    

if __name__ == '__main__':
    main()