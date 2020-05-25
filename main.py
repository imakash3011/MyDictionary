import json
from difflib import get_close_matches
data=json.load(open("data.json"))
#print(data)
def translate(word):
    word=word.lower()  #changing all word to lower case
    if word in data:
        return data[word]
    elif word.title() in data:   #changing tamil into Tamil so that both can work
        return data[word.title()]
    elif word.upper() in data:   #changing tamil into TAMIL so that both can work
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:     #("abc",["abcd","abcde","acbed"]) like this
        print("did you mean %s instead " %get_close_matches(word,data.keys())[0])
        decide=input("press y for yes and n for no ")
        if decide=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif decide=="n":
            return("Sorry no match found ")
        else:
            return("you have entered wrong input ")        
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