import random
numbers=[1,2,3,4,5,6,7,8,9,10];
while True:
    
    user_input=int(input("\nGuess number: "));
    choices=random.choice(numbers);
    
    if user_input==choices:
        print("\nYou have guessed the correct number which is ")
        print("Computer generated number was ",choices)
        print("Your number was ",user_input)
        break;
    else:
        print("\nYou have not guessed the correct number ")
        print("Computer generated number was ",choices)
        print("Your number was",user_input)



