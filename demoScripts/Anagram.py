
# Variables for edge cases which may or may not be true based on definition
ignoreNumbers = False
ignoreWhitesapce = True
ignorePunctuation = True
ignoreCapitalization = True

def detectPalindrome(s1, s2):
	s1Value = getStringValue(s1)
	s2Value = getStringValue(s2)

	return s1 == s2

# Assumes ASCII Characters
def getStringValue(string):
	value = 0
	processedString = string

	if ignoreCapitalization:
		processedString = string.lower()

	for c in processedString:
		if c.isspace() && ignoreWhitesapce:
			continue
		if c.isdigit() && ignoreNumbers:
			continue
		if c in String.punctuation && ignorePunctuation:
			continue

		value += ord(c)

	return value
