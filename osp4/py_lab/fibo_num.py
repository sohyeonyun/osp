#!/usr/bin/python

n = int(input("fibonacci number? "))

F = [1, 1]
for i in range(2, n):
	F.append(F[i-1] + F[i-2])

print(",".join( repr(e) for e in F ))

print("F%d = %d" % (n, F[n-1]))
