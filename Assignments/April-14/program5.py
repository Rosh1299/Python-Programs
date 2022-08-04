# "WAP to accept 5 names of cricket players from user and store in ""Players.txt""
#  and print the name of the last player

file = open("Players.txt", "a")
for i in range(1, 6):
    player_name = input(f"Enter Player-{i} Name:")
    file.write(player_name)
    file.write("\n")
print("Data Saved Successfully.")
file.close()

file = open("Players.txt", "r")
data = file.readlines()
print("Name of last player in file:", data[-1])
file.close()
