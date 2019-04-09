from random import randint

print("Wanna play a game with me? ")
print("Enter 'y' : Start the Game! ")
# print("Enter any other key: exit the game")
start_game = input()

while str(start_game) == "y":
    num_max = 100
    turns = 6
    num = randint(1, num_max)
    print("Guess what integer (0~" + str(num_max) + " I am thinking now ?")
    print("You have " + str(turns) + " chances to answer!")
    bingo = False
    counter = 1
    while bingo == False:

        if int(counter) < (turns + 1):
            print("Pls enter a integer:")
            answer = input()
            counter = counter + 1

            if int(answer) < num:
                print("Too small!")
                print(" ")
            if int(answer) > num:
                print("Too large!")
                print(" ")
            if int(answer) == num:
                print("BINGO! You are right!")
                bingo = True

        else:
            print("You lose! HA HA HA!")
            bingo = True

    print(" ")
    print("Continue to play ? ")
    print("Enter 'y' : Restart the Game")
    print("Enter any other key: exit the game")
    start_game = input()
