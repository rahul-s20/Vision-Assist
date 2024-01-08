import pandas as pd
import re
import unicodedata
import string
import tensorflow as tf
from sklearn.model_selection import train_test_split
from keras.layers import TextVectorization


def unicode_to_ascii(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def clean_text(text):
    text = unicode_to_ascii(text.lower().strip())
    text = re.sub(r"i'm", "i am", text)
    text = re.sub(r"\r", "", text)
    text = re.sub(r"he's", "he is", text)
    text = re.sub(r"she's", "she is", text)
    text = re.sub(r"it's", "it is", text)
    text = re.sub(r"that's", "that is", text)
    text = re.sub(r"what's", "that is", text)
    text = re.sub(r"where's", "where is", text)
    text = re.sub(r"how's", "how is", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"can't", "cannot", text)
    text = re.sub(r"n't", " not", text)
    text = re.sub(r"n'", "ng", text)
    text = re.sub(r"'bout", "about", text)
    text = re.sub(r"'til", "until", text)
    text = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub("(\\W)", " ", text)
    text = re.sub('\S*\d\S*\s*', '', text)
    # text = "<start> " + text + " <end>"
    return text


def tokenize(lang):
    lang_tokenizer = tf.keras.preprocessing.text.Tokenizer(filters='')
    lang_tokenizer.fit_on_texts(lang)
    tensor = lang_tokenizer.texts_to_sequences(lang)
    tensor = tf.keras.preprocessing.sequence.pad_sequences(tensor, padding='post')
    return tensor, lang_tokenizer


def remove_tags(sentence):
    return sentence.split("<start>")[-1].split("<end>")[0]


class Preprocessing:
    def __init__(self, dataset_path: str, trn_tst_split: bool = True) -> None:
        self.data = pd.read_csv(dataset_path, sep='\t', names=['question', 'answer'], dtype='string')
        self.questions_list: list = None
        self.answers_list: list = None
        self.full_text: str = None
        self.trn_tst_split = trn_tst_split
        self.input_tensor = None
        self.inp_lang = None
        self.target_tensor = None
        self.targ_lang = None

    def convo_init(self):
        b = {'question': ['Hi', 'Hello', 'how are you', 'how are you doing', ],
             'answer': ['hello', 'hi', "i'm fine. how about yourself?", "i'm fine. how about yourself?"]}
        df2 = pd.DataFrame(b)
        vertical_concat = pd.concat([self.data, df2], axis=0, ignore_index=True)
        return vertical_concat

    def __cleaning__(self) -> None:
        self.data['question'] = self.data['question'].apply(clean_text)
        self.data['answer'] = self.data['answer'].apply(clean_text)

    def __list_separation__(self) -> None:
        self.questions_list = self.data['question'].tolist()
        self.answers_list = self.data['answer'].tolist()

    def __split_test_train__(self, input_tensor, target_tensor):
        input_tensor_train, input_tensor_val, target_tensor_train, target_tensor_val = train_test_split(input_tensor,
                                                                                                        target_tensor,
                                                                                                        test_size=0.2)
        return input_tensor_train, input_tensor_val, target_tensor_train, target_tensor_val

    def __call__(self):
        self.data = self.convo_init()
        # self.__cleaning__()
        # self.__list_separation__()
        # self.input_tensor, self.inp_lang = tokenize(self.questions_list)
        # self.target_tensor, self.targ_lang = tokenize(self.answers_list)
        # input_tensor_train, input_tensor_val, target_tensor_train, target_tensor_val = self.__split_test_train__(
        #     self.input_tensor, self.target_tensor)

        return self.data
