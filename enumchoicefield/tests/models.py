from django.db import models


from enumchoicefield.fields import EnumChoiceField
from enumchoicefield.enum import ChoiceEnum


class MyEnum(ChoiceEnum):
    foo = "Foo"
    bar = "Bar"
    baz = "Baz Quux"


class ChoiceModel(models.Model):
    choice = EnumChoiceField(MyEnum)


class NullableChoiceModel(models.Model):
    choice = EnumChoiceField(MyEnum, null=True, blank=True)


class DefaultChoiceModel(models.Model):
    choice = EnumChoiceField(MyEnum, default=MyEnum.baz)
