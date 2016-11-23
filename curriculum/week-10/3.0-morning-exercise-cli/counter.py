#!/usr/bin/python

from collections import Counter
from re import split


word_list = open("input.txt", 'r')
wordcount = Counter(word_list)

wordcount = {}
for line in word_list:
	
	for word in word_list:
		if word not in wordcount:
			wordcount[word] = 1
		else:
			wordcount[word] += 1

print wordcount

