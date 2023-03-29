from tortoise.models import Model
from tortoise.fields import UUIDField, CharField, ReverseRelation

class User(Model):
    id = UUIDField(pk=True, description="User ID")
    name = CharField(max_length=1024, description="User short name")
    email = CharField(max_length=1024, description="User email")
    password = CharField(max_length=1024, null=True, description="User password")
    tokens:ReverseRelation["Token"]

from .auth import Token