def solution(answers):
    answer = []
    student=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    correct=[0,0,0]
    for i in range(len(answers)):
        if student[0][i%5]==answers[i]:
            correct[0]+=1
        if student[1][i%8]==answers[i]:
            correct[1]+=1
        if student[2][i%10]==answers[i]:
            correct[2]+=1
    maxNum=max(correct)
    for i in range(3):
        if correct[i]==maxNum:
            answer.append(i+1)
    return answer