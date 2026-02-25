print('''
 ==========+ 
|  __  __  ||
| |  ||  | ||
| |  ||  | ||
| |__||__| |--
|  __  __()|\ Peeking in...
| |  ||  | +|
| |  ||  | ||
| |  ||  | ||
| |__||__| ||
|__________|-  ejm

''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure")
measure_one=input("left or right ?").lower()
if measure_one== "left" :
    measure_two = input("swim or wait?").lower()
    if measure_two == "wait":
        measure_three = input("Which door?(blue , red , yellow)").lower()
        if measure_three == "blue" :
            print("Eaten by beasts.\nGame Over.")
        elif measure_three == "red":
            print("Burned by fire.\nGame Over.")    
        elif measure_three == "yellow":
            print("You Win!")
        else:
            print("Game Over.")        
    else:
        print("Attacked by trout.\nGame Over.")    
else:
    print("Fall into a hole.\nGame Over.")