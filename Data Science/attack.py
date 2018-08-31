# This project checks to see if your password is a strong one
# It works with longer passwords, but not really short ones.
# That's because since each letter is considered a word in the dictionary.txt file,
# any password that contains just letters will be considered as a word/not a strong password.
# To alleviate this, I've split it so that it will break the string into substrings of length 3,
# because there are a lot of combinations of two letter words in the dictionary.txt as well.

# doesn't work for "I", "am", etc. etc.
# longer words should work
def is_secure(password, word_list):
	# make a list of letters of word
	if (password in word_list):
		print(password)
		return False
	# char_list = list(password)
	if (len(password) < 3):
		if (not password in word_list):
			return True

	# iterate through letters in password
	# start with one letter and then keep incresing letters
	# to check if the substring of password is an actual word
	for i in range(3, len(password)):
		sub_pw = password[0:i]
		if(sub_pw in word_list):
			print("i=", i, "sub=", sub_pw)
			secure = is_secure(password[i:], word_list)
			# print(secure)
			if (not secure):
				return False
		if(i == len(password) - 1):
			return True
		
	# goes through each word in the dictionary and checks if it appears in the password
	# doesn't work too well because each letter counts as a word in the dictionary.txt
	# for word in word_list:
	# 	if (word in password):
	# 		index = password.find(word)		#first index of word appearing
	# 		left_pw = password[0:index]
	# 		right_pw = password[index + len(word):]
	# 		security = [is_secure(left_pw, word_list), is_secure(right_pw, word_list)]
	# 		# only if both left and right sides are actual words, then return false
	# 		if (security[0] == False and security[1] == False):
	# 			return False
	return True




# open and read in words from text file
file = open("dictionary.txt", "r")
text = file.read()
file.close()

# will automatically create a list of all the words
split = text.split()
# print(type(split))

# prompt user for input
password = input("What's your password?\n").lower()

secure = is_secure(password, split)
# keep prompting user if the password is a word
while (len(password) < 3 or not secure):		#any(word in password for word in split)
	password = input("Password is a word! Enter a new one.\n").lower()
	secure = is_secure(password, split)

print("Congratulations! Your password is very secure!")