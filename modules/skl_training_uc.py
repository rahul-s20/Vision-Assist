from mongoengine import connect, Q
from schemas.user_commands import UserCommands
import pandas as pd
from brain_cell.skl_model import train_existing_model

connect(host='mongodb://localhost:27017/vision_dev')

print('Connected to DB')


def fetch_user_commands(user_id: str):
    data = UserCommands.objects.filter(Q(acct_holder=user_id) & Q(is_active=True)).all()
    list_data = [{'question': d.command, 'answer': d.target} for d in data]
    df_data = pd.DataFrame(list_data, dtype='string')
    return df_data


def main_train():
    data = fetch_user_commands(user_id='12345')
    x = train_existing_model(data_df=data)
    if x:
        print("Training completed")
    else:
        raise ValueError("Something went wrong")


def main_train_txt(data):
    x = train_existing_model(data_df=data)
    if x:
        print("Training completed")
    else:
        raise ValueError("Something went wrong")
