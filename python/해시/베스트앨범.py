from collections import defaultdict
def solution(genres, plays):
    answer = []
    musics={} #장르 순
    plays_size=defaultdict(list) #노래 순
    for i in range(len(genres)):
        if genres[i] in musics:
            musics[genres[i]]+=plays[i]
            plays_size[genres[i]].append([plays[i],i])
        else:
            musics[genres[i]]=plays[i]
            plays_size[genres[i]].append([plays[i],i])

    sorted_dict = dict(sorted(musics.items(), reverse=True,key = lambda item: (item[1],item[0]))) #장르 정렬
   
    for music in sorted_dict.keys(): #장르에 따라서 
        result=plays_size[music] #리스트에 노래횟수,고유번호 저장
        result.sort(key = lambda x:(x[0]),reverse=True) #노래 정렬
        if(len(result))>=2:
            answer.append(result[0][1])
            answer.append(result[1][1])
        else:
            answer.append(result[0][1])   
    return answer