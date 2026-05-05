import random
numbers=[1,2,3,4,5,6,7,8,9,10];
while True:
    
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




