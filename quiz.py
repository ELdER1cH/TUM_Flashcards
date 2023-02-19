import random
import collections
import cards.gdb_cards as gdb_cards
import cards.itsec_cards as itsec_cards
import debug 

def debug():
    print("Debugging")
    imp = input("Enter the name of the module you would like to debug: \n")
    if (imp == "gdb"):
        for i in range(len(gdb_cards.questions)):
            print(f"{i=}\n Question: {gdb_cards.questions[i]}\nAnswer: {gdb_cards.answers[i]}\n")
        return
    elif(imp == "itsec"):
        pass




#Used Variables
index = 0
counter = 0
used_indices = collections.deque()


print("Select a deck to study:")
print("1. gdb")
print("2. itsec")
print("3. SQL")
print("q. Quit")
inp = -1
while(inp != "1" and inp != "2" and inp != "q" and inp != "-2" and inp != "3"):
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
    elif(inp == "3"):
        questions = gdb_cards.SQL_Questions
        answers = gdb_cards.SQL_Answers
        print("You have selected the SQL deck. Press ENTER to start the quiz. Press \"q\" to exit at any time\n\n")
        print("There are:",len(questions), "questions in this deck")
    elif(inp == "q"):
        break
    elif(inp == "-2"):
        debug()
    else:
        inp = input("Please enter a valid number: \n")

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
    
