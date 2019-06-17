'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

'''

import random
import time

def target_sum(arr, target):
	# sort array
	arr = sorted(arr)

	start_iterator = 0
	end_iterator = len(arr)-1


	while start_iterator < end_iterator:
		temp = arr[start_iterator] + arr[end_iterator]

		if temp == target:
			return True
		elif temp < target:
			start_iterator += 1
		else:
			end_iterator -= 1

	return False


def target_sum2(arr, target):
	# put all numbers in a hashmap
	number_set = set(arr)

	# check for numbers in arr if target(number) exist in a hasmap
	for num in arr:
		if target - num in number_set:
			return True
	return False


arr = [x for x in range(1000000)]
random.shuffle(arr)
# print(arr)
target = 94577


t0 = time.time()
print(target_sum(arr, target))
t1 = time.time()

print(t1-t0)

t0 = time.time()
print(target_sum2(arr, target))
t1 = time.time()

print(t1-t0)