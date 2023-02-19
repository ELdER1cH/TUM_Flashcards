import random
import collections
import cards.gdb_cards as gdb_cards
import cards.itsec_cards as itsec_cards

#Used Variables
index = 0
counter = 0
used_indices = collections.deque()


print("Select a deck to study:")
print("1. gdb")
print("2. itsec")
inp = -1
while(inp != "1" and inp != "2"):
    inp = input("Enter the number of the deck you would like to study: \n")
    if(inp == "1"):
        questions = gdb_cards.questions
        answers = gdb_cards.answers
        print("You have selected the gdb deck. Press ENTER to start the quiz. Press \"q\" to exit at any time\n\n")
        print("There are:",len(questions), "questions in this deck")
    elif(inp == "2"):
        questions = itsec_cards.questions
        answers = itsec_cards.answers
        print("You have selected the itsec deck. Press ENTER to start the quiz. Press \"q\" to exit at any time\n\n")
        print("There are:",len(questions), "questions in this deck")
    else:
        inp = input("Please enter a valid number: \n")

while 1:

    index = random.randrange(len(questions))
    if not used_indices.__contains__(index):
        used_indices.insert(index, index)
    elif len(used_indices) == len(questions):
        inp = input("All questions have been asked. Would you like to start again? If not, press 'n' \n")
        if inp == "n":
            break
        else:
            used_indices.clear()
            counter = 0
            continue
    else:
        continue
    
    inp = input("Press ENTER for a question or q to exit: \n")
    if(inp == "q"):
        break
    counter += 1
    print(f"Question # {counter} of {len(questions)}:\n")
    print(questions[index])
    print("\n")
    
    inp = input("Press ENTER for the answer: \n")
    if(inp == "q"):
        break
    print(answers[index])
    print("\n")