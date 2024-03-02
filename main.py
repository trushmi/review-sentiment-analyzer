import nltk

import utilities

from nltk import NaiveBayesClassifier


def main():
    negativeReview = utilities.read_file('./data/negativeReview.txt')
    positiveReview = utilities.read_file('./data/positiveReview.txt')

    words = set()

    for review in negativeReview:
        words.update(utilities.preprocess_review(review))
    for review in positiveReview:
        words.update(utilities.preprocess_review(review))

    training = []
    training.extend(utilities.generate_features(negativeReview,words,'Negative'))
    training.extend(utilities.generate_features(positiveReview,words,'Positive'))


    classifier = nltk.NaiveBayesClassifier.train(training)    
    users_review = input("Please enter a review to analyze: ")
    result = (utilities.classify(classifier, users_review, words))
    print(result)

if __name__ == "__main__":
    main()