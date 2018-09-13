import re
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

user_input = input("Enter string below: ")
user_input = user_input.upper()
decrypted = None

# Check for numbers in the sequence to remove
#NOTE: Need to remove any special, non-alphabetic characters from user input

if user_input.isalpha():
	decrypted = user_input
else:
	decrypted = re.sub(r'\d', "", user_input)

print(decrypted)

# Perform the encryption
#NOTE: Modify to be function that can support encryption, decryption, and error handling

encrypt_list = []

#NOTE: Need to randomize the encryption shifter each time the function is called
for el in decrypted:
	index = letters[el] - 3
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

