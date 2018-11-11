#! /usr/bin/python
# class to read file and print no of words and lines in it.

# Read file from Command prompt
import sys

f = open(sys.argv[1], "r")
contents = f.read()


def count_words(content):
    # split sentences with spaces
    word = content.split(" ")
    return len(word)


def count_lines(content):
    # split content based on new line '\n
    lines = content.split("\n")
    i = 0
    for line in lines:
        if len(line) != 0:
            i += 1
    return i


print('Number of words in this file are', count_words(contents))
print('Number of Lines in this file are', count_lines(contents))


f.close()
