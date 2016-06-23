.. _enum:

============
Enum classes
============

.. module:: enumchoicefield.enum

.. class:: PrettyEnum

    A :class:`PrettyEnum` makes defining nice, human-readable names
    for enum members easy.
    To use it, subclass :class:`PrettyEnum` and
    declare the enum members with their human-readable name as their value:

    .. code:: python

        class Fruit(PrettyEnum):
            apple = "Apple"
            banana = "Banana"
            orange = "Orange"

    The members' values will be automatically set to ascending integers,
    starting at one.
    In the example above,
    ``Fruit.apple.value`` is ``1``, and
    ``Fruit.orange.value`` is ``3``.


.. class:: DeconstructableEnum

    .. py:method:: deconstruct()

        a :class:`DeconstructableEnum` defines :meth:`deconstruct`,
        compatible with Django migrations.
        If you want to set a default for an
        :class:`~enumchoicefield.fields.EnumChoiceField`,
        the enum must be deconstructable.


.. class:: ChoiceEnum

    a :class:`ChoiceEnum` extends both
    :class:`PrettyEnum` and :class:`DeconstructableEnum`.
    It is recommended to use a :class:`ChoiceEnum` subclass with
    :class:`~enumchoicefield.fields.EnumChoiceField`,
    but this is not required.
