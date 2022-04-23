def solution(m, musicinfos):
    answer =[]
    dic={}
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    for music in musicinfos:
        start,end,name,song=music.split(',')
        eh,em=end.split(':')
        sh,sm=start.split(':')
        time=int(eh)*60+int(em)-int(sh)*60-int(sm)
        song = song.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        if len(song)>=time:
            dic[name]=song[:time]
        else:
            dic[name]=song*(time//len(song))+song[:time%len(song)]
    for key in dic.keys():
        if m in dic[key]:
            answer.append((key,len(dic[key])))
    if answer:
        answer.sort(key=lambda x:x[1], reverse=True)
        return answer[0][0]
    return '(None)'
