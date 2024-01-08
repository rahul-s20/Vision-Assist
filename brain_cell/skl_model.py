from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
import string
import joblib
from pandas import DataFrame, concat


def cleaner(x):
    return [a for a in (''.join([a for a in x if a not in string.punctuation])).lower().split()]


def train(data_df: DataFrame):
    Pipe = Pipeline([
        ('bow', CountVectorizer(analyzer=cleaner)),
        ('tfidf', TfidfTransformer()),
        ('classifier', DecisionTreeClassifier())
    ])
    Pipe.fit(data_df['question'], data_df['answer'])
    joblib.dump(data_df, 'nuron_saved_models/skl_chat_data.joblib')
    joblib.dump(Pipe, 'nuron_saved_models/skl_chat.joblib')
    return True


def train_existing_model(data_df: DataFrame):
    existing_model = joblib.load('nuron_saved_models/skl_chat.joblib')
    existing_data = joblib.load('nuron_saved_models/skl_chat_data.joblib')
    concat_data = concat([existing_data, data_df], axis=0, ignore_index=True)
    existing_model.fit(concat_data['question'], concat_data['answer'])
    joblib.dump(concat_data, 'nuron_saved_models/skl_chat_data.joblib')
    joblib.dump(existing_model, 'nuron_saved_models/skl_chat.joblib')
    return True


def predict(input_str: str):
    load_model = joblib.load('nuron_saved_models/skl_chat.joblib')
    y = load_model.predict([input_str])[0]
    return y
