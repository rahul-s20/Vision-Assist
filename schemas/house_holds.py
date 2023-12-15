from mongoengine import Document, StringField, BooleanField
from utils.helper import current_date


class HouseHold(Document):
    pin_no = StringField(required=True)
    alias = StringField(required=True)
    device_url = StringField(required=True)
    acct_holder = StringField(default='12345')
    is_active = BooleanField(default=True)
    timestamp = StringField(max_length=10, default=current_date())

