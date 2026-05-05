import random
numbers=[1,2,3,4,5,6,7,8,9,10];
while True:
    difficulty=input("\nChoose difficuly (Easy,Hard,Medium): ");
    if difficulty == "easy":
        numbers = list(range(1, 11))
    elif difficulty == "medium":
        numbers = list(range(10, 21))
    elif difficulty == "hard":
        numbers = list(range(22, 36))   
    else:
        print("Invalid choice! Defaulting to Easy.")  # 👈 Handle wrong input
        numbers = list(range(1, 11))
    while True:
        try:
            user_input=int(input("\nGuess number: "));
            choices=random.choice(numbers);
            diff=abs(user_input-choices)
    
            if diff==0:
                print("Correct",user_input," ",choices);
                break
            elif diff <=2:
                print("🔥 Very close!",user_input," ",choices);
            elif diff <=5:
                print("😐 Getting warmer...",user_input," ",choices);
            else:
                print("🧊 Ice cold!",user_input," ",choices);

        except ValueError:
            print("Please enter valid number");
            continue

    play_again=input("\nWant to play y/n ")
    if play_again !="y":
        print("Thanks for playing");
        break
    
