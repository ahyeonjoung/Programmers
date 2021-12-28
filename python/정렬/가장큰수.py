def solution(numbers):
    answer = ''
    num = list(map(str, numbers)) 
    num.sort(key = lambda x : x*3, reverse = True)


    return str(int(''.join(num))) #000인 경우방지