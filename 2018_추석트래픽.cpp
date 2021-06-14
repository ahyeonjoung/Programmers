#include <string>
#include <vector> 
 
using namespace std;

int solution(vector<string> lines) {
    int answer = 0;
   vector<int> start_t, end_t;
    
    for(int i = 0; i < lines.size(); i++) 
    {     
        string h, m, s, ms; //시간, 분, 초, 소수점초  
        int ih, im, is, process;  
        
        lines[i].pop_back(); //마지막원소 s제거
        h = lines[i].substr(11, 2); //시간
        m = lines[i].substr(14, 2); //분
        s = lines[i].substr(17, 2); //초
        ms = lines[i].substr(20, 3); //소수점초
        process = stof(lines[i].substr(24, 5)) * 1000; //처리시간
        
        ih = stoi(h) * 3600 * 1000; //시간->소수점초
        im = stoi(m) * 60 * 1000; //분->소수점초
        is = stoi(s) * 1000 + stoi(ms); //초->소수점초
        
        start_t.push_back(ih + im + is - process + 1); //시작초 
        end_t.push_back(ih + im + is); //끝초
    }
    
    for(int i = 0; i < lines.size(); i++)
    {
        int end_time = end_t[i] + 1000; //1초동안의 트래픽측정
        int count = 0;
        
        for(int j = i; j < lines.size(); j++)
        {
            if(start_t[j] < end_time)
                count++;
        }
        
        if(answer < count)
            answer = count; //최대값
    }
    return answer;
}
