import importlib.metadata

from .enum import ChoiceEnum
from .fields import EnumChoiceField

__all__ = ['ChoiceEnum', 'EnumChoiceField', 'version']

version = importlib.metadata.version('django-enumchoicefield')
