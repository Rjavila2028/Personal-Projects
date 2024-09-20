'''
Author: Ricardo Avila
KUID: 3175035
Date Made: 9/18/24
Last modified: 9/18/24
Purpose: Be able to play games with made dice
'''

play = 'y'
balance = 1000
import Dice


print("What game do you want to play?")
print('1. Under or Over Seven')
print('2. Higher or lower')
    
game = int(input("Enter Number: "))

while(game != 1 and game != 2 and game != 3):
    game = int(input("Please enter a proper number: "))

while(balance > 0 and play == 'y' or play == 'Y'):
    print("Balance = $" + str(balance))
    dice_total = 0
            
    if(game == 1):
        print("What do you want to bet?")
        print("1. under pays 1:1")
        print("2. even pays 4:1")
        print("3. over pays 1:1")
        bet = int(input("Enter a number: "))
        while(bet != 1 and bet != 2 and bet != 3):
            bet = int(input("Please enter a proper number: "))
        wager = int(input("How much do you want to bet? "))
        while(wager > balance or wager <= 0):
            wager = int(input("Enter a bet within your balance: "))
        
        roll = Dice.roll_dice(2)
        dice_value = Dice.generate_dice_faces_diagram(roll)
        print(dice_value)
        
        
        for num in roll:
            dice_total += num
        print("Dice total =",dice_total)
        if(bet == 1 and dice_total < 7):
            print("You Win")
            balance += wager
        elif(bet == 1 and dice_total >= 7):
            print("You Lose")
            balance -= wager
        elif(bet == 2 and dice_total < 7):
            print("You Lose")
            balance -= wager
        elif(bet == 2 and dice_total > 7):
            print("You Lose")
            balance -= wager
        elif(bet == 2 and dice_total == 7):
            print("You Win")
            balance += wager * 4
        elif(bet == 3 and dice_total <= 7):
            print("You lost")
            balance -= wager
        else:
            print("You win")
            balance += wager

    elif(game == 2):
        play2 = 'y'
        winnings = 0
        num_dice = int(input("Do you want to play with 1 or 2 dice? "))
        while(num_dice != 1 and num_dice != 2):
            num_dice = int(input("Please enter 1 or 2: "))

        roll = Dice.roll_dice(num_dice)
        dice_value = Dice.generate_dice_faces_diagram(roll)
        if(num_dice == 1):
            wager = int(input("How much do you want to bet? "))
            while(wager > balance or wager <= 0):
                wager = int(input("Enter a bet within your balance: "))
            winnings = wager
            balance -= wager
            print("Rule: If it is the same as the last numbers both will hit")
            print("Rule: Higher for 1 and Lower for 6 do not include ties")
            while(play2 == 'y' or play2 == 'Y'):
                dice_value2 = dice_value
                roll2 = 0
                roll3 = 0
                for num in roll:
                    roll2 += num
                print(dice_value2)
                if(roll2 == 1):
                    print("Over Pays 1.2X")
                    print("Under Pays 6X")
                elif(roll2 == 2):
                    print("Over Pays 1.2X")
                    print("Under Pays 3X")
                elif(roll2 == 3):
                    print("Over Pays 1.5X")
                    print("Under Pays 2X")
                elif(roll2 == 4):
                    print("Over Pays 2X")
                    print("Under Pays 1.5X")
                elif(roll2 == 5):
                    print("Over Pays 3X")
                    print("Under Pays 1.2X")
                else:
                    print("Over Pays 6X")
                    print("Under Pays 1.2X")
                
                print("What do you want to bet?")
                print("1. Over")
                print("2. Under")
                bet = int(input("Enter a number: "))
                while(bet != 1 and bet != 2):
                    bet = int(input("Please enter a proper number: "))
                roll = Dice.roll_dice(num_dice)
                dice_value = Dice.generate_dice_faces_diagram(roll)
                for num in roll:
                    roll3 += num
                win = 'y'
                print(dice_value)
                if(roll2 == 1):
                    if(bet == 1):
                        if(roll2 < roll3):
                            print("You Win")
                            winnings *= 1.2
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                    else:
                        if(roll2 >= roll3):
                            print("You Win")
                            winnings *= 6
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                elif(roll2 == 2):
                    if(bet ==1):
                        if(roll2 <= roll3):
                            print("You Win")
                            winnings *= 1.2
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                    else:
                        if(roll2 >= roll3):
                            print("You Win")
                            winnings *= 3
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                elif(roll2 == 3):
                    if(bet == 1):
                        if(roll2 <= roll3):
                            print("You Win")
                            winnings *= 1.5
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                    else:
                        if(roll2 >= roll3):
                            print("You Win")
                            winnings *= 2
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                elif(roll2 == 4):
                    if(bet == 1):
                        if(roll2 <= roll3):
                            print("You Win")
                            winnings *= 2
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                    else:
                        if(roll2 >= roll3):
                            print("You Win")
                            winnings *= 1.5
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                elif(roll2 == 5):
                    if(bet == 1):
                        if(roll2 <= roll3):
                            print("You Win")
                            winnings *= 3
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                    else:
                        if(roll2 >= roll3):
                            print("You Win")
                            winnings *= 1.2
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                else:
                    if(bet == 1):
                        if(roll2 <= roll3):
                            print("You Win")
                            winnings *= 6
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                    else:
                        if(roll2 > roll3):
                            print("You Win")
                            winnings *= 1.2
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                if(win == 'y'):
                    play2 = input("Do you want to continue streak?(y/n) ")
                else:
                    play2 = 'n'
                if(play2 != 'y'):
                    temp_winnings = int(winnings*100)
                    winnings = temp_winnings/100
                    balance += winnings
        else:
            wager = int(input("How much do you want to bet? "))
            while(wager > balance or wager <= 0):
                wager = int(input("Enter a bet within your balance: "))
            winnings = wager
            balance -= wager
            print("Rule: If it is the same as the last numbers both will hit")
            print("Rule: Higher for 1 and Lower for 6 do not include ties")
            print("Rule: You are betting on dice total")
            while(play2 == 'y' or play2 == 'Y'):
                dice_value2 = dice_value
                roll2 = 0
                roll3 = 0
                for num in roll:
                    roll2 += num
                print(dice_value2)
                if(roll2 == 2):
                    print("Over Pays 1.1X")
                    print("Under Pays 11X")
                elif(roll2 == 3):
                    print("Over Pays 1.1X")
                    print("Under Pays 5.5X")
                elif(roll2 == 4):
                    print("Over Pays 1.2X")
                    print("Under Pays 3.7X")
                elif(roll2 == 5):
                    print("Over Pays 1.38X")
                    print("Under Pays 2.75X")
                elif(roll2 == 6):
                    print("Over Pays 1.58X")
                    print("Under Pays 2.2X")
                elif(roll2 == 7):
                    print("Over Pays 1.9X")
                    print("Under Pays 1.9X")
                elif(roll2 == 8):
                    print("Over Pays 2.2X")
                    print("Under Pays 1.58X")
                elif(roll2 == 9):
                    print("Over Pays 2.75X")
                    print("Under Pays 1.38X")
                elif(roll2 == 10):
                    print("Over Pays 3.7X")
                    print("Under Pays 1.2X")
                elif(roll2 == 11):
                    print("Over Pays 5.5X")
                    print("Under Pays 1.1X")
                else:
                    print("Over Pays 11X")
                    print("Under Pays 1.1X")
                
                print("What do you want to bet?")
                print("1. Over")
                print("2. Under")
                bet = int(input("Enter a number: "))
                while(bet != 1 and bet != 2):
                    bet = int(input("Please enter a proper number: "))
                roll = Dice.roll_dice(num_dice)
                dice_value = Dice.generate_dice_faces_diagram(roll)
                for num in roll:
                    roll3 += num
                win = 'y'
                print(dice_value)
                if(roll2 == 2):
                    if(bet == 1):
                        if(roll2 < roll3):
                            print("You Win")
                            winnings *= 1.1
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                    else:
                        if(roll2 >= roll3):
                            print("You Win")
                            winnings *= 11
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                elif(roll2 == 3):
                    if(bet ==1):
                        if(roll2 <= roll3):
                            print("You Win")
                            winnings *= 1.1
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                    else:
                        if(roll2 >= roll3):
                            print("You Win")
                            winnings *= 5.5
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                elif(roll2 == 4):
                    if(bet == 1):
                        if(roll2 <= roll3):
                            print("You Win")
                            winnings *= 1.2
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                    else:
                        if(roll2 >= roll3):
                            print("You Win")
                            winnings *= 3.7
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                elif(roll2 == 5):
                    if(bet == 1):
                        if(roll2 <= roll3):
                            print("You Win")
                            winnings *= 1.38
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                    else:
                        if(roll2 >= roll3):
                            print("You Win")
                            winnings *= 2.75
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                elif(roll2 == 6):
                    if(bet == 1):
                        if(roll2 <= roll3):
                            print("You Win")
                            winnings *= 1.58
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                    else:
                        if(roll2 >= roll3):
                            print("You Win")
                            winnings *= 2.2
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                elif(roll2 == 7):
                    if(bet == 1):
                        if(roll2 <= roll3):
                            print("You Win")
                            winnings *= 1.9
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                    else:
                        if(roll2 >= roll3):
                            print("You Win")
                            winnings *= 1.9
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                elif(roll2 == 8):
                    if(bet ==1):
                        if(roll2 <= roll3):
                            print("You Win")
                            winnings *= 2.2
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                    else:
                        if(roll2 >= roll3):
                            print("You Win")
                            winnings *= 1.58
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                elif(roll2 == 9):
                    if(bet == 1):
                        if(roll2 <= roll3):
                            print("You Win")
                            winnings *= 2.75
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                    else:
                        if(roll2 >= roll3):
                            print("You Win")
                            winnings *= 1.38
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                elif(roll2 == 10):
                    if(bet == 1):
                        if(roll2 <= roll3):
                            print("You Win")
                            winnings *= 3.7
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                    else:
                        if(roll2 >= roll3):
                            print("You Win")
                            winnings *= 1.2
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                elif(roll2 == 11):
                    if(bet == 1):
                        if(roll2 <= roll3):
                            print("You Win")
                            winnings *= 5.5
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                    else:
                        if(roll2 >= roll3):
                            print("You Win")
                            winnings *= 1.1
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                else:
                    if(bet == 1):
                        if(roll2 <= roll3):
                            print("You Win")
                            winnings *= 11
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                    else:
                        if(roll2 > roll3):
                            print("You Win")
                            winnings *= 1.1
                        else:
                            print("You Lose")
                            winnings = 0
                            win = 'l'
                if(win == 'y'):
                    play2 = input("Do you want to continue streak?(y/n) ")
                else:
                    play2 = 'n'
                if(play2 != 'y'):
                    temp_winnings = int(winnings*100)
                    winnings = temp_winnings/100
                    balance += winnings
        
        

    if balance > 0:
        play = input("Do you want to play again?(y/n) ")

if(balance > 0):
    print("Thanks for playing")
else:
    print("Sorry you ran out of money")
