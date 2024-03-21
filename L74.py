def until_dot(s):
    index = 0
    while index < len(s) and s[index] != ".":
        index += 1
    print(s[:index])
until_dot( "This is a sentence. This is another.")

x= "this is a sentence. njnjfnj"

#another way of doing it
print(x[:x.index(".")])






