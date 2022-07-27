# Chapter 01 - Arrays and Strings

## Hash Tables
According to CtCI:

'A hash table is a data structure that maps keys to values for highly efficient lookup. There are a number of
ways of implementing this. Here, we will describe a simple but common implementation.
In this simple implementation, we use an array of linked lists and a hash co.de function. To insert a key
(which might be a string or essentially any other data type) and value, we do the following:
1. First, compute the keys hash code, which will usually be an int or long. Note that two different keys could have the same hash code, as there may be an infinite number of keys and a finite number of ints.
2. Then, map the hash code to an index in the array. This could be done with something like hash (key) % array_length. Two different hash codes could, of course, map to the same index.
3. At this index, there is a linked list of keys and values. Store the key and value in this index. We must use a linked list because of collisions: you could have two different keys with the same hash code, or two different hash codes that map to the same index.
To retrieve the value pair by its key, you repeat this process. Compute the hash code from the key, and then compute the index from the hash code. Then, search through the linked list for the value with this key.
If the number of collisions is very high, the worst case runtime is O( N), where N is the number of keys.
However, we generally assume a good implementation that keeps collisions to a minimum, in which case the lookup time is a (1).'

I implemented a mixed approach between this description and the next article from realpython.com:
[Build a Hash Table in Python with TDD](https://realpython.com/python-hash-table/)

## Resizable Arrays
In Python exists an Array class but List are mostly used to store a series of items and access it by index.
List are automatically resizable.
Anyway, as an exercise, I implemented an ArrayList class which has a fixed size and doubles it when need more space.

## StringBuilder
In a similar way, Python provides several functions similars to StringBuilder like append(), join() and string concatenation

## Interview Questions

### 1.1 Is Unique
Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
Hints: 44, 117, 132

### 1.2 Check Permutation
Given two strings, write a method to decide if one is a permutation of the other.
Hints: 1, 84, 122, 131

### 1.3 URLify
Write a method to replace all spaces in a string with '%20: You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr John Smith   "
Output: "Mr%20J ohn%20Smith"
Hints: 53, 118
