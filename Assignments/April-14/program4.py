# WAP to accept 5 names of cricket players from user and store in "Players.txt"

file = open("Players.txt", "w")
for i in range(1, 6):
    player_name = input(f"Enter Player-{i} Name:")
    file.write(player_name)
    file.write("\n")
print("Data Saved Successfully.")
file.close()
