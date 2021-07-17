   
import random
def takeQuiz(correctAns):
   ''' this functions accepts a list of correct answers
    it prompts user to provide answers and stores in an another list, userAns
    it compares and displays appropriately
    and it finally reports the number of correct answers
    '''
   #create an empty list, userAns
   userAns = []
   #loop 10 times
   for i in range(10):
       #prompt user to give answer to each question
       ans = input(f"Q{i+1}: ")
       #add this answer into the list
       userAns.append(ans)
   print(userAns)
   #compare each entry in userAns with correctAns
   total=0
   for i in range(10):
       if userAns[i]==correctAns[i]:
           #keep tracks of score for correct answers
           total+=1
           print(f"Q{i+1}: {userAns[i]} correct")
       else:
           print(f"Q{i+1}: {userAns[i]} is incorrect, answer is {correctAns[i]}")
   #end of for loop
   #report number of correct answers
   print(f"Total {total} out of 10 correct")
    
def q6():
    correctAns=('a','b','b','a','d','c','b','a','b','c')
    takeQuiz(correctAns)
    print("End program")
    
def menu():
    '''this menu function presents a list of choices for user to select
    it returns user's choice
    '''
    print("Menu")
    print("1. List quiz answers")
    print("2. Change quiz answers")
    print("3. Test quiz")
    print("0. Quit")
    opt = int(input("Enter option: "))
    return opt

def init(correctAns):
    '''accepts a list, correctAns;
    reads from Q7Dat.txt which contains the correct answers to 10 mcq
    it stores these answers in correctAns
    '''
    
    fin = open("Q7Dat.txt","r")
    for eachAns in fin:
        ans = eachAns.strip("\n")
        correctAns.append(ans)
    fin.close()

def displayAnswers(correctAns):
    '''this function accepts a list of correct answers
    and displays them
    '''
    for i in range(len(correctAns)): #or range(10) is acceptable too
        print(f"Q{i+1}: {correctAns[i]}")
        
def changeAnswers(correctAns):
    '''accepts a list of correct answers
    prompts user repeatedly to enter question number and new answer
    it updates the list, correctAns, with new answer; loop ends when user enters
    question number.
    it validates question number (1-10) and new answer ('a','b','c','d')
    if invalid, display error message
    '''
    while True:
        #prompt for question number
        print("Enter -1 to quit changing answers")
        qNo = int(input("Enter question number: "))
        #check if is is-1; stop loop
        if qNo==-1:
            break
        #if valid (1-10)
        elif qNo in range(1,11):
            #prompt for new answer
            newAns = input("Enter new answer: ")
            #update new answer to correctAns
            if newAns in ['a','b','c','d']:
                correctAns[qNo-1]=newAns
            else:
                print("Invalid answer!")
        #else display error message
        else:
            print("Invalid question number!")
    #end of while loop
            
def updateFile(correctAns):
    '''accepts a list of correct answer
    it updates the file, Q7Dat.txt
    '''
    fout = open("Q7Dat.txt","w")
    for i in range(len(correctAns)):
        fout.write(f"{correctAns[i]}\n")
    fout.close()
    
def q7():
    correctAns = []
    init(correctAns)
    print(correctAns) #for testing only
    while True:
        opt = menu()
        if opt==1:
            displayAnswers(correctAns)
        elif opt==2:
            changeAnswers(correctAns)
        elif opt==3:
            takeQuiz(correctAns)
        elif opt==0:
            updateFile(correctAns)
            break
        else:
            print("Invalid option!")
    #end of while loop
    print("End program")
q7()
