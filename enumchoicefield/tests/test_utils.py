from django.db.models import Case, IntegerField, When
from django.test import TestCase

from enumchoicefield.utils import order_enum

from .models import ChoiceModel, MyEnum


class OrderEnumTestCase(TestCase):
    def test_case_when_enum(self):
        """Test sending an Enum class to order_enum"""
        order = order_enum('choice', MyEnum)
        expected = Case(
            When(choice=MyEnum.foo, then=0),
            When(choice=MyEnum.bar, then=1),
            When(choice=MyEnum.baz, then=2),
            default=3,
            output_field=IntegerField())
        self.assertEqual(str(order), str(expected))

    def test_case_when_list(self):
        """Test sending an incomplete list to order_enum"""
        order = order_enum('choice', [MyEnum.baz, MyEnum.bar])
        expected = Case(
            When(choice=MyEnum.baz, then=0),
            When(choice=MyEnum.bar, then=1),
            default=2,
            output_field=IntegerField())
        self.assertEqual(str(order), str(expected))

    def test_ordering_enum(self):
        c_bar = ChoiceModel(pk=1, choice=MyEnum.bar)
        c_baz = ChoiceModel(pk=2, choice=MyEnum.baz)
        c_foo = ChoiceModel(pk=3, choice=MyEnum.foo)
        ChoiceModel.objects.bulk_create([c_bar, c_baz, c_foo])

        qs = ChoiceModel.objects\
            .annotate(choice_order=order_enum('choice', MyEnum))\
            .order_by('choice_order')
        self.assertEqual(list(qs), [c_foo, c_bar, c_baz])

    def test_ordering_list(self):
        """Test ordering by an incomplete list of members."""
        c_bar = ChoiceModel(pk=1, choice=MyEnum.bar)
        c_baz = ChoiceModel(pk=2, choice=MyEnum.baz)
        c_foo = ChoiceModel(pk=3, choice=MyEnum.foo)
        ChoiceModel.objects.bulk_create([c_bar, c_baz, c_foo])

        # MyEnum.baz is not in the list, so should be sorted to the end
        desired_order = [MyEnum.bar, MyEnum.foo]
        qs = ChoiceModel.objects\
            .annotate(choice_order=order_enum('choice', desired_order))\
            .order_by('choice_order')
        self.assertEqual(list(qs), [c_bar, c_foo, c_baz])
