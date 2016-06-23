.. _admin:

===========================
Using with the Django admin
===========================

:class:`~enumchoicefield.fields.EnumChoiceField`\s
are compatible with the Django admin out of the box,
with one exception. If you want to use a
:class:`~enumchoicefield.fields.EnumChoiceField`
in a :attr:`~django.contrib.admin.ModelAdmin.list_filter`, you need to use the
:class:`~enumchoicefield.admin.EnumListFilter`.

.. autoclass:: enumchoicefield.admin.EnumListFilter

