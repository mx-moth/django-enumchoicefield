Welcome to Django EnumChoiceField's documentation!
==================================================

For a quick example, check out the code below:

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


Contents:

.. toctree::
   :maxdepth: 1

   setup
   usage
   field
   enum
   queries
   admin
