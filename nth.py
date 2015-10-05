#!/opt/local/bin/python

def ask_ok(prompt, retries=4, complaint='s or e, please!'):
    while True:
        ok = input(prompt)
        if ok in ('e', 'E'):
            return True
        if ok in ('s', 'S'):
            return False
        retries = retries - 1
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)

def main_loop():
	if (ask_ok('Do you want to enter a [s]equence or an [e]quation? ')):
	
		# value returned from prompt must be True which was an 'e' for equation
		# therefore prompt user for an equation
		#
		equation = input('Tell me the equation ')
		#
		# validate the input and check it is ok equation
		#
		flag = False
		for c in equation:
			if c in 'n': 
				flag = True
		if (flag):
			# this might be a valid equation as it contains an 'n'
			# replacing n and expanding out to full string
			# 
			output_string = 'Sequence is '
			for loop in range(1,6):
				temp_str = ' * ' + str(loop) 
				new_equation = equation.replace('n',temp_str) 
				output_string = output_string + str(eval(new_equation)) + ','
				print(new_equation + ' = ' + str(eval(new_equation)))
			print(output_string)
		else:
			# this is NOT a valid equation so need to bail out with an error msg
			print('***Error: bad format of the equation: ',equation,' ***\n')
	else:
		sequence = input('Give me a comma separated sequence ')
		print(sequence)


while True:
	main_loop()
