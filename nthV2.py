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
		flag = False
		for c in sequence:
			if c in ',':
				flag = True
		if (flag):
			# this might be a valid sequence of numbers as it contains at least one comma
			# next we need to split the sequence string into values
			my_array = sequence.split(',')
			for i in my_array:
				print(i)
			print(len(my_array))
			diff_array = [my_array[i+1]-my_array[i] for i in range(len(my_array)-1)]
			print(diff_array)
		else:
			# this is NOT a valid sequence so need to bail out with an error msg
			print('***Error: bad format of the sequence: ',sequence,' ***\n')

while True:
	main_loop()
