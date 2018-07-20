.. _queries:

===========
ORM Queries
===========

You can filter and search for enum members using standard Django ORM queries.
The following queries demonstrate some of what is possible:

.. code-block:: python

    from enumchoicefield import ChoiceEnum, EnumChoiceField

    class Fruit(ChoiceEnum):
        apple = "Apple"
        banana = "Banana"
        lemon = "Lemon"
        lime = "Lime"
        orange = "Orange"

    class Profile(models.Model):
        name = models.CharField(max_length=100)
        favourite_fruit = EnumChoiceField(Fruit, default=Fruit.banana)


    apple_lovers = Profile.objects.filter(favourite_fruit=Fruit.apple)
    banana_haters = Profile.objects.exclude(favourite_fruit=Fruit.banana)

    citrus_fans = Profile.objects.filter(
        favourite_fruit__in=[Fruit.orange, Fruit.lemon, Fruit.lime])

Ordering
========

Ordering on a :class:`~enumchoicefield.fields.EnumChoiceField` field
will order results alphabetically by the ``name``\s  of the enum members,
which is probably not useful.
To order results by an enum value,
:func:`enumchoicefield.utils.order_enum` can be used.

.. module:: enumchoicefield.utils

.. autofunction:: order_enum

Undefined behaviour
===================

Internally, the enum member is stored as a CharField
using the ``name`` attribute.
Any operation that CharFields support are also supported by an
:class:`~enumchoicefield.fields.EnumChoiceField`.
Not all of these operations make sense,
such as ``contains``, ``gt``, and ``startswith``,
and may not behave in a sensible manner.
