from django.test import TestCase

from .models import (
    ChoiceModel, NullableChoiceModel, DefaultChoiceModel, MyEnum)


class EnumTestCase(TestCase):
    def test_saving(self):
        instance = ChoiceModel(choice=MyEnum.foo)
        instance.save()
        self.assertEqual(instance.choice, MyEnum.foo)

    def test_loading(self):
        ChoiceModel.objects.create(
            choice=MyEnum.bar)

        instance = ChoiceModel.objects.get()
        self.assertEqual(instance.choice, MyEnum.bar)

    def test_modifying(self):
        ChoiceModel.objects.create(
            choice=MyEnum.bar)
        instance = ChoiceModel.objects.get()
        self.assertEqual(instance.choice, MyEnum.bar)
        instance.choice = MyEnum.foo
        instance.save()

        instance = ChoiceModel.objects.get()
        self.assertEqual(instance.choice, MyEnum.foo)

    def test_null_saving(self):
        instance = NullableChoiceModel()
        instance.save()
        self.assertIsNone(instance.choice)

    def test_null_loading(self):
        NullableChoiceModel.objects.create()
        instance = NullableChoiceModel.objects.get()
        self.assertIsNone(instance.choice)

    def test_null_clearing(self):
        NullableChoiceModel.objects.create(choice=MyEnum.foo)
        instance = NullableChoiceModel.objects.get()
        self.assertEqual(instance.choice, MyEnum.foo)

        instance.choice = None
        instance.save()

        instance = NullableChoiceModel.objects.get()
        self.assertIsNone(instance.choice)

    def test_default(self):
        instance = DefaultChoiceModel()
        self.assertEqual(instance.choice, MyEnum.baz)

    def test_default_create(self):
        DefaultChoiceModel.objects.create()
        instance = DefaultChoiceModel.objects.get()
        self.assertEqual(instance.choice, MyEnum.baz)

    def test_deconstruct(self):
        self.assertEqual(
            ChoiceModel._meta.get_field('choice').deconstruct(),
            ('choice', 'enumchoicefield.fields.EnumChoiceField', [], {
                'enum_class': MyEnum,
                'max_length': 3}))


class TestQuery(TestCase):
    def setUp(self):
        self.foo = ChoiceModel.objects.create(choice=MyEnum.foo)
        self.bar = ChoiceModel.objects.create(choice=MyEnum.bar)
        self.baz = ChoiceModel.objects.create(choice=MyEnum.baz)

    def test_exact(self):
        self.assertEqual(
            self.foo,
            ChoiceModel.objects.get(choice=MyEnum.foo))

    def test_in(self):
        self.assertQuerysetEqual(
            ChoiceModel.objects.filter(choice__in=[MyEnum.bar, MyEnum.baz]),
            [self.bar, self.baz], transform=lambda x: x)
