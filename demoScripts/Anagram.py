import string

# Variables for edge cases which may or may not be true based on definition
ignoreNumbers = False
ignoreWhitespace = True
ignorePunctuation = True
ignoreCapitalization = True

# NOTE: Some edge cases will return false positives with this method.
# For example "AD" and "BC" are ordinally equivilant, even though they are not anagrams of one another.
# However, the trade off is a linear comparison. This is extremely fast.
def detectAnagramOrdinal(s1, s2):
	s1Value = getStringValue(s1)
	s2Value = getStringValue(s2)

	return s1Value == s2Value

def getStringValue(s):
	value = 0
	processedString = s

	if ignoreCapitalization:
		processedString = s.lower()

	for c in processedString:
		if c.isspace() and ignoreWhitespace:
			continue
		if c.isdigit() and ignoreNumbers:
			continue
		if c in string.punctuation and ignorePunctuation:
			continue

		value += ord(c)

	return value

def detectAnagramDict(s1, s2):
	sdict1 = getCharDictionary(s1)
	sdict2 = getCharDictionary(s2)

	return sdict1 == sdict2

def getCharDictionary(s):
	dictionary = dict()

	for c in s:
		if c.isspace() and ignoreWhitespace:
			continue
		if c.isdigit() and ignoreNumbers:
			continue
		if c in string.punctuation and ignorePunctuation:
			continue

		if c in dictionary:
			dictionary[c] += 1
		else:
			dictionary[c] = 1

	return dictionary
