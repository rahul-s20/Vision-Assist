from brain_cell.skl_model import train_existing_model
from brain_cell.preprocessing import Preprocessing

data = Preprocessing(dataset_path='dataset/chatbot_dataset.txt')

res = train_existing_model(data_df=data())
print("Re Training completed")