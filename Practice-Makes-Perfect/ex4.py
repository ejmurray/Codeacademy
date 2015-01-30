def digit_sum(n):
    s = str(n)
    total = 0
    lst = []
    for i in s:
        lst.append(int(i))
        total = sum(lst)
    return total
# this code seems idiomatically more sensible and easier to read
