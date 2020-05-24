import json
from difflib import get_close_matches
data=json.load(open("data.json"))
#print(data)
def translate(word):
    word=word.lower()  #changing all word to lower case
    if word in data:
        return data[word]
            
    else:
        print("Sorry no match found ")
    
word=input("enter the word to search ")
output=translate(word)

#we are doing following thing to print all different meaning in separate separate line
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)