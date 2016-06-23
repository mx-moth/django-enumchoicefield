from django.test import SimpleTestCase
from django.utils import six

from enumchoicefield.enum import DeconstructableEnum, PrettyEnum


class EnumTests(SimpleTestCase):

    def test_pretty_enum(self):
        class MyEnum(PrettyEnum):
            foo = "Foo"
            bar = "Bar"
            baz = "Baz Quux"

        # Ensure names are set
        self.assertEqual(six.text_type(MyEnum.foo), "Foo")
        self.assertEqual(six.text_type(MyEnum.bar), "Bar")
        self.assertEqual(six.text_type(MyEnum.baz), "Baz Quux")

        # Ensure values are automatically generated
        if six.PY3:
            # In Python3, values are numbered in order
            self.assertEqual(MyEnum.foo.value, 1)
            self.assertEqual(MyEnum.bar.value, 2)
            self.assertEqual(MyEnum.baz.value, 3)

            self.assertEqual(MyEnum(2), MyEnum.bar)
        else:
            # In Python2, values are ordered arbitarily
            self.assertEqual(
                {1, 2, 3}, set(member.value for member in MyEnum))

    def test_extended_pretty_enum(self):
        class MyEnum(PrettyEnum):
            foo = ("Foo", 10)
            bar = ("Bar", 20)
            baz = ("Baz Quux", 40)

            def __init__(self, name, number):
                # TODO Work out if super() can be used through mad haxs
                PrettyEnum.__init__(self, name)
                self.number = number

        # Make sure names still work
        self.assertEqual(six.text_type(MyEnum.foo), "Foo")
        self.assertEqual(six.text_type(MyEnum.bar), "Bar")
        self.assertEqual(six.text_type(MyEnum.baz), "Baz Quux")

        # Ensure the extra data is included
        self.assertEqual(MyEnum.foo.number, 10)
        self.assertEqual(MyEnum.bar.number, 20)
        self.assertEqual(MyEnum.baz.number, 40)

    def test_deconstrubable_enum(self):
        class MyEnum(DeconstructableEnum):
            foo = 1
            bar = 2
            baz = 3

        # This should be a 3-tuple of: python path to module, constructor args,
        # and constructor kwargs. Enum(1) will get the Enum value with a value
        # of 1, which is close enough to a constructor with arguments...
        self.assertEqual(MyEnum.foo.deconstruct(), (
            "enumchoicefield.tests.test_enum.MyEnum",
            (MyEnum.foo.value,),
            {}))
