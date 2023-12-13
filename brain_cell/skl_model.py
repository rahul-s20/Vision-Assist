from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
import string
import joblib


def cleaner(x):
    return [a for a in (''.join([a for a in x if a not in string.punctuation])).lower().split()]


def train(data_df):
    Pipe = Pipeline([
        ('bow', CountVectorizer(analyzer=cleaner)),
        ('tfidf', TfidfTransformer()),
        ('classifier', DecisionTreeClassifier())
    ])
    Pipe.fit(data_df['question'], data_df['answer'])
    joblib.dump(Pipe, 'nuron_saved_models/skl_chat.joblib')
    return True


def predict(input_str: str):
    load_model = joblib.load('nuron_saved_models/skl_chat.joblib')
    y = load_model.predict([input_str])[0]
    return y
