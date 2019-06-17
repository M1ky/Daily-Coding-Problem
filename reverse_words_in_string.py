'''
Given an input string, reverse the string word by word in linear manner.

Example:
Input: "the sky is blue"
Output: "blue is sky the"

Note:
	A word is defined as a sequence of non-space characters.
	Input string may contain leading or trailing spaces, reversed string should not.
	Reduce multiple spaces between two words to a single space in the reversed string.
'''

def reverse_words_in_string(str):

	start = 0 # iterator for start of word in input str
	end = start # iterator for end of word in input str

	words = [] 

	'''
	Add words, based on start and end iterators
	For every char != ' ' we update only end iterator, 
	For every char == ' ' we update both start and end itarator and if
	end > start we add a word (characters between start and end) to an array words
	'''
	for i in range(len(str)):
		char = str[i]
		if char == ' ':
			if end > start:
				words.append(str[start:end])
			start = end = i+1
		else:
			end = i+1

	# Add last word in a string where char != ' ' is last
	end = len(str)
	if end > start:
		words.append(str[start:end])

	# Format output
	out = []
	for i in range(len(words)-1, -1, -1):
		out.append(words[i])

	return ' '.join(out)


test = ' blue    is the sky      '
print(reverse_words_in_string(test))