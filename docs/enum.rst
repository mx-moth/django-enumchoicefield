.. _enum:

============
Enum classes
============

.. module:: enumchoicefield.enum

.. class:: PrettyEnum

    A :class:`PrettyEnum` makes defnining nice, human-readable names for your
    Enum values easy. To use it, subclass :class:`PrettyEnum` and define your
    Enum values to be their human-readable name:

    .. code:: python

        class Fruit(PrettyEnum):
            apple = "Apple"
            banana = "Banana"
            orange = "Orange"

    The Enum values will be automatically set to ascending integers, starting
    at one. In the example above, ``Fruit.apple.value`` is ``1``, and
    ``Fruit.orange.value`` is ``3``.


.. class:: DeconstructableEnum

    a :class:`DeconstructableEnum` defines a :func:`deconstruct` method,
    compatible with Django migrations. If you want to set a default for an
    :class:`~enumchoicefield.fields.EnumChoiceField`, your Enum must be
    deconstructable.

.. class:: ChoiceEnum

    a :class:`ChoiceEnum` extends both :class:`PrettyEnum` and
    :class:`DeconstructableEnum`. It is recommended to use a
    :class:`ChoiceEnum` subclass with
    :class:`~enumchoicefield.fields.EnumChoiceField`, but this is not required.
