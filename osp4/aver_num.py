#!/usr/bin/python


n = int(input("How many numbers are you entering? "))
print("Enter numbers...")

nums = []
for _ in range(n):
	nums.append(int(input()))

sum = 0
for i in range(n):
	sum += nums[i]

avg = sum / n
print("average : ", avg)

