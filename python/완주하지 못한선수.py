from collections import Counter
def solution(participant, completion):
    counter=Counter(completion)
    counter2=Counter(participant)
    answer=''
   
   
    for word in participant:
        if counter[word]==0:
            answer=word
        if counter[word]-counter2[word]!=0:
            answer=word
    return answer

