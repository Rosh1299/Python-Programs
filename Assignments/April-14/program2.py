# WAP to print the Reader's Info from a file "Readers.txt"

file = open('Readers.txt', 'r')
data = file.read()
print(data)
file.close()
