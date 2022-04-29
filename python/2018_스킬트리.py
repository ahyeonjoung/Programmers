def solution(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        stack=list(skill)
        stack.reverse()
        flag=True
        for s in list(skills):
            if s in stack:   
                if stack[-1]!=s: 
                    flag=False
                    break
                else:
                    stack.pop()
        if flag:
            answer+=1

    return answer
