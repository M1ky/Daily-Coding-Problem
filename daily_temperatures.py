'''

Given a list of daily temperatures T, return a list such that, for each day in the input,
tells you how many days you have to wait until the temperature will be warmer.
If there is no such day, put 0.

'''


def days_till_warmer_temperature(arr):

	# table holding solution
	out = [0]*len(arr)

	stack = []

	for index in range(len(arr)):
		temperature = arr[index]

		while len(stack) > 0 and arr[stack[-1]] < temperature:
			oldIndex = stack[-1]

			if temperature > arr[oldIndex]:
				out[oldIndex] = index - oldIndex
				stack.pop()
			else:
				break
		stack.append(index)

	return out


test = [73, 74, 75, 71, 69, 72, 76, 73]
print(days_till_warmer_temperature(test))