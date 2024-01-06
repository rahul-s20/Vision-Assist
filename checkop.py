# from mongoengine import connect
# from schemas.user_commands import UserCommands
#
# connect(host='mongodb://localhost:27017/vision_dev')
#
# print('Connected to DB')
#
# lis = [
#     {'command': 'please turn on light1.', 'target': 'hh_obj.el_control_func(alias="light1", pin_no="25", is_on="on", url="http://192.168.1.22/")'},
#     {'command': 'please turn off light1.', 'target': 'hh_obj.el_control_func(alias="light1", pin_no="25", is_on="off", url="http://192.168.1.22/")'},
#     {'command': 'please turn on fan1.', 'target': 'hh_obj.el_control_func(alias="fan1", pin_no="27", is_on="on", url="http://192.168.1.22/")'},
#     {'command': 'please turn off fan1.', 'target': 'hh_obj.el_control_func(alias="fan1", pin_no="27", is_on="off", url="http://192.168.1.22/")'}
# ]
# for i in lis:
#     uc_obj = UserCommands(command=i['command'], target=i['target'])
#     uc_obj.save()
#
# print("Done")

import modules.skl_train
# main_train()

# from modules import  skl_train