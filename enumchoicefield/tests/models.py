from django.db import models

from enumchoicefield.enum import ChoiceEnum
from enumchoicefield.fields import EnumChoiceField


class MyEnum(ChoiceEnum):
    __order__ = 'foo bar baz'
    foo = "Foo"
    bar = "Bar"
    baz = "Baz Quux"


class BaseModel(models.Model):
    class Meta:
        abstract = True
        ordering = ('id',)


class ChoiceModel(BaseModel):
    choice = EnumChoiceField(MyEnum)

    def __str__(self):
        return '{} chosen'.format(self.choice)


class NullableChoiceModel(BaseModel):
    choice = EnumChoiceField(MyEnum, null=True, blank=True)


class DefaultChoiceModel(BaseModel):
    choice = EnumChoiceField(MyEnum, default=MyEnum.baz)
