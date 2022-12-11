input = [l.strip() for l in open("i.txt")]

def letter_to_priority(c):
    if c.islower():
        return ord(c)-ord('a') + 1
    else:
        return ord(c)-ord('A') + 27

priority = 0
for word in input:
    word1 = word[slice(0, len(word)//2)]
    word2 = word[slice(len(word)//2, len(word))]
    for i in range(len(word1)):
        if not word1.count(word1[i]) == 0 and not word2.count(word1[i]) == 0:
            priority += letter_to_priority(word1[i])
            break

print("P1:", priority) 

priority = 0
for i in range(0, len(input), 3):
    word1 = input[i]
    word2 = input[i+1]
    word3 = input[i+2]
    for i in range(len(word1)):
        if not word1.count(word1[i]) == 0 and not word2.count(word1[i]) == 0 and not word3.count(word1[i]) == 0:
            priority += letter_to_priority(word1[i])
            break

print("P2:", priority)