.. _usage:

=====
Usage
=====

The following code outlines the most simple usecase of ``EnumChoiceField``:

.. code-block:: python

    from enumchoicefield import ChoiceEnum, EnumChoiceField

    class Fruit(ChoiceEnum):
        apple = "Apple"
        banana = "Banana"
        orange = "Orange"

    class Profile(models.Model):
        name = models.CharField(max_length=100)
        favourite_fruit = EnumChoiceField(Fruit, default=Fruit.banana)


    citrus_lovers = Profile.objects.filter(favourite_fruit=Fruit.orange)


The enumerations should extend the :class:`~enumchoicefield.enum.ChoiceEnum` class.
For each member in the enumeration, their human-readable name should be their value.
This human-readable name will be used when presenting forms to the user.

For more advanced usage, refer to the documentation on
:doc:`/field`, :doc:`/enum`, or :doc:`/queries`.
