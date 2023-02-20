import random
import collections
import cards.gdb_cards as gdb_cards
import cards.itsec_cards as itsec_cards
import cards.gbs_cards as gbs_cards


#Used Variables
index = 0
counter = 0
used_indices = collections.deque()

#new decks can easily be added here, and the first while loop will not become cluttered over time
valid_stacks = [
"GBS",
"ITSEC",
"GDB",
"SQL"
]

print("Type 'list' to see a list of available cards / input")
inp = 0
while(not valid_stacks.__contains__(inp)):
    inp = input("\nEnter the name of the deck you would like to study (Input is not case sensitive): \n").upper()
    if (inp == "LIST"):
        print("\nHere are the available decks:")
        for i in range (0, len(valid_stacks)):
            print(valid_stacks[i])
    elif (inp == "GDB"):
        questions = gdb_cards.questions
        answers = gdb_cards.answers
        print("You have selected the gdb deck. Press ENTER to start the quiz. Press \"q\" to exit at any time\n\n")
        print("There are ",len(questions), "questions in this deck")
    elif (inp == "ITSEC"):
        questions = itsec_cards.questions
        answers = itsec_cards.answers
        print("You have selected the itsec deck. Press ENTER to start the quiz. Press \"q\" to exit at any time\n\n")
        print("There are:",len(questions), "questions in this deck")
    elif(inp == "SQL"):
        questions = gdb_cards.SQL_Questions
        answers = gdb_cards.SQL_Answers
        print("You have selected the SQL deck. Press ENTER to start the quiz. Press \"q\" to exit at any time\n\n")
        print("There are:",len(questions), "questions in this deck")
    elif(inp == "q"):
        break
    else:
        print("Please enter a valid deck name! Try again...")

while 1:
    #Get Question
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
    
    inp = input("Press ENTER for the next question\n")
    if(inp == "q"):
        break
    counter += 1
    print(f"Question # {counter} of {len(questions)}:\n")
    # print("Question: ", index)
    print(questions[index])
    print("\n")
    
    inp = input("Press ENTER for the answer: \n")
    if(inp == "q"):
        break
    # print("gAnswer: ", index)
    print(answers[index])
    print("\n")
