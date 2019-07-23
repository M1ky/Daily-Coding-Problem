'''

Given an array of integers and a number k, where 1 <= k <= length of the array, 
compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. 
You can modify the input array in-place and you do not need to store the results. 
You can simply print them out as you compute them.

'''

import time
import random

def max_value_of_subarrays_brute(arr, k):
	output = [] # array storing results
	compute = [] # array storing subarray - changes in every iteration


	# add numbers from arr in length k to array compute
	for i in range(len(arr)-k+1):
		for j in range(i, k+i):
			compute.append(arr[j])

		# add maximum number in compute to output
		output.append(max(compute))

		# clear array
		compute = []

	return output


class Queue():
	def help(self):
		print('''
			Class representing a Queue
			''')

	def __init__(self):
		self.items = []

	def enqueue(self, item):
		# inserts item into the first position at the que
		self.items.insert(0, item)

	def dequeue(self):
		# as long as que is not empty
		if not self.is_empty():
			# return the top item
			return self.items.pop()

	def is_empty(self):
		# returns true if queue is empty (so it's len == 0)
		return len(self.items) == 0

	def peek(self):
		if not self.is_empty():
			return self.items[-1].value

	def __len__(self):
		# overide the len function
		return self.size()

	def size(self):
		return len(self.items)

	def print_queue(self):
		for i in self.items:
			print(i)

	def max(self):
		return max(self.items)


def max_value_of_subarrays_queue(arr, k):
	que = Queue() # create a queue
	output = [] # array storing outputs

	# for each element in input array add it to queue
	for i in range(len(arr)):

		# if queue is not of length k add element to queue
		if len(que) != k:
			que.enqueue(arr[i])

		else:
			output.append(que.max()) # add max element in queue to output
			que.dequeue() # remove first element from queue
			que.enqueue(arr[i]) # add new element to queue


	output.append(que.max()) # add last max element in queue to output
	
	return output



test = [int(1000*random.random()) for i in range(100000)]
# test = [10, 5, 6, 10, 8, 9, 10]

t1 = time.time()
max_value_of_subarrays_queue(test, 3)
max_value_of_subarrays_queue(test, 2)
max_value_of_subarrays_queue(test, 4)
t2 = time.time()

# time result
print(t2-t1)


t1 = time.time()
max_value_of_subarrays_brute(test, 3)
max_value_of_subarrays_brute(test, 2)
max_value_of_subarrays_brute(test, 4)
t2 = time.time()

# time result
print(t2-t1)

