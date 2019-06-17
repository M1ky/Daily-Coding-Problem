'''
Given an array of size N-1 and given there are numbers from 1 to N with
one element missing, the missing number is to be found.
'''

def find_missing_number_in_array(arr):
	'''
	Time complexity: O(n)
	Space complexity: O(1)
	arr - array: int
	'''

	# sum all numbers in size N
	target_sum = sum(i for i in range(1, len(arr)+2))

	# subtract each element of array from target sum
	for i in test:
		target_sum -= i

	# return what's left
	return target_sum




test = [1,2,4,5]
print(find_missing_number_in_array(test))