def solution(n, k):
    answer = 0
    number=list(make_n(n,k))
    tempNum=''
    for i in number:
        if i=='0':
            if len(tempNum)!=0:
                if is_prime_number(int(tempNum)):
                    answer+=1
                tempNum=''
        else:
            tempNum+=i
    if len(tempNum)!=0:
        if is_prime_number(int(tempNum)):
            answer+=1
    return answer


def make_n(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 

import math
def is_prime_number(x):
    if x==1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False 
    return True 
