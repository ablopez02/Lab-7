def w_triangle(word):
    length = len(word)
    while length > 0:
        print(word[:length])
        length -= 1
w_triangle("abracadabra")
