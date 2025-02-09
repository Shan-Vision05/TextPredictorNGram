# NGramSentencePredictor  

## Description  
This repository contains a sentence prediction model based on **bigram** and **trigram** language modeling techniques using the **NLTK corpus**. The project leverages **n-gram probabilities** to predict the next word in a given text, utilizing **statistical language modeling**.  

The implementation includes **data preprocessing, tokenization, and frequency analysis** using **NLTK’s built-in corpora**, such as the **Brown, Gutenberg, or WebText corpus**. This project serves as a fundamental introduction to **Natural Language Processing (NLP)** and can be extended to more advanced **Markov models or deep learning approaches**.  

## Dependencies  
- Python 3.x  
- NLTK (`pip install nltk`)  

## Environment  
It is highly recommended to run this project in an **Anaconda environment**:  

`conda activate <your_environment_name>`

## Guide to Run  

The main script to execute the model is **`main.py`**.  

- The `main()` function contains multiple blocks of code, each implementing a different function as per the assignment requirements.  
- To test a specific function, **comment out the other blocks** and keep only the one you need.  

## Running the Script  

You can run the script using:  

`python3 main.py  # If using Python 3 ` 
OR  
`python main.py   # Depending on your Python version` 

This will execute all the required functions sequentially.

## Code Structure  

- **`main.py`** – Entry point of the program, executes different functions.  
- **`model/`** – Contains language models:  
  - **`BiGram.py`** – Implements **bigram model** for prediction & probability calculation.  
  - **`TriGram.py`** – Implements **trigram model** for prediction & probability calculation.  
- **`Perplexity.py`** – Computes a **perplexity score** for a given sentence.  
- **`PreprocessText.py`** – Creates a **corpus** from NLTK datasets for training.  

## Features  
- ✅ **Uses NLTK corpus** for training language models  
- ✅ Implements **bigram** and **trigram** models for prediction  
- ✅ Supports **custom text datasets** for training  
- ✅ Provides **probability-based word predictions**  
- ✅ Clean and modular **Python implementation**  