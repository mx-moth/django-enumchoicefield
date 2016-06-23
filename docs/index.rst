.. Django EnumChoiceField documentation master file, created by
   sphinx-quickstart on Wed Jun  3 16:17:00 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Django EnumChoiceField's documentation!
==================================================

For a quick example, check out the code below:

.. code:: python

    from enumchoicefield import ChoiceEnum, EnumChoiceField

    class Fruit(ChoiceEnum):
        apple = "Apple"
        banana = "Banana"
        orange = "Orange"

    class Profile(models.Model):
        name = models.CharField(max_length=100)
        favourite_fruit = EnumChoiceField(Fruit, default=Fruit.banana)


    citrus_lovers = Profile.objects.filter(favourite_fruit=Fruit.orange)


Contents:

.. toctree::
   :maxdepth: 1

   setup
   usage
   field
   enum
   queries
   admin



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

