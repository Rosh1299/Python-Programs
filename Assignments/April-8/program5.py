
sentence = input("Enter sentence:")

char_count = {"Small letter": 0, "Capital letter": 0,
              "Space": 0, "Digits": 0, "Special character": 0}
for char in sentence:
    if char.islower():
        char_count["Small letter"] += 1
    elif char.isupper():
        char_count['Capital letter'] += 1
    elif char == ' ':
        char_count['Space'] += 1
    elif char.isdigit():
        char_count['Digits'] += 1
    else:
        char_count["Special character"] += 1

for key, value in char_count.items():
    print(f"{key}:{value}")
