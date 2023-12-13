from brain_cell.skl_model import train
from brain_cell.preprocessing import Preprocessing

data = Preprocessing(dataset_path='dataset/dialogs.txt')
res = train(data_df=data())
print("Training completed")