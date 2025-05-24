Aufgabe 6: Zip
---------------

Simplify the following code using the function ``zip()``:

.. code:: python3

   fruits = ["apple", "banana", "orange", "cherries"]
   prices = [0.5, 1.0, 1.5, 3.0]

   table = []
   i = 0
   while i < len(fruits):
       row = (fruits[i], prices[i])
       table.append(row)
       i += 1
   print(table)

Try the expression:

.. code:: python3

   for a, b in zip(fruits, prices):
       ...
