import random

choices = ["Rock","paper","Scissors"]
human_choice=int(input("please input choivce :"))
camputer_choice = random.randint(0,2)

print(f"human choise is {choices[human_choice]}" )
print(f"camputer choise is {choices[camputer_choice]}" )

if human_choice == 0 and camputer_choice == 2 :
    print("human win")

elif human_choice == 2 and camputer_choice == 0 :
    print("camputer win")  

elif camputer_choice>human_choice:
    print("camputer win")

elif human_choice == camputer_choice:
    print("it is draw!")

else:
    print("human win")