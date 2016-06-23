.. _queries:

===========
ORM Queries
===========

You can filter and search for enum members using standard Django ORM queries.
The following queries demonstrate some of what is possible:

.. code:: python

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

Undefined behaviour
===================

Internally, the enum member is stored as a CharField
using the ``name`` attribute.
Any operation that CharFields support are also supported by an
:class:`~enumchoicefield.fields.EnumChoiceField`.
Not all of these operations make sense,
such as ``contains``, ``gt``, and ``startswith``,
and may not behave in a sensible manner.

Ordering on a :class:`~enumchoicefield.fields.EnumChoiceField` field
will order by the ``name``\s  of the enum members,
which is probably not useful.
It is not possible to order results by
the definition order or the ``value`` of the enum members,
