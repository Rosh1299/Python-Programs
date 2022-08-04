# sentence = "i like python i like java too"
sentence = input("Enter sentence:")

wordlist = sentence.split(' ')

word_count = {}

for i in wordlist:
    if i not in word_count:
        word_count[i] = 1
    else:
        word_count[i] += 1
print(word_count)

for i in word_count.items():
    if i[1] == 1:
        print(i[0])
