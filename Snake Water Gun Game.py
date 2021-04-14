import random

options=['snake','water','gun']

computer_points=0
player_points=0
i=1
while(i<=10):
    computer_Select = random.choice(options)
    player_choice = input("Enter S for Snake, W for Water and G for Gun:")
    if player_choice=='S' and computer_Select=='water':
        player_points=player_points+1
    elif player_choice=='S' and computer_Select=='gun':
        computer_points=computer_points+1
    elif player_choice=='W' and computer_Select=='snake':
        computer_points=computer_points+1
    elif player_choice=='W' and computer_Select=='gun':
        player_points=player_points+1
    elif player_choice=='G' and computer_Select=='snake':
        player_points=player_points+1
    elif player_choice=='G' and computer_Select=='water':
        computer_points=computer_points+1
    elif player_choice=="S" and computer_Select=="snake":
        continue
    elif player_choice=="W" and computer_Select=='water':
        continue
    elif player_choice=="G" and computer_Select=="gun":
        continue

    print(player_points)
    print(computer_points)
    print(i)
    i=i+1




if (player_points>computer_points):
    print(f"You are the winner with {player_points} points")
elif(player_points==computer_points):
    print("Game Draw")
else:
    print(f"Computer is winner with {computer_points} points")




