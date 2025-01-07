questions = ( "Who is the largest land animal? ",
            "How many bytes are in 1 kilobyte of memory?",
            "What is the name of highest mountain peak?",
            "Which is the biggest youtube channel in india by subscriber count? "
    )
options =(("A. Whale","B. Elephant","C. Hippopotamus","D. Giraffe"),
            ("A. 986","B. 1000","C. 1024","D. 1044"),
            ("A. Kachenjunga","B. Mount Everest","C. Mount Fuji","D. K2"),
            ("A. Acharya prashant","B. T-series","C. Carryminati","D. BB ki Vines")
)
guesses =[]
answers =("B","C","B","B")
question_num =0
score =0
print("------------------MCQ QUIZ-----------------------")
for question in questions :
    print("-------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    
    guess =input("Enter Your Answer (A B C D) : ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score +=1
        print(f"{guess} is the correct option")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct option")
    
    question_num +=1

print("-------------------------------------------")
print("Your Guesses : " , end=" ")
for guess in guesses :
    print(guess,end=" ")
print()
        
print("Answers      : ",end=" ")
for answer in answers:
    print(answer,end=" ")
print()
    
print(f"Your score is {int((score/len(answers)*100))}%")

    
