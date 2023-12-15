from mongoengine import Document, StringField, BooleanField
from utils.helper import current_date


class UserCommands(Document):
    command = StringField(required=True)
    target = StringField(required=False)
    is_active = BooleanField(default=True)
    acct_holder = StringField(default='12345')
    timestamp = StringField(max_length=10, default=current_date())

