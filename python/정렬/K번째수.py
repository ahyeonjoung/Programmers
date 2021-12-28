def solution(array, commands):
    answer = []    
    for co in commands:
        temp=[]
        temp=array[co[0]-1:co[1]]
        temp.sort()
        answer.append(temp[co[2]-1])

    return answer