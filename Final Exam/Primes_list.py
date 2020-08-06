import math
def primes_list(N):
    '''
    N: an integer
    '''
    # Your code here
    list = []
    num = 2
    while num <= N:
        flag = False
        for prime in list[:int(math.sqrt(num))]:
            if num % prime ==0:
                flag = True
                break
        if not flag:
            list.append(num)
        num += 1
    return list

print(primes_list(2))