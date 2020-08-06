def sum_digits(s):
    n = 0
    notint=0
    for char in s:
        try:
            n += int(char)
        except:
            notint += 1
    if notint != len(s):
        return n
    else:
        raise ValueError
    
print(sum_digits("na1231e:"))