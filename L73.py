def count_character(word, char):
    count = 0
    index = 0
    while index < len(word):
        if word[index] == char:
            count += 1
        index += 1
    return count
print(count_character("bonobos","o"))


index = 0
s = "mind the gap!"
while index <len(s) and s[index] != " ":
    index += 1
print(s[:index])
