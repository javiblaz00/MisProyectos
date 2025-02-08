import random as rand

def get_guess():
    guess = int(input("Enter a number between 1 - 999: "))
    return guess

def lotery():
    result = rand.randrange(1,999,1)
    return result
    
def main():
    guess = get_guess()
    result = lotery()
    print("Lotery is:", result)
    print("Your guess is:", guess)
    if guess == result:
        print("You won")
    else:
        print("Try again!")
        
main()