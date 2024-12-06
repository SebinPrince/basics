print("Set contains 1, 2, 3 sticks\nThe player who takes the last stick is the loser.")
p1 = input("Enter the name of Player 1: ")
p2 = input("Enter the name of Player 2: ")
stick = 16

while stick != 0:

    print(f"Sticks remaining: {stick}")
    choice = int(input(f"{p1}, the number of sticks you can take (1, 2, or 3): "))


    while choice not in [1, 2, 3] or choice > stick:
        print("Invalid choice. You can only take 1, 2, or 3 sticks, and not more than the remaining sticks.")
        choice = int(input(f"{p1}, the number of sticks you can take (1, 2, or 3): "))

    stick -= choice
    if stick == 0:
        print(f"{p1} is the loser!")
        break


    print(f"Sticks remaining: {stick}")
    choice = int(input(f"{p2}, the number of sticks you can take (1, 2, or 3): "))


    while choice not in [1, 2, 3] or choice > stick:
        print("Invalid choice. You can only take 1, 2, or 3 sticks, and not more than the remaining sticks.")
        choice = int(input(f"{p2}, the number of sticks you can take (1, 2, or 3): "))

    stick -= choice
    if stick == 0:
        print(f"{p2} is the loser!")
        break
