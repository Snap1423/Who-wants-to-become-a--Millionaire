questions = [
   ["Which planet is known as the Red Planet?","Venus","Mars","Jupiter","Saturn",2],
   ["Who wrote the play Romeo and Juliet?","Charles Dickens"," William Shakespeare","Jane Austen","Mark Twain",2],
   ["What is the largest ocean on Earth?","Atlantic Ocean","Indian Ocean","Arctic Ocean","Pacific Ocean",4],
   ["In which year did the Titanic sink?","1912","1920","1905","1931",1],
   ["What is the capital city of Japan?","Beijing","Seoul","Tokyo","Bangkok",3],
   ["What is the chemical symbol for gold?","Ag","Au","Fe","Pb",2],
   ["Who painted the Mona Lisa?","Vincent van Gogh","Pablo Picasso","Leonardo da Vinci","Claude Monet",3],
   [" What is the main ingredient in guacamole?","Tomato","Avocado","Onion","Lime",2],
   ["How many continents are there?","5","6","7","8",3],
   ["What is the powerhouse of the cell?","Nucleus","Cytoplasm","Mitochondria","Ribosome",3]
]
prizes = [1000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 10000000]
i = 0
for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    # check whether the answer is correct or not 
    a = int(input("Enter your answer. 1 for a, 2 for b, 3 for c, 4 for d\n"))
    if(question[5] == a):
        print("\n---------CORRRECT!----------")
    else:
        print(f"Incorrect,the correct answer was: {question[5]}")
        print("\n---------BETTER LUCK NEXT TIME!----------")
        break
    print(f"You won {prizes[i]}")
    i+=1
