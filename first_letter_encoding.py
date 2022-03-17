print("Insert the message:")
sMessage = input("> ")
lMessage = sMessage.split(" ")
sResult = ''
nIndex = 0

for sWord in lMessage:
	if len(sWord) > 1:
		sResult += sWord.replace(sWord[0], '', 1)
	else:
		sResult += "%" + sWord

	if nIndex != len(lMessage)-1:
		sResult += " "

	nIndex += 1

print(sResult)
bYes_No = "No" if sResult != "ome %t ext" else "Yes"
print("Is the result right? " + bYes_No)