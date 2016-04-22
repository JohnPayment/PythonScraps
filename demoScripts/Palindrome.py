
# Variables for edge cases which may or may not be true based on definition
blankIsTrue = True
oneCharPalindrome = True

def detectPalindrome(userString):
	length = len(userInput)

	if length == 0:
		return blankIsTrue
	elif length == 1:
		return oneChatPalindrome

	for i in range(0, length - 1):
		if(userInput[i] == userInput[length - (i + 1)]):
			continue
		else:
			return False

	return True
