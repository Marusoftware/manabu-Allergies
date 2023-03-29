from tortoise.models import Model
from tortoise.fields import UUIDField, CharField, ReverseRelation

class User(Model):
    id = UUIDField(pk=True, description="User ID")
    name = CharField(max_length=1024, description="User short name")
    #fullname = CharField(max_length=1024, default="", description="User long name")
    #is_dev = BooleanField(default=False, description="Is this user developer?")
    email = CharField(max_length=1024, description="User email")
    password = CharField(max_length=1024, null=True, description="User password")
    #otp_key = CharField(max_length=32, null=True, description="OTP Secret Key")
    #otp_recovery = CharField(max_length=6, null=True, description="OTP Recovery Key")
    tokens:ReverseRelation["Token"]

from .auth import Token