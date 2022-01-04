count=0

def dfs(idx, value, numbers, target):
    #전역변수 count 사용 선언
    global count 
    length = len(numbers)
    
    # 재귀함수 base case
    if idx == length:
        if value == target:
            count+= 1
        return 
    
    # 재귀함수 recursive case
    dfs(idx+1, value + numbers[idx],numbers, target)
    dfs(idx+1, value - numbers[idx],numbers, target)


def solution(numbers, target):
    global count
    dfs(0,0, numbers, target)
    
    return count
