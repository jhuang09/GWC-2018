# Find a correlation between number of downloads and birthdates
# Find a correlation between number of downloads and age
# Find a correlation between number of downloads and death

import classics
import operator
import matplotlib.pyplot as plt
list_of_book = classics.get_books()

# for row in list_of_book:
# 	print(row["bibliography"]["title"], row["metadata"]["downloads"])

sorted_books = dict()
for book in list_of_book:
	title = book["bibliography"]["title"]
	downloads = book["metadata"]["downloads"]
	birth = book["bibliography"]["author"]["birth"]
	death = book["bibliography"]["author"]["death"]
	sorted_books[title] = {"downloads" : downloads, "birth": birth, "death": death}

# sorted_list = sorted(sorted_books.items(), key=operator.itemgetter(1), reverse=True)
plt.figure(1)
for each_book in sorted_books:
	book_info = sorted_books[each_book]
	birth = book_info["birth"]
	death = book_info["death"]
	age = death - birth
	if (age <= 0 or age >= 110):
		continue
	downloads = book_info["downloads"]
	plt.plot(age, downloads, "bo")
	# plt.subplot(111)
	# plt.plot(downloads, age, "r--")
plt.title("Relationship between age and downloads")
plt.ylabel("Downloads")
plt.xlabel("Age")
plt.show()
plt.savefig("birth.png")

#print(list_of_scores)