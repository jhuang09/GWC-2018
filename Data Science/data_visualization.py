'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def get_average(list_name):
	length = len(list_name)
	total = 0
	for value in list_name:
		total += value
	return (total / length)

def already_exists(list_name, word):
	if (word in list_name):
		return True
	return False


#Get the JSON data
tweetFile = open("TwitterData/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below! 
polarity = []
subjectivity = []
common_words = ["and", "the", "about", "http", "https", "have", "for", "that" ]
massive_text = ""
filtered_words = {}

for each_tweet in tweetData:
	#grab content of each tweet
	text = each_tweet["text"]
	massive_text += text
	massive_text += " "
	txtblob = TextBlob(text)
	txtblob.sentiment

	#add the subjectivity and polarity of each tweet
	subjectivity.append(txtblob.sentiment.subjectivity)
	polarity.append(txtblob.sentiment.polarity)


#get the average of the lists
avg_polar = get_average(polarity)
avg_sub = get_average(subjectivity)

print(avg_polar, avg_sub)

# plot information
# number controls how specific the data plots are
n, bins, patches = plt.hist(polarity, 50)
plt.show()

# # part 2 extension
plt.scatter(polarity, subjectivity)
plt.xlabel("Polarity")
plt.ylabel("Subjectivity")
plt.show()

#part 3: visualizing language
# remember to update wordcloud package
massive_txtblob = TextBlob(massive_text)
for each_word in massive_txtblob.words:
	if (not each_word.isalpha() or len(each_word) < 3 or (each_word.lower() in common_words)):
		continue
	else:
		if (already_exists(filtered_words, each_word.lower())):
			filtered_words[each_word.lower()] += 1
		else:
			filtered_words[each_word.lower()] = 1

print(filtered_words)

wordcloud = WordCloud().generate_from_frequencies(filtered_words)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


# Textblob sample:
tb = TextBlob("You are a brilliant computer scientist.")
print(tb.polarity)
