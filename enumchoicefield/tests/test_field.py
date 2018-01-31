import json

from django.core import serializers
from django.test import TestCase

from enumchoicefield.forms import EnumField

from .models import (
    ChoiceModel, DefaultChoiceModel, MyEnum, NullableChoiceModel)


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

    def test_value_to_string(self):
        model_field = ChoiceModel._meta.get_field('choice')

        self.assertEqual(
            model_field.value_to_string(ChoiceModel(choice=MyEnum.bar)),
            'bar')
        self.assertEqual(
            model_field.value_to_string(ChoiceModel(choice=None)),
            '')

    def test_seralize(self):
        pk_1 = NullableChoiceModel.objects.create(choice=MyEnum.baz).pk
        pk_2 = NullableChoiceModel.objects.create(choice=None).pk

        serialized = serializers.serialize(
            'json', NullableChoiceModel.objects.all())
        self.assertEqual(
            json.loads(serialized),
            [
                {"model": "tests.nullablechoicemodel", "pk": pk_1, "fields": {
                    "choice": "baz"}},
                {"model": "tests.nullablechoicemodel", "pk": pk_2, "fields": {
                    "choice": None}},
            ])

    def test_formfield(self):
        model_field = ChoiceModel._meta.get_field('choice')
        form_field = model_field.formfield()
        self.assertIsInstance(form_field, EnumField)
        self.assertIs(form_field.enum, model_field.enum)


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
