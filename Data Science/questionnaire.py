# This will store each person's answers into a JSON file
# People will be able to update their answers by inputting the same name
import json

def check_int(num):
	valid = False
	while (not valid):
		try:
			num = int(num)
			valid = True
			return num
		except ValueError:
			print("Invalid answer. Please try again.")
			num = input()

def already_exists(dict_list, answers):
	index = -1
	for i in range(len(dict_list)):
		if (answers[0].lower() == dict_list[i]["name"]):
			#update information instead of adding
			index = i
			break
	return index
		

questions = ["What's your name?", "What's your favorite food?", "How old are you?"]
answers = []
prop = ("name", "food", "age")
for question in questions:
	print(question)
	answer = input()
	if (question == questions[2]):
		#wow handling exceptions
		
		answer = check_int(answer)
		if (int(answer) < 12):
			print("You're too young to be taking this quiz. Bye bye!")
			exit()
		while (int(answer) > 100 or int(answer) < 0):
			print("Invalid answer. Please try again")
			answer = input()
	answers.append(answer)
length = len(questions)
new_person = {}
print("You answered:")
for i in range(length):
	print(questions[i])
	print(answers[i])
	new_person[prop[i]] = answers[i]
print(new_person)

# js = json.dumps(new_person)
fp = open("data.json", "rb+")
jsontoPython = fp.read()
jsontoPython = json.loads(jsontoPython) #list

index = already_exists(jsontoPython, answers)
if index != -1:
	del jsontoPython[index]

jsontoPython.append(new_person)	#list

pythontoJSON = json.dumps(jsontoPython)
fp.close()
fp = open("data.json", "w+")
print(json.dumps(jsontoPython, indent=4, sort_keys=True))
fp.write(pythontoJSON)
fp.close()