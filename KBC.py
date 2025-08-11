# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
questions = ["How many oceans are there in world?",
             "Which planet is known as red planet?",
             "Who is known as missile man of india?"] 
             
options = ["A. 6 , B. 8 , C. 5 , D. 4",
           "A. Jupiter , B. Mars , C. Earth , D. Neptune",
           "A. Mahatma gandhi , B. APJ Kalam , C. Rbindranath tagore , D. Manmohan singh"]
           
answers = ["C", "B" , "B"]

prize_money = [1000, 4000, 8000]
total_winnings = 0

for i in range(len(questions)):
    print(f"question{i+1}: {questions[i]}")
    print(f"options: {options[i]}")
    user_input = input("Enter your answer from given A,B,C,D options!").strip().upper()
    if user_input == answers[i]:
            print("You entered right answer")
            total_winnings += prize_money[i]
    else:
            print(f"Wrong answer, correct answer is {answers[i]}")
            break
        
    print(f"Congratulations you are taking home: ${total_winnings}!")
            

  


