#!/usr/bin/python

#union/intersection

def operation():
	line1 = input("1st list: ")
	line2 = input("2nd list: ")

	splitted1 = line1.replace("]", "").replace('[', '').replace(",", " ").split()
	splitted2 = line2.replace("]", "").replace("[", "").replace(",", " ").split()

	split = list(splitted1 + splitted2)

	#union operation
	union = list(set(split))
	print("=> union ", sorted(list(map(int, union))))

	#intersection operation
	D = dict()
	inter = []
	for word in union:
		D[word] = split.count(word)
	for key, value in D.items():
		if (value != 1):
			inter.extend(key)

	print("=> intersection ", sorted(list(map(int, inter))))

