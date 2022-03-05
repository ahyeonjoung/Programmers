def solution(lottos, win_nums):
    answer = []
    temp=0
    zero=0
    dic={6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    for lotto in lottos:
        if lotto in win_nums:
            temp+=1
        if lotto==0:
            zero+=1
  
    answer.append(dic[temp+zero])
    answer.append(dic[temp])
    return answer