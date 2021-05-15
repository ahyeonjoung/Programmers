#include <string>
#include <vector>
#include <algorithm> 
 
using namespace std;

 char number[18] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                   'A', 'B', 'C', 'D', 'E', 'F'};  //16진수까지의 숫자
  
string convert(int num, int n){ //숫자->n    
    string st; 
    if(num == 0){   
        return "0"; 
    }
    while(num > 0){ 
        st += number[num % n]; 
        num /= n;      
    } 
    reverse(st.begin(), st.end());      
    return st;     
}


string solution(int n, int t, int m, int p) {
    string answer = "";   //내 차례
    string temp=""; //모든 
    for(int num = 0; temp.size() <= m*t; num++){
        string ngame = convert(num, n); 
        temp += ngame;
    }
    
    for(int i = 0; i < t; i++){
        answer += temp.at((m*i)+(p-1));  
    }
    return answer;
}
