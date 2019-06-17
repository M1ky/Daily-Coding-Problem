'''
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses
so that the resulting parentheses string is valid.

Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.
'''


def min_parentheses_to_add_to_make_valid_string(str):

	count = 0 # how many parentheses we need to add
	stack = []

	for char in str:

		'''
		Add '(' sing to the stack.
		For every ')' check if there is '(' in a stack, if there is delete '(' from stack, else: count += 1
		'''
		if char == ')':
			# additional check, in case something else than '(' occurs in stack
			# if len(stack) > 0 and stack[len(stack) - 1] == '(':

			if len(stack) > 0:
				del stack[len(stack) - 1]
			else:
				count = count + 1
		else:
			stack.append('(')

	# add all that's left in stack to counter
	for char in stack:
		count = count + 1

	return count


test = '(()))())))'
print(min_parentheses_to_add_to_make_valid_string(test))
			