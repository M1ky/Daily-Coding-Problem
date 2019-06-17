'''
Given an array of integers, return a new array such that each element at index i of the new array 
is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

import time
from functools import reduce

def product_elements_arr(arr):

	solution = []

	for i in range(len(arr)):
		temp_multiple = 1

		for j in range(len(arr)):
			temp_multiple *=  arr[j]

		# temp multiple will currently store product of all values in arr
		# '//' sign will return int from division ('/ returns float which for huge numbers raises OverflowError')
		temp_multiple = temp_multiple // arr[i]
		solution.append(int(temp_multiple))

	return solution


def product_elements_arr2(arr):

	solution = []

	for i in range(len(arr)):
		temp_multiple = 1

		for j in range(len(arr)):
			temp_multiple =  [x for z,x in enumerate(arr) if z!=i]

		solution.append(int(reduce(lambda x,y: x*y, temp_multiple)))

	return solution


# arr = [1, 2, 3, 4, 5]
arr = [x for x in range(1, 300)]


# faster solution
t0 = time.time()
product_elements_arr(arr)
t1 = time.time()

print(t1-t0)

t0 = time.time()
product_elements_arr2(arr)
t1 = time.time()

print(t1-t0)




