import nltk

import utilities

from nltk import NaiveBayesClassifier


def main():
    negative_reviews = utilities.read_file('./data/negativeReview.txt')
    positive_reviews = utilities.read_file('./data/positiveReview.txt')

    words = set()

    for review in negative_reviews:
        words.update(utilities.preprocess_review(review))
    for review in positive_reviews:
        words.update(utilities.preprocess_review(review))

    training = []
    training.extend(utilities.generate_features(negative_reviews,words,'Negative'))
    training.extend(utilities.generate_features(positive_reviews,words,'Positive'))


    classifier = nltk.NaiveBayesClassifier.train(training)    
    users_review = input("Please enter a review to analyze: ")
    result = (utilities.classify(classifier, users_review, words))
    print(result)

if __name__ == "__main__":
    main()