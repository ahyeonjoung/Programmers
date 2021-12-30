def solution(brown, yellow):
    answer = []
    total=brown+yellow
    for i in range(2,brown+1):
        if total%i==0:
            j=total/i #나머지길이
            if (j-2)*(i-2)==yellow: #안에속한 중간블록
                answer.append(i)
                answer.append(j)
                break
    answer.sort(reverse=True)  #가로길이 > 세로길이   
    return answer