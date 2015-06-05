======================
Django EnumChoiceField
======================

A Django model field for native Python 3.4 Enums.

.. code:: python

    from enumchoicefield import ChoiceEnum, EnumChoiceField

    class Fruit(ChoiceEnum):
        apple = "Apple"
        banana = "Banana"
        orange = "Orange"

    class Profile(models.Model):
        name = models.CharField(max_length=100)
        favourite_fruit = EnumChoiceField(Fruit, default=Fruit.banana)

Documentation
=============

See `Django EnumChoiceField on ReadTheDocs <https://django-enumchoicefield.readthedocs.org/en/latest/>`_.

Testing
=======

To run the tests:

.. code:: sh

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements-dev.txt
    $ tox
