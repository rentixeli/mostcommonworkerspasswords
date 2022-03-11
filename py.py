#!/usr/bin/env python3

list1 = 'abcdefghijklmnopqrstuvwxyz'
numlist = "!@#$%^&*()\"';/.][}{-+"

Doubles = []

for i in range (0, 26):
	for letter in list1:
		capLet = list1[i]
		Doubles.append(capLet.capitalize() + letter)

readyList = []
for i in Doubles:
	for j in numlist:
		readyList.append(i + '123456' + j)

bigList = []
for i in readyList:
	for j in numlist:
		bigList.append(i + j)

finished = []
for i in bigList:
	finished.append(i)
for i in readyList:
	finished.append(i)

for i in finished:
	print(i)
