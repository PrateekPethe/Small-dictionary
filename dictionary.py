import json
from difflib import get_close_matches

data = json.load(open("dictionary.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."
loop = 0
while(loop !=2):
    print("\nEnter Your Choice : ")
    print("1. Search Word \n2. Exit \n")
    choice = int(input())
    if choice == 1:
        word = input("Enter word: ")
        output = translate(word)
        if type(output) == list:
            for item in output:
                print(item)
        else:
            print(output)
    elif choice == 2:
        loop = 2
    else:
        print("Wrong Choice !. Press Either 1 or 2 ")
        