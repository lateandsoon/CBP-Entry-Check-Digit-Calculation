'''
Alec Pearce - 01/02/2020
Check Digit Calculation
Source of Business logic : 
https://www.cbp.gov/sites/default/files/assets/documents/2018-Feb/ACE%20CATAIR%20Appendix%20E%20Valid%20Entry%20Numbers%20-%20May%202012.pdf
'''

#Brokerage Check Digit Calculation
import time

def create_chkdgt(filer_code, entry_number, increment):
	'''
	Takes a AN filer code from a broker, and the first 7 digits numeric of an entry to calculate an entry # check digit.
	'''
	print('\n')
	filer_code = str(filer_code).upper()
	entry_number = str(entry_number)
	filer_code_converion = {'A': 1 , 'H':8, 'O':6, 'U':4, 'B':2, 'I':9, 'P':7, 'V':5, 'C':3, 'J':1, 'Q':8, 'W':6, 'D':4, 'K':2, 'R':9, 'X':7, 'E':5, 'L':3, 'S':2, 'Y':8, 'F':6, 'M':4, 'T':3, 'Z':9, 'G':7, 'N':5 }

	#Create transformed Alphanumeric Filer Code to Numeric
	numeric_filer_code = ''
	for i in filer_code:
		if i in filer_code_converion.keys():
			numeric_filer_code += str(filer_code_converion[i])
		else:
			numeric_filer_code += str(i)

	#Combine Filer Code & Entry #
	combined_number = numeric_filer_code + entry_number

	#Calculate Check Digits via Formatting of Even & Odd Positions
	#Fetch every other value from combined number
	even_values = []
	odd_values = []
	for digit in range(len(combined_number)):
		if digit % 2 > 0:
			even_values.append(combined_number[digit])
		else:
			odd_values.append(combined_number[digit])

	print('Even :', even_values)
	print('Odd : ', odd_values)

	#Calculate Evens
	#Multiply each value by 2
	doubled_even_values = []
	for value in range(len(even_values)):
		doubled_even_values.append(int(even_values[value]) * 2)

	#Increase or decrease value by 1 if product is >= 10, only take the first resulting digit
	for value in range(len(doubled_even_values)):
		if doubled_even_values[value] >= 10:
			doubled_even_values[value] = str(doubled_even_values[value] + 1)[-1:]

	print('Doubled Even :', doubled_even_values)

	#Sum all even values - Step C.
	summed_even_values = 0
	for value in range(len(doubled_even_values)):
		summed_even_values += int(doubled_even_values[value])

	print('Summed Even :', summed_even_values)

	#Calculate Odds - Step D.
	summed_odd_values = 0
	for value in range(len(odd_values)):
		summed_odd_values += int(odd_values[value])

	print('Summed Odd :', summed_odd_values)

	#Combined Odd and Even Summed Values - Step E.
	summed_odd_even_values = summed_even_values + summed_odd_values

	print(summed_even_values, ' + ', summed_odd_values, ' = ', summed_odd_even_values)

	#Subtract last digit in Step E from 10. Last digit of result is Check Digit
	check_digit = 10 - int(str(summed_odd_even_values)[-1:])
	if check_digit == 10:
		check_digit = 0

	print('Check Digit Calculation : 10 -', str(summed_odd_even_values)[-1:])
	print('Check Digit :', check_digit)
	check_digit = int(check_digit) + int(increment)
	print('Check Digit Incremented :', check_digit)
	print('Entry # : ', filer_code, '-', str(entry_number) + '-' + str(check_digit))
	return check_digit

def get_filer():
	filer_code = input('Enter Filer Code : ')
	return filer_code

def get_entry_number():
	entry_number = input('Please enter first 7 digits of entry # : ')
	return entry_number

def get_increment():
	increment = input('Enter check digit increment (0, 1, 2, etc.): ')
	return increment

def main():
	print('\nWelcome. \n\nThis program shows and calculates a CBP Entry # check digit. \n\nCalculation logic can be found at : \nhttps://www.cbp.gov/sites/default/files/assets/documents/2018-Feb/ACE%20CATAIR%20Appendix%20E%20Valid%20Entry%20Numbers%20-%20May%202012.pdf\n')
	try:
		filer_code = get_filer()
		assert len(filer_code) == 3,'Filer Code must be 3 digits'
	except AssertionError as error:
		print(error)
		filer_code = get_filer()
		
	try:
		entry_number = get_entry_number()
		assert len(entry_number) == 7, 'Entry Number must be 7 digits'
		assert type(int(entry_number)) == int, 'Entry Number must be numeric'
	except AssertionError as error:
		print(error)
		entry_number = get_entry_number()
		
	try:
		increment = get_increment()
		assert len(increment) == 1, 'Check digit increment must be 1 digit'
		assert type(int(increment)) == int, 'Check digit increment must be numeric'
	except AssertionError as error:
		print(error)
		increment = get_increment()

	try:
		check_digit = create_chkdgt(filer_code, entry_number, increment)
		close = input('Press any key to close\n')
	except:
		print('Sorry, there was an issue with the data entered, please check your inputs and try again.')
		main()
main()