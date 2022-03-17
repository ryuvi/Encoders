# FIRST: Take the code input
# SECOND: Transform in list
# THIRD: Pass through the list and match the letter with a number
# FOURTH: Write the result

lA = ["a", "b", "c"]
lD = ["d", "e", "f"]
lG = ["g", "h", "i"]
lJ = ["j", "k", "l"]
lM = ["m", "n", "o"]
lP = ["p", "q", "r", "s"]
lT = ["t", "u", "v"]
lW = ["w", "x", "y", "z"]


# TAKE THE CODE INPUT AND TRANSFORM IN LIST
def init():
	nOption = input("Want to [1]encode or [2]decode? ")

	if nOption in ("1", "encode"):
		print("Insert the message:")
		sMessage = input("> ")
		lMessage = sMessage.split(" ")
		encode(lMessage)

	elif nOption in ("2", "decode"):
		print("Insert the message:")
		sMessage = input("> ")
		lMessage = sMessage.split(" ")
		decode(lMessage)

	else:
		init()


# JUST A COUNTER TO NOW HOW MANY TIMES THE NUMBER IS PRESSED
def number_quantity(sLetter, lPossibility):
	nLoop = 0
	for sPossibility in lPossibility:
		if sLetter == sPossibility:
			nLoop += 1

	return nLoop


# CHECK WHICH LETTER IS, SO THE NUMBER CAN BE ASSIGNED
def to_number(letter):
	sLetter_to_number = ''
	if letter in lA:
		nNumber = 2
		nQuantity = number_quantity(letter, lA)
		nIndex = 0
		while nIndex <= nQuantity:
			sLetter_to_number += str(nNumber)
			nIndex += 1

		return sLetter_to_number

	elif letter in lD:
		nNumber = 3
		nQuantity = number_quantity(letter, lD)
		nIndex = 0
		while nIndex <= nQuantity:
			sLetter_to_number += str(nNumber)
			nIndex += 1

		return sLetter_to_number

	elif letter in lG:
		nNumber = 4
		nQuantity = number_quantity(letter, lG)
		nIndex = 0
		while nIndex <= nQuantity:
			sLetter_to_number += str(nNumber)
			nIndex += 1

		return sLetter_to_number

	elif letter in lJ:
		nNumber = 5
		nQuantity = number_quantity(letter, lJ)
		nIndex = 0
		while nIndex <= nQuantity:
			sLetter_to_number += str(nNumber)
			nIndex += 1

		return sLetter_to_number

	elif letter in lM:
		nNumber = 6
		nQuantity = number_quantity(letter, lM)
		nIndex = 0
		while nIndex <= nQuantity:
			sLetter_to_number += str(nNumber)
			nIndex += 1

		return sLetter_to_number

	elif letter in lP:
		nNumber = 7
		nQuantity = number_quantity(letter, lP)
		nIndex = 0
		while nIndex <= nQuantity:
			sLetter_to_number += str(nNumber)
			nIndex += 1

		return sLetter_to_number

	elif letter in lT:
		nNumber = 8
		nQuantity = number_quantity(letter, lT)
		nIndex = 0
		while nIndex <= nQuantity:
			sLetter_to_number += str(nNumber)
			nIndex += 1

		return sLetter_to_number

	elif letter in lW:
		nNumber = 9
		nQuantity = number_quantity(letter, lW)
		nIndex = 0
		while nIndex <= nQuantity:
			sLetter_to_number += str(nNumber)
			nIndex += 1

		return sLetter_to_number


# GO THROUGH THE LIST AND MATCH LETTER WITH NUMBER
def encode(lMessage):
	sResult = ''
	for sItem in lMessage:
		for sSubItem in sItem:
			sResult += to_number(sSubItem) + "-"
		sResult += " "

	print(sResult)
	bYes_No = "No" if sResult != "7777-666-6-33 8-33-99-8" else "Yes"
	print("Is the result right? " + bYes_No)


# CHECK WHICH NUMBER IS, SO THE LETTER CAN BE ASSIGNED
def set_letter(code, location):
	if code == 2:
		return lA[location]

	elif code == 3:
		return lD[location]

	elif code == 4:
		return lG[location]

	elif code == 5:
		return lJ[location]

	elif code == 6:
		return lM[location]

	elif code == 7:
		return lP[location]

	elif code == 8:
		return lT[location]

	elif code == 9:
		return lW[location]


# GO THROUGH THE LIST AND MATCH NUMBER WITH LETTER
def decode(lMessage):
	sResult = ''
	lLetter = []
	nIndex = 0

	for sWord in lMessage:
		lLetter = sWord.split("-")
		for sLetter in lLetter:
			nLetter = len(sLetter)-1
			nCode = sLetter[0][0]
			# 7777-666-6-33 8-33-99-8

			sResult += set_letter(int(nCode), nLetter)

		if nIndex != len(lMessage)-1:
			sResult += " "

		nIndex += 1

	print(sResult)
	bYes_No = "No" if sResult != "some text" else "Yes"
	print("Is the result right? " + bYes_No)

init()