def reverse(text):
    reversestr = []
    for l in range(len(text), 0, -1):
        reversestr.append(text[l-1])
    return "".join(reversestr)
