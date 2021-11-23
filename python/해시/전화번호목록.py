def solution(phone_book):
    answer = True
    phone_book.sort(). 
    #만약 접두어가 존재한다면, 정렬했을때 앞뒤로 올수밖에 없다. 
    for i in range(0,len(phone_book)-1):
        if phone_book[i+1].find(phone_book[i],0, len(phone_book[i]))==0:
            answer=False
            return answer
    return answer
