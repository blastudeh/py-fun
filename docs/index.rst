py-fun documentation
====================

This project provides a multilingual calculator and collection operations.

Calculator
----------

Calculator uses a single shared instance. It supports addition,
subtraction, multiplication, division and prime factorization.
Inputs may be numbers, numeric strings or supported number names.

Factorization accepts positive whole numbers. The factors of 1
form an empty list. Division by zero raises ZeroDivisionError.

.. automodule:: src.calculator.calculator
   :members:
   :undoc-members:

Collection
----------

Each Collection is a separate object.

* contains counts occurrences of an item.
* zip pairs items and stops at the shorter sequence.
* pset returns all subsets as tuples, ignoring duplicate input items.
* perm returns distinct arrangements as tuples.

.. automodule:: src.collection.collection
   :members:
   :undoc-members:

Running and testing
-------------------

Run the calculator examples::

   make run

Run the automated tests::

   make tests

Build the project and this documentation::

   make build
