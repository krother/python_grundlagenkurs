
Block Cipher
============

In this chapter you will:
-------------------------

======= ====================================
area    topic
======= ====================================
🚀      implement a transposition cipher
⚙       slice lists and strings
💡      use the ``join`` method of the ``string`` data type
🔀      use a loop variable for indexing
🔀      use indexing to re-arrange a list
======= ====================================


Indexing and Slicing
--------------------

Strings and lists are both ordered sequences of elements.
In both, you can address elements by their position.
However, Python is counting differently than humans:

.. figure:: indexing.png
   :alt: Indexing


Exercise 1: Indexing lists
--------------------------

What do the following expressions result in?

.. code:: python3

   numbers = [1, 4, 9, 16, 25, 36]

   numbers[4]
   movies[0]
   movies[-1]
   numbers[-3]


Exercise 2: Slicing strings
---------------------------

What do the following commands result in?

   name = "hello world"

   name[5:]
   name[5:10]
   name[:10:2]
   numbers[2:-2]
   numbers[::2]

Exercise 3: Ranges
------------------

Use ``list(range())`` to create the following lists:

.. code:: python3

   [4, 7, 9, 12, 15]

   [10, 20, 30, 40, 50, 60]

   [33, 32, 31, 30]


Exercise 4: Decypher
--------------------

The following text contains an encrypted word:

.. code:: python3

   name = "CSAIPRALKAINACZEYLVOST"

Print every second character, starting with the 2nds.


Exercise 5: Slicing puzzle
--------------------------

Use the expressions to modify the list as indicated. Use each expression
once.

.. figure:: list_funcs1.png
   :alt: list funcs exercise1


Exercise 6: Blocks
------------------

The following code is creating the first two blocks for a `transposition cipher <https://en.wikipedia.org/wiki/Transposition_cipher>`__ .
Complete the code by creating the other two blocks as well.

.. code:: python3

   message = "MEETINGATDAWNATTHEBRIDGE"

   block1 = message[0::4]
   block2 = message[1::4]
   ___
   ___
   encrypted = block1 + block2 + block3 + block4


Exercise 7: Transposition Cipher
--------------------------------

Complete the program that encrypts a text using a transposition cipher:

.. code:: python3

   message = input("enter the text to encrypt: ")
   encrypted = ""
   for start in range(4):
       ___

Exercise 8: Decrypt
-------------------

Write a program to decrypt an encrypted message again.


Exercise 9: Encryption Key
--------------------------

Use an encryption key like ``2031`` that specifies a new order for the blocks.
Implement the following:

1. create an empty list
2. create the blocks as above and add them to the list
3. go through each position of the encryption key
4. select the block with the index given by the digit from the key (convert it to int)
5. add the block to the result string


Reflection questions
--------------------

- what is indexing?
- what do the three numbers in *slicing* do?
- what do you think about the transposition cipher. Is it secure?
- how could you decrypt a transposition cipher without the key?