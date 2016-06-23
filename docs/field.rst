.. _field:

===============
EnumChoiceField
===============

.. module:: enumchoicefield.fields

.. class:: EnumChoiceField(enum_class, ...)

    Create an EnumChoiceField. This field generates choices from an :class:`enum.Enum`.

    The :class:`EnumChoiceField` extends :class:`django.db.models.Field`.
    It accepts one additional argument:
    ``enum_class``, which should be a subclass of :class:`enum.Enum`.
    It is recommended that this enum subclasses
    :class:`~enumchoicefield.enum.ChoiceEnum`,
    but this is not required.

    When saving enum members to the database, The chosen member is stored
    in the database using its ``name`` attribute. This keeps the database
    representation stable when adding and removing enum members.

    A ``max_length`` is automatically generated from the longest ``name``.
    If you add a new enum member with a longer name, or remove the longest member,
    the generated ``max_length`` will change.
    To prevent this, you can manually set a ``max_length`` argument,
    and this will be used instead.

    If a default choice is supplied,
    the enum class must have a ``deconstruct`` method.
    If the enum inherits from :class:`~enumchoicefield.enum.DeconstructableEnum`,
    this will be handled for you.

    The display value for the Enums is taken from
    the ``str`` representation of each value.
    By default this is something like ``MyEnum.foo``,
    which is not very user friendly.
    :class:`~enumchoicefield.enum.PrettyEnum` makes defining
    a human-readable ``str`` representation easy.
