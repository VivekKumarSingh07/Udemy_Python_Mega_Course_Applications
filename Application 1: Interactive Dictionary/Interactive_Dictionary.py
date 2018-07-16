import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def GetMeaning(word):
	if word in data:
		return(data[word])
	elif word.title() in data:
		return(data[word.title()])
	elif word.upper() in data:
		return(data[word.upper()])
	elif len(get_close_matches(word, data.keys())) > 0:
		yes_or_no = input("You meant %s instead? Press 'Y' if yes or 'N' if no: " %get_close_matches(word,data.keys())[0])
		if yes_or_no == "Y" or yes_or_no == "y":
			return (data[get_close_matches(word,data.keys())[0]])
		elif yes_or_no == "N" or yes_or_no == "n":
			return "The word doen't exist. Double check it"
		else:
			return "We didn't understand your query."
	else:
		return "The word doen't exist. Double check it"

word = input("Enter word:")
word = word.lower()
output = GetMeaning(word)

if type(output) is list:
	for item in output:
		print(item)
else:
	print(output)
