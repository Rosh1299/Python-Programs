# WAP to accept a name and search character from user and print at which index the character is occuring
# Example :- Name is ""Nilesh"" so now ask user to search for some character 
# assume that user have entered ""i"" so output will be ""i is found at 1st index"".
# assume that user have entered ""w"" so output will be ""w is not in the name "".


word = input("Enter any word:")
char = input("Enter character to search in word:")

count = 0
if char in word:
    for i in word.lower():
        if char.lower() == i:
            index = count
            print(f"{char} is found at index {index}.")
            break
        else:
            count += 1
else:
    print(f"{char} is not found in a word.")
