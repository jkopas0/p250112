
num_chars = "1234567890."
op_chars = "/*-+"

def main():
	while True:
		user_input = input("> ")
		array = prepare_input(user_input)
		answer = calculate_loop(array)
		print(f"= {answer}")
		
def prepare_input(string):
	accepted_chars = num_chars + op_chars + "()"
	
	split_string = []
	
	for char in string:
		for _char in accepted_chars:
			if char == _char:
				split_string.append(char)
				
	tmp = ""
	tmp_array = []
	
	for char in split_string:
		if char.isdigit() or char == '.':
			tmp += char
		elif char == '-':
			if tmp:
				tmp_array.append(tmp)
				tmp = ""
			tmp_array.append('+')
			tmp += char
		elif char == '(':
			if tmp:
				tmp_array.append(tmp)
				tmp = ""
			tmp_array.append('*')
			tmp_array.append(char)
		elif char == ')':
			if tmp:
				tmp_array.append(tmp)
				tmp = ""
			tmp_array.append(char)
		else:
			if tmp:
				tmp_array.append(tmp)
				tmp = ""
			tmp_array.append(char)
			
	if tmp:
		tmp_array.append(tmp)
	
	split_string = tmp_array
	
	for i in range(len(split_string)):
		try:
			split_string[i] = float(split_string[i])
		except ValueError:
			pass
			
	split_string = [i for i in split_string if not (isinstance(i, str) and '.' in i)]
	
	tmp = []
	tmp_array = []
	
	for i in split_string:
		if i == '(':
			tmp.append(tmp_array)
			tmp_array = []
		
		elif i == ')':
			if tmp:
				last = tmp.pop()
				last.append(tmp_array)
				tmp_array = last
		
		else:
			tmp_array.append(i)
			
	split_string = tmp_array if not tmp else []
	
	split_string = clean_array_loop(split_string)
	
	return split_string
	
def clean_array_loop(array):
	for i in range(len(array)):
		if isinstance(array[i], list):
			array[i] = clean_array_loop(array[i])
	return clean_array(array)
	
def clean_array(array):
	tmp_array = []
	
	for i in array:
		if isinstance(i, float):
			if not tmp_array or isinstance(tmp_array[-1], str):
				tmp_array.append(i)
		
		elif isinstance(i, str) and i in op_chars:
			if tmp_array and isinstance(tmp_array[-1], (float, list)):
				tmp_array.append(i)
				
		elif isinstance(i, list):
			tmp_array.append(i)
				
	if isinstance(tmp_array[-1], str):
		tmp_array.pop(-1)
		
	return tmp_array

def calculate_loop(array):
	for i in range(len(array)):
		if isinstance(array[i], list):
			array[i] = calculate_loop(array[i])
	array = calculate(array, ('*', '/'), (lambda a, b: a * b, lambda a, b: a / b))
	array = calculate(array, ('+', '-'), (lambda a, b: a + b, lambda a, b: a - b))
	return array[0]

def calculate(array, ops, funcs):
	tmp_array = []
	
	for i in range(len(array)):
		if isinstance(array[i], str) and array[i] in ops:
			for j in range(len(ops)):
				if array[i] == ops[j]:
					array[i + 1] = funcs[j](array[i - 1], array[i + 1])
			
		elif isinstance(array[i], str) and array[i] not in ops:
			tmp_array.append(array[i - 1])
			tmp_array.append(array[i])
			
		elif i == len(array) - 1:
			tmp_array.append(array[i])
			
	return tmp_array

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\nClosing...")
