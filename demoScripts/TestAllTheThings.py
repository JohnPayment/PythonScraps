from FizzBuzz import fizzBuzz
from Anagram import detectAnagramDict as detectAnagram
from Palindrome import detectPalindrome

import sys

fizzBuzz()

print "\n"

print            "Anagram Tests"
print            "Test                                    | Result"
print            "------------------------------------------------"
sys.stdout.write("Identical strings                       | ")
if detectAnagram("test", "test"):
	print "Pass\n"
else:
	print "Fail\n"
sys.stdout.write("Non-Identical Anagram                   | ")
if detectAnagram("test", "estt"):
	print "Pass\n"
else:
	print "fail\n"
sys.stdout.write("Fail strings of equal length            | ")
if detectAnagram("test", "nope"):
	print "Fail\n"
else:
	print "Pass\n"
sys.stdout.write("Fail strings of unequal length          | ")
if detectAnagram("test", "testing"):
	print "Fail\n"
else:
	print "Pass\n"
sys.stdout.write("Empty string 1                          | ")
if detectAnagram("", "nope"):
	print "Fail\n"
else:
	print "Pass\n"
sys.stdout.write("Empty string 2                          | ")
if detectAnagram("test", ""):
	print "Fail\n"
else:
	print "Pass\n"
print "\n"

print            "Palindrome Tests"
print            "Test                  | Result"
print            "------------------------------"
sys.stdout.write("Even-Count Palindrome | ")
if detectPalindrome("woow"):
	print "pass\n"
else:
	print "fail\n"
sys.stdout.write("Odd-Count Palindrome  | ")
if detectPalindrome("wow"):
	print "pass\n"
else:
	print "fail\n"
sys.stdout.write("Even-Count Fail Test  | ")
if detectPalindrome("test"):
	print "fail\n"
else:
	print "pass\n"
sys.stdout.write("Odd-Count Fail Test   | ")
if detectPalindrome("testing"):
	print "fail\n"
else:
	print "pass\n"
sys.stdout.write("Empty String          | ")
if detectPalindrome(""):
	print "pass\n"
else:
	print "fail\n"
sys.stdout.write("One-character string  | ")
if detectPalindrome("1"):
	print "pass\n"
else:
	print "fail\n"
print "\n"
