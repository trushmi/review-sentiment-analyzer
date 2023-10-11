from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

stop_words = set(stopwords.words('english'))


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            return file_content.split(",\n")

    except FileNotFoundError:
        print(f"File {file_path} not found!")
        return []

def preprocess_review(review):
    tokenizer = RegexpTokenizer(r"\w+(?:'\w+)?")
    return [x.lower() for x in tokenizer.tokenize(review) if x.lower() not in stop_words]

  
def generate_features(reviews, words, label):
    feature_set = []
    
    for review in reviews:
        processed_words = preprocess_review(review)
        features = {word: (word in processed_words) for word in words}
        feature_set.append((features, label))
    
    return feature_set

def classify(classifier, s, words):
    tokens = preprocess_review(s)
    features = {word: (word in tokens) for word in words}
    label = classifier.classify(features)

    prob_dist = classifier.prob_classify(features)
    prob_negative= f"Probability of Negative: {prob_dist.prob('Negative'):.2f}"
    prob_positive=f"Probability of Positive: {prob_dist.prob('Positive'):.2f}"

    return f"{prob_negative}; {prob_positive}. Final result: {label}" 