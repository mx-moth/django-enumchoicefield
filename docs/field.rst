.. _field:

===============
EnumChoiceField
===============

.. module:: enumchoicefield.fields

.. class:: EnumChoiceField(enum_class, ...)

    Create an EnumChoiceField. This field generates choices from an ``enum.Enum``.

    The ``EnumChoiceField`` extends ``Field``.
    It accepts one additional argument:
    ``enum_class``, which should be a subclass of :class:`~enum.Enum`.
    It is recommended that this Enum subclasses
    :class:`~enumchoicefield.enum.ChoiceEnum``,
    but this is not required.

    When saving Enum choices to the database, The chosen enum value is stored
    in the database using its ``name`` attribute. This keeps the database
    representation stable when adding and removing enum values.

    A ``max_length`` is automatically generated from the Enum ``name``
    attributes. If you add a new, longer Enum value, or remove the longest Enum
    value, the generated ``max_length`` will change. To prevent this, you can
    supply a ``max_length`` as normal, and this will be used instead.

    If a default choice is supplied, the Enum class must have a ``deconstruct``
    method. If your Enum inherits from
    :class:`~enumchoicefield.enum.DeconstructableEnum`, this will be handled
    for you.

    The display value for the Enums is taken from the ``str`` representation of
    each value. By default this is something like ``MyEnum.foo``, which is not
    very user friendly. :class:`~enumchoicefield.enum.PrettyEnum` makes
    defining a human-readable ``str`` representation easy.
