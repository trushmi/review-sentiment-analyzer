# Review Sentiment Analyzer
# In this ReadMe:
- [About this project](#about-this-project)
- [Features](#features)
- [Tech stack](#tech-stack)
- [How to run the app](#how-to-run-the-app)
- [Future Enhancements](#future-enhancements)

## About this project:

Review Sentiment Analyzer is a Python-based project that utilizes **Natural Language Processing (NLP)** techniques to analyze and classify customer reviews into 'Positive' or 'Negative' categories. By leveraging the **Naive Bayes classifier** from the **NLTK library**, the project assesses the sentiments conveyed in textual reviews, assisting businesses and individuals to comprehend their customer feedback at a glance.

## Features
- Utilizes NLP techniques to analyze customer reviews.
- Classifies customer reviews into 'Positive' or 'Negative' categories.
- Leverages the Naive Bayes classifier from the NLTK library for sentiment analysis.
- Assists businesses and individuals in understanding customer feedback quickly and effectively.
  
## Tech stack
 - Python
 - Natural Language Processing (NLP)
   
## Files and Directories:

**main.py**: Contains the main script to run the sentiment analysis model.

**utilities.py**: Contains utility functions for data preprocessing, feature generation, and classification.

**positiveReview.txt** and **negativeReview.txt**: Text files that contain examples of positive and negative reviews respectively, used for training the classifier.

**requirements.txt**: Lists all necessary Python packages and their versions.

## How to run the app:
  
1. ### Clone the repository:
```

   git clone [repository URL]
```
2.  ### Navigate to the project directory:
```
  cd [project name]

```
3. ### Set up a virtual environment:
```
python3 -m venv venv
```
4. ### Activate virtual environment
```
source venv/bin/activate
```
5. ### Install the required Python packages:
```
pip install -r requirements.txt
```
6. ### Run the Application
```
python3 server.py
```

## Future Enhancements

- The model might be improved by using a larger and more varied dataset for training.
- Integrating additional preprocessing steps, such as lemmatization and negation handling.
- Experimenting with different feature sets and exploring other classification models


## NOTICE

This project uses the Natural Language Toolkit (NLTK) (http://www.nltk.org/) to analyze and categorize review sentiments.

NLTK is open source software. The source code is distributed under the terms of the Apache License Version 2.0.
Please see the LICENSE file for the Apache License.
