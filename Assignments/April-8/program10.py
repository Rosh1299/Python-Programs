num = int(input("Enter any number:"))

digit_in_word = {0: "Zero ", 1: "One ", 2: "Two ", 3: "Three ",
                 4: "Four ", 5: "Five ", 6: "Six ", 7: "Seven ", 8: "Eight ", 9: "Nine "}

num_in_word = ""

for i in str(num):
    num_in_word += digit_in_word[int(i)]
print(num_in_word)
