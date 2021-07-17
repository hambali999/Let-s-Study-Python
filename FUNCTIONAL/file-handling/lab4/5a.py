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

q6()