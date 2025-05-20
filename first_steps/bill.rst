Receipts
========

.. image:: receipts.jpg

Photo by `Carli Jeen on unsplash.com <https://unsplash.com/@carlijeen?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash>`__
 

In this chapter you will:
-------------------------

======= ====================================
area    topic
======= ====================================
🚀      sum up numbers from shopping bills
⚙       loop over a list
💡      use the ``append`` method of the ``list`` data type
🔀      transform a list into a new one
🐞      fix value errors
======= ====================================


Exercise 1
----------

To process larger amounts of data, we cannot invent a new variable name
for every number. 
Instead, we can store multiple number in a **list**.

The program below sums up items on a list.
Complete the code by inserting ``costs``, ``for``, ``item``, ``total``

.. code:: python

   costs = [8, 5, 20, 12, 1]
   total = 0
   ___ item in ___:
       ___ += ___
   print(total)


Exercise 2: List methods
------------------------

Find out what each expression does to the list in the center.

.. figure:: lists.png
   :alt: list exercise


Exercise 3: Add an extra item 
-----------------------------

You have an extra item you need to take into account:

.. code:: python3

   costs = [8, 5, 20, 12, 1]
   extra = 4

Use a list method from exercise 2 to add the extra item to the list.
Then calculate the sum.


Exercise 4: Concatenate
-----------------------

Explain the difference between the following expressions:

::

   [1, 2 + 3, 4]

   [1, 2] + [3, 4]

   ["1", "2" + "3", "4"]

   ["1, 2" + "3, 4"]

   "[1, 2" + "3, 4]"



Exercise 5: Puzzle
------------------

Use the expressions to modify the list as indicated. Use each expression
once.

.. figure:: list_funcs2.png
   :alt: list funcs exercise2


Exercise 6: List transformation
-------------------------------

Sometimes it is useful to create a new list from an existing one.
This is called **transforming** a list.
Order the lines in the following program:

.. code:: python3

   print(total)
   costs = ["8", "5", "20", "12", "1"]
   numbers.append(int(item))
   for item in costs:
   total = sum(numbers)
   numbers = []


Exercise 7: Receipt assistant
-----------------------------

Write a program that sums up shopping bills.
The user enters amounts, one number at a time.
If they enter nothing (an empty string),
the program calculates the total value of the items entered. 

The output of the program could look like this:

::

   Please enter the costs on your bills, one number at a time:
   13
   8
   5
   21

   The total cost of your bills is 47


.. hint::

   You will need a ``while`` loop for entering the numbers.


Reflection Questions
--------------------

-  How can you create a list?
-  How can you add an item to a list?
-  How can you run a for loop over a list?
