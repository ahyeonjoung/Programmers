#include <string>
#include <vector> 
using namespace std; ;

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    answer.assign(N,0);
    int tmp=0; 0;
    vector <int> correct; 
    correct.assign(N+1,0);
    vector <int> trying;
    trying.assign(N+1,0);
    vector <double> temp;
    temp.assign(N+1,0.0); 
    
    for(int i=0;i<stages.size();i++){ 
        tmp=stages[i];
        for(int j=0;j<tmp;j++){
            trying[j]++;
        }
        if(tmp!=N+1)
            correct[tmp-1]++;
    }
    
    for(int i=0;i<N;i++){
        if(trying[i]!=0)
            temp[i]=(double)correct[i]/(double)trying[i];
        answer[i]=i+1;
    }
    
    for(int i=0;i<N;i++){
        for(int j=0;j<N-1-i;j++){
            if(temp[j]<temp[j+1]){
                double t=temp[j];
                temp[j]=temp[j+1];
                temp[j+1]=t;
                int k=answer[j];
                answer[j]=answer[j+1];
                answer[j+1]=k;
            }
        }
    }
    return answer;
}
