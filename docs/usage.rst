.. _usage:

=====
Usage
=====

The following code outlines the most simple usecase of ``EnumChoiceField``:

.. code:: python

    from enumchoicefield import ChoiceEnum, EnumChoiceField

    class Fruit(ChoiceEnum):
        apple = "Apple"
        banana = "Banana"
        orange = "Orange"

    class Profile(models.Model):
        name = models.CharField(max_length=100)
        favourite_fruit = EnumChoiceField(Fruit)


Your enumerations should extend the :class:`~enumchoicefield.enum.ChoiceEnum` class.
For each item in your enumeration, their human-readable name should be their value.
This human-readable name will be used when presenting forms to the user.

For more advanced usage, refer to the documentation on
:doc:`/field` or :doc:`/enum`
