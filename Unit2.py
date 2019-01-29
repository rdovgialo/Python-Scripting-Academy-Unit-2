def get_names():
    print("List any 5 of the first 20 elements in the Period table")
    list_answers = []
    num_guesses = 0
    used = False
    while num_guesses < 5:
        answer = input("Enter the name of an element: ")
        #First entry will always have no matches in the list
        if num_guesses == 0:
            list_answers.append(answer.lower())
            num_guesses+=1
        else:
            # Run through all list items to check if guess matches the any of list items
            for word in list_answers:
                if answer.lower() == word:
                    used = True
                else:
                    used = False
            #if no mathces faound -> append | else -> a match was found
            if used:
                print(answer + " was already entered   <--no duplicates allowed")
            else:
                #check that answer is one word before appending
                if " " in answer:
                    print("please provide only one word ")
                else:
                    list_answers.append(answer.lower())
                    num_guesses+=1
    return list_answers
#--------------------------------------------------------------------------------------------------------------------------
def check_list(item, list_2_check):
    correct=False
    for thing in list_2_check:
        if item.lower() == thing.lower():
            correct=True
        else:
            # variable correct is set to FALSE by fefoult
            pass
    return correct
#--------------------------------------------------------------------------------------------------------------------------

!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt
elements1_20 = open('elements1_20.txt','r')
elements = []
# Convert data from file to a list in lower case
element = elements1_20.readline().strip().lower()
while element:
    elements.append(element)
    element = elements1_20.readline().strip().lower()
answers = get_names()
correct_list = []
incorrect_list = []
for answ in answers:

    check = check_list(answ, elements)
    # use boolean value to deside which list answ need to be appended
    if check:
        correct_list.append(answ)
    else:
        incorrect_list.append(answ)
procentage = (len(correct_list)*100)/len(answers)
print(str(procentage)+'% correct\nFound: ',end='')
for correct in correct_list:
    print(correct+" ",end='')
print('\nNot Found: ',end='')
for incorrect in incorrect_list:
    print(incorrect+" ",end='')
