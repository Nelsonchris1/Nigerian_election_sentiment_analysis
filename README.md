# Sentiment Analysis of Nigerian Presidential Election using Twitter Data

## Introduction
This project is a sentiment analysis of tweets related to the Nigerian presidential election, focusing on the three main presidential candidates. The aim of the project is to analyze the sentiment of Twitter users towards the candidates and determine which candidate is most favored by the Twitter community.

## Requirements
To run this project, you need the following libraries:

snscrape
pandas
numpy
nltk
sklearn
You can install these libraries by running the following command:

```python 
pip install snscrape pandas numpy nltk sklearn
```

## Data Collection
I used snscrape to extract tweets related to the Nigerian presidential election. I collected tweets from Febuary 21st, 2023 to February 24th, 2023. I collected a total of 19,000 tweets for all candidates.

## Data Cleaning
I cleaned the data by removing URLs, special characters, and stopwords using the NLTK library. I also performed stemming and tokenization to reduce the number of unique words in the dataset.

## Sentiment Analysis
I used the TextBlob library to perform sentiment analysis on the cleaned tweets. TextBlob is a Python library for processing textual data, which provides an easy-to-use interface for natural language processing tasks such as sentiment analysis.

I calculated the sentiment score for each tweet, which ranges from -1 (most negative) to +1 (most positive). I then calculated the average sentiment score for each candidate.


References
snscrape: https://github.com/JustAnotherArchivist/snscrape
TextBlob: https://textblob.readthedocs.io/en/dev/



