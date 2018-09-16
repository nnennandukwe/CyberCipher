from __future__ import print_function

import re
import random
# Initial Basic Caesar Cipher Cryptography Program

# Alphabet

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letters = {
	"A": 0,
	"B": 1,
	"C": 2,
	"D": 3,
	"E": 4,
	"F": 5,
	"G": 6,
	"H": 7,
	"I": 8,
	"J": 9,
	"K": 10,
	"L": 11,
	"M": 12,
	"N": 13,
	"O": 14,
	"P": 15,
	"Q": 16,
	"R": 17,
	"S": 18,
	"T": 19,
	"U": 20,
	"V": 21,
	"W": 22,
	"X": 23,
	"Y": 24,
	"Z": 25,
}

def encrypt_value(value):

	user_input = value.upper()
	decrypted = None

	# Check for numbers in the sequence to remove
	#NOTE: Need to remove any special, non-alphabetic characters from user input

	if user_input.isalpha():
		decrypted = user_input
	else:
		decrypted = re.sub(r'\d', "", user_input)

	print(decrypted)

	# Perform the encryption
	#NOTE: Modify to be function that can support encryption and error handling

	encrypt_list = []

	# randomize the shifter once for entire string
	shifter = random.randint(1,9)

	# coin flip a negative or positive shifter operation
	direction = random.randint(0,1)

	if direction:
		for el in decrypted:
			index = letters[el] + shifter
			try:
				el = alphabet[index]
			except IndexError:
				if index > 26:
					index - 26
				else:
					index + 26
			encrypt_list.append(el)
	else:
		for el in decrypted:
			index = letters[el] - shifter
			try:
				el = alphabet[index]
			except IndexError:
				if index > 26:
					index - 26
				else:
					index + 26
			encrypt_list.append(el)

	encrypted = "".join(encrypt_list)

	print("ENCRYPTION: ", encrypted)

	# decrypt_value(
	# value=encrypted,
	# shifter=shifter,
	# direction=direction
	# )
	
	return encrypted

def decrypt_value(value, shifter, direction):

	user_input = value.upper()
	encrypted = None

	if user_input.isalpha():
		encrypted = user_input
	else:
		encrypted = re.sub(r'\d', "", user_input)

	print(encrypted)

	decrypt_list = []

	if direction:
		for el in encrypted:
			index = letters[el] - shifter
			try:
				el = alphabet[index]
			except IndexError:
				if index > 26:
					index - 26
				else:
					index + 26
			decrypt_list.append(el)
	else:
		for el in encrypted:
			index = letters[el] + shifter
			try:
				el = alphabet[index]
			except IndexError:
				if index > 26:
					index - 26
				else:
					index + 26
			decrypt_list.append(el)

	decrypted = "".join(decrypt_list)

	print("DECRYPTION: ", decrypted)

	return decrypted