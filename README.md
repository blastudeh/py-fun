# py-fun

Author: Okum Udeh

A Python project containing a multilingual Calculator and a Collection class.

## Calculator

Supports addition, subtraction, multiplication, division and prime
factorization. Accepts numbers, numeric strings, number names from
zero to nine in English, German, Spanish, Russian and Chinese,
and Roman numerals I to X.

Calculator uses the singleton pattern: repeated calls to Calculator()
return the same object.

## Collection

Each Collection() creates a separate object.

- contains(s, e): count occurrences of e in s.
- zip(s, p): pair items, stopping at the shorter sequence.
- pset(s): return all subsets as tuples, ignoring duplicate input items.
- perm(p): return distinct arrangements as tuples.

## Commands

Run these commands from the project folder inside the development container:

    make install
    make run
    make tests
    make build

## Documentation

Documentation source files are in docs/.
Generated HTML documentation is in docs/_build/html/.

## Tests

Tests are in tests/calculator/ and tests/collection/.
Run make tests to check both components.
