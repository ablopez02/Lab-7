def total_length(string_list):
    total = 0
    for string in string_list:
        total += len(string)
    return total
print(total_length(['queen','rules']))
print(total_length([]))
print(total_length(['balloons']))
print(total_length(["",'',"",'']))
s = "tenochtitlan"
index = 0
while index < len(s):
    index += 1
    print(s[:index])


