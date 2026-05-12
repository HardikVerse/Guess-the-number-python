import random

num = random.randint(1,100)


guess = 0

print("Guess the number between 1 to 100.")


while True:
    user_num = int(input("Enter number : "))
    if(user_num > num):
        print("Lower number please\n")
        guess += 1

    elif(user_num < num):
        print("Higher number please\n")
        guess += 1

    elif(user_num == num):
        print(f"You have guessed the number {num} correctly in {guess} attempts.")
        break


with open("guess.txt") as f:
    score = f.read()
    if (score != ""):
        score = int(score)

        if(score > guess):
            print("This is new Score")
            with open("guess.txt", "w") as f:
                f.write(str(guess))

    else:
        with open("guess.txt", "w") as f:
            f.write(str(guess))
            print("This is New Score")
        
    
    

