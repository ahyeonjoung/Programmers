
def solution(new_id):
    answer = ''
    #1단계: 소문자로 치환
    new_id=new_id.lower() 
    #2단계: 허용되지 않은 문자 제거
    letter=['1','2','3','4','5','6','7','8','9','0','-','_','.']
    for i in range(len(new_id)):
        if new_id[i].islower():
            answer+=new_id[i]
        if new_id[i] in letter:
            answer+=new_id[i]
    #3단계: 마침표 치환
    while ".." in answer:
        answer=answer.replace("..",".")
    #4단계: 마침표 제거
    if len(answer)>1:
        while answer[0]=='.':
            answer=answer[1:]
        while answer[len(answer)-1]=='.':
            answer=answer[:-1]
    if len(answer)==1 and answer==".":
        answer="a" #5단계: a대입
    #6단계: 16자이상
    if len(answer)>=16:
        answer=answer[:15]
        if answer[14]=='.':
            answer=answer[:14]
    #7단계: 2자이하
    if len(answer)<=2:
        last_letter=answer[len(answer)-1]
        while len(answer)<3:
            answer+=last_letter
            
        
    return answer
