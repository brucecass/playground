#!/opt/local/bin/python

#
# Script name : nthV2.py
# Author : BDC
# Date : 05.10.15
# Description : play script in order to both try to learn a bit of python and to also try to 
#               hightlight how easy nth term ks3 maths is to Son
#

import sys

def all_same(items):
    return all(x == items[0] for x in items)

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
		# validate the input and check it is ok equation, well at this point
		# lets just check that there is a 'n' in the equation supplied
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
			
			# lets just assume that we will report back a sequence of 6 numbers max
			#
			for loop in range(1,6):
				temp_str = ' * ' + str(loop) 

				# bit of string manipulation here: replacing the 'n' with a multiplication
				# character and then adding a loop value after i.e. n = * 1 in the first
				# iteration
				#
				new_equation = equation.replace('n',temp_str) 
				
				# building up the output sequence string by eval'ing (running the maths)
				# and appending the result to the string that was generated the last time 
				# around the loop
				#
				try:
					if (loop != 5):
						output_string = output_string + str(eval(new_equation)) + ','
					else:
						output_string = output_string + str(eval(new_equation))
				except:

					# someone must have entered some text that could not be 
					# mathematically correct - maybe some text 
					#
					print('**** ERROR: bad equation supplied ****\n')
					break

			# print the sequence of numbers calculated
			#
			print(output_string)
		else:

			# this is NOT a valid equation so need to bail out with an error msg
			#
			print('***Error: bad format of the equation: ',equation,' ***\n')
	else:
		
		# value returned from prompt must be False which was an 's' for sequence
		# therefore prompt user for a sequence of numbers in a list
		#
		sequence = input('Give me a comma separated sequence ')
                
		# validate the input and check it is an ok(ish) sequence of numbers, well at 
		# this point lets just check that there is one or more ',' in the sequence supplied
                #
		flag = False
		for c in sequence:
			if c in ',':
				flag = True
		if (flag):

			try:	
				# this might be a valid sequence of numbers as it contains at least one comma
				# next we need to split the sequence string into values
				#
				my_array = sequence.split(',')
	
				# initiate an empty array/list so that we can add values to it
				#
				diff_value = []
	
				# lets run through the array/list of values given to us and lets calculate the difference 
				# between each member of the sequence
				#
				for i in range(len(my_array)-1):

					diff_value.insert(i,int(my_array[i+1])-int(my_array[i]))

				# lets run through the array/list of values that have been calcuated between each supplied sequence
				# number and lets check that they are all the same i.e. the sequence is a linear sequence
				#
				if all_same(diff_value):

					# All items in the list are the same so we should be able to work out the nth term equation 
					# from all this and we should be able to calulate the 'offset' value
					#
					offset_value = int(my_array[0])-int(diff_value[0])
	
					# print out the calculated equation
 					#
					print('Equation is = %d' % diff_value[0],'n','%+d ' % offset_value,'\n')
				else:
				
					# hhhmm not all the values in the supplied sequence have the same difference 
					# So this is NOT a linear sequence and we need to bail out
					#
					print('***BAIL!! THERE\'S A VALUE IN THE LIST THAT ISN\'T THE SAME!!***\n\n')
			except:
					
					# someone must have entered some text that could not be 
					# mathematically correct - maybe some text 
					#
					print('**** ERROR: bad sequence supplied ****\n')
		else:
	
			# this is NOT a valid sequence (or there isn't a comma found in the supplied sequence
			# So need to bail out with an error msg
			#
			print('***Error: bad format of the sequence: ',sequence,' ***\n')

while True:

	# infinate loops are bad
	try:
		# continue to execute the main loop of code until a control+C is hit
		main_loop()

	except KeyboardInterrupt:
		
		# if we catch a control+C then bail out of the code completely
        	print('\n\nBye bye then...\n')
        	sys.exit()
