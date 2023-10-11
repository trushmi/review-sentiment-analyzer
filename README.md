## Project Overview:

ReviewSentimentAnalyzer is a Python-based project that utilizes **Natural Language Processing (NLP)** techniques to analyze and classify customer reviews into 'Positive' or 'Negative' categories. By leveraging the **Naive Bayes classifier** from the **NLTK library**, the project assesses the sentiments conveyed in textual reviews, assisting businesses and individuals to comprehend their customer feedback at a glance.

## Files and Directories:

**main.py**: Contains the main script to run the sentiment analysis model.

**utilities.py**: Contains utility functions for data preprocessing, feature generation, and classification.

**positiveReview.txt** and **negativeReview.txt**: Text files that contain examples of positive and negative reviews respectively, used for training the classifier.

**requirements.txt**: Lists all necessary Python packages and their versions.

## Dependencies:

Ensure these packages are installed:

- click==8.1.7
- joblib==1.3.2
- nltk==3.8.1
- regex==2023.10.3
- tqdm==4.66.1

## Installation and Setup:

1. To begin, clone this repository to your local machine.

   - git clone [repository_link]
   - cd [project_directory]

2. Virtual Environment Setup:

   - Establish and activate a virtual environment.
   - $ virtualenv env
   - $ source env/bin/activate # use `env\Scripts\activate` for Windows

3. Install all dependencies

   - Ensure you have Python and PIP installed. Then, install the dependencies via the requirements.txt file:
   - $ pip install -r requirements.txt

4. Download NLTK

   - Ensure you have the NLTK data related to stopwords.
   - import nltk
   - nltk.download('stopwords')

5. Run the Application
   - Ensure that all files (main.py, utilities.py, positiveReview.txt, and negativeReview.txt) are in the same directory and run the following command in your terminal:
   * python main.py

## Utility Functions (utilities.py)

- **read_file(file_path: str)** -> list: Reads a file and returns a list of strings, each string being a review.

- **preprocess_review(review: str)** -> list: Tokenizes and preprocesses the review.
- **generate_features(reviews: list, words: set, label: str)** -> list: Generates feature sets for training the classifier.
- **classify(classifier, s: str, words: set)** -> str: Classifies a given review and prints the probabilities of each sentiment.

## Future Enhancements

- The model might be improved by using a larger and more varied dataset for training.
- Integrating additional preprocessing steps, such as lemmatization and negation handling.
- Experimenting with different feature sets and exploring other classification models

## Contributions

Contributions, bug reports, and feature requests are welcome! Feel free to open an issue or create a pull request.

## NOTICE

This project uses the Natural Language Toolkit (NLTK) (http://www.nltk.org/) to analyze and categorize review sentiments.

NLTK is open source software. The source code is distributed under the terms of the Apache License Version 2.0.
Please see the LICENSE file for the Apache License.
