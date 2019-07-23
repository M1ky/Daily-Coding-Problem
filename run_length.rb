=begin

Run-length encoding is a fast and simple method of encoding strings. 
The basic idea is to represent repeated successive characters as a single count and character. 
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. 
You can assume the string to be encoded have no digits and consists solely of alphabetic characters. 
You can assume the string to be decoded is valid.

=end

def encode(str)
	char_stack = []
	out = ''

	str.split("").each do |chr|
		
		# if stack is empty add char to stack
		if char_stack.length == 0
			char_stack << chr
		else
			# if stack is not empty check if new char == last char from stack
			if chr == char_stack[-1]
				# add it to stack
				char_stack << chr
			else
				# add last character in stack * length of stack to output string 
				out = out + char_stack.length.to_s + char_stack[-1]

				# clear the stack
				char_stack = []

				# add newest char to empty stack
				char_stack << chr
			end
		end
	end

	# add remains that are left in stack to output
	out = out + char_stack.length.to_s + char_stack[-1]

	return out
end


def decode(str)

	out = ''

	(0..str.length).step(2) do |x|
		out = out + (str[x+1].to_s * str[x].to_i)
	end

	return out
end

encoded = encode("AAAABBBCCDAA")
puts encoded
puts decode(encoded)
