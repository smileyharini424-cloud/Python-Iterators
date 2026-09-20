# Python Iterators

## Explanation

An iterator is an object that allows elements of a collection to be accessed one at a time. Python provides the `iter()` function to create an iterator and the `next()` function to retrieve the next element.

## Problem Statement

Write a Python program to create an iterator from a list and access its elements one by one using `next()`.

## Features

* Creates a list
* Converts the list into an iterator
* Accesses elements one at a time
* Demonstrates `iter()`
* Demonstrates `next()`
* Handles the end of the iterator

## How It Works

1. A list containing student names is created.
2. The `iter()` function converts the list into an iterator.
3. The `next()` function retrieves each element.
4. When there are no more elements, `StopIteration` is raised.
5. The exception is handled using `try-except`.

## Technologies Used

* Python 3
* Iterators
* `iter()`
* `next()`
* Exception Handling

## Program Flow

Start → Create List → Create Iterator → Get Elements Using `next()` → Handle StopIteration → End

## Sample Input

```text id="xqj9za"
No user input required.
```

## Sample Output

```text id="f1q4ya"
First Element: Harini
Second Element: Anu
Third Element: Ravi
Fourth Element: Kiran
Iterator has no more elements.
```

## Key Learning

* `iter()` creates an iterator from an iterable.
* `next()` retrieves the next element.
* Iterators process elements one at a time.
* `StopIteration` indicates that the iterator has no more elements.
* Iterators are useful for memory-efficient data processing.

## File Location

```text id="0v8q7p"
Python-Iterators/iterators.py
```

## Repository Structure

```text id="4b1r7m"
Python-Iterators/
│
├── iterators.py
└── README.md
```

## Author

V.Harini
