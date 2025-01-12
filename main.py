
class app:
	def __init__(self):
		self.user_input = ""
		self.num_chars = "0123456789."
		self.op_chars = "*/-+^=()"
		self.previous_calculation = 0.0
		
	def main(self):
		while True:
			self.user_input = input("> ") + '='
			if not self.split_input_string():
				print("No input has been provided.")
				continue
			if self.handle_parentheses(0) == -1:
				print("Could not calculate.")
				continue
			try:
				self.previous_calculation = self.user_input[0]
				print(f"= {self.user_input[0]}")
			except IndexError:
				print("Could not calculate.")
			
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
		try:
			while split_string[-1] == '=':
				split_string.pop(-1)
		except IndexError:
			return False
		self.user_input = split_string
		return True
		
	def handle_parentheses(self, pos):
		pos_start = pos
		end = len(self.user_input)
		
		tmp = []
		
		while pos < end:
			if self.user_input[pos] == '(':
				self.user_input.pop(pos)
				pos = self.handle_parentheses(pos)
				if pos == -1: return -1
			elif self.user_input[pos] == ')':
				self.user_input.pop(pos)
				return self.handle_operatins(pos_start, pos)
			end = len(self.user_input)
			pos += 1
		return self.handle_operations(pos_start, pos)
		
	def handle_operations(self, pos_start, pos):
		if not self.perform_operation('^', pos_start, pos - 1, lambda a, b: a ** b): return -1
		if not self.perform_operation('*', pos_start, pos - 1, lambda a, b: a * b): return -1
		if not self.perform_operation('/', pos_start, pos - 1, lambda a, b: a / b): return -1
		if not self.perform_operation('+', pos_start, pos - 1, lambda a, b: a + b): return -1
		if not self.perform_operation('-', pos_start, pos - 1, lambda a, b: a - b): return -1
		self.user_input = [i for i in self.user_input if i != ""]
		return pos_start
		
	def perform_operation(self, op, pos, pos_end, func):
		try:
			while pos < pos_end:
				if self.user_input[pos] == op:
					x = func(self.user_input[pos - 1], self.user_input[pos + 1])
					self.user_input[pos - 1] = x
					self.user_input[pos] = ""
					self.user_input[pos + 1] = ""
				pos += 1
			return True
		except TypeError:
			return False
			
if __name__ == "__main__":
	app = app()
	try:
		app.main()
	except KeyboardInterrupt:
		print("\nClosing...")
