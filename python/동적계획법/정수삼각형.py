def solution(triangle):
    answer = 0
    for i in triangle:
        i.append(0)
        i.insert(0,0)
    
    for i in range(1,len(triangle)):
        for j in range(1,i+2):
            triangle[i][j]+=max(triangle[i-1][j-1],triangle[i-1][j])
    answer=max(triangle[-1])
    
    return answer