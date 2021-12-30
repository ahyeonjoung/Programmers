def solution(n, lost, reserve):
    answer = 0
    length=len(reserve)
    #전처리
    set_lost=list(set(lost)-set(reserve)) #여별이 있는 도난당한사람
    set_reserve=list(set(reserve)-set(lost))
    lost.sort() #정렬후 왼쪽부터 탐색
    reserve.sort()
    #탐색
    for i in set_lost:
        if i-1 in set_reserve:
            set_reserve.remove(i-1)
        elif i+1 in set_reserve:
            set_reserve.remove(i+1)

    answer=n-len(lost)+length-len(set_reserve)

    return answer