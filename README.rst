======================
Django EnumChoiceField
======================

.. image:: https://travis-ci.org/timheap/django-enumchoicefield.svg?branch=master
    :target: https://travis-ci.org/timheap/django-enumchoicefield
.. image:: https://readthedocs.org/projects/django-enumchoicefield/badge/?version=latest
    :target: https://django-enumchoicefield.readthedocs.io/en/latest/
.. image:: https://badge.fury.io/py/django-enumchoicefield.svg
    :target: https://pypi.org/project/django-enumchoicefield/

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
