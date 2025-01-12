
class app:
	def __init__(self):
		self.user_input = ""
		self.num_chars = "0123456789."
		self.op_chars = "*/-+="
		
	def main(self):
		while True:
			self.user_input = input("> ") + '='
			self.split_input_string()
			self.perform_operation('*', lambda a, b: a * b)
			self.perform_operation('/', lambda a, b: a / b)
			self.perform_operation('+', lambda a, b: a + b)
			self.perform_operation('-', lambda a, b: a - b)
			print(f"= {self.user_input[0]}")
			
	def split_input_string(self):
		num_chars = self.num_chars
		op_chars = self.op_chars
		
		split_string = []
		
		tmp = ""
		
		for char in self.user_input:
			tmp_tmplen = len(tmp)
			for num in num_chars:
				if char == num:
					tmp += char
			if tmp_tmplen == len(tmp) and tmp != "":
				tmp = float(tmp)
				split_string.append(tmp)
				tmp = ""
			for op in op_chars:
				if char == op:
					split_string.append(char)
		if split_string[-1] == split_string[-2]:
			split_string.pop(-1)
		self.user_input = split_string
		
	def perform_operation(self, op, func):
		for i in range(len(self.user_input)):
			if self.user_input[i] == op:
				x = func(self.user_input[i - 1], self.user_input[i + 1])
				self.user_input[i - 1] = x
				self.user_input[i] = ""
				self.user_input[i + 1] = ""
				i -= 1
		self.user_input = [i for i in self.user_input if i != ""]
		
if __name__ == "__main__":
	app = app()
	try:
		app.main()
	except KeyboardInterrupt:
		print("\nClosing...")
