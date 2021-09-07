#include <string>
#include <vector>      
#include <queue>
#include <algorithm>
using namespace std;
#define INF 1e9 

vector<pair<int, int> > graph[100001];
int d1[100001]; 
int d2[100001]; 
void dijkstra(int start,int d[])
{
    priority_queue<pair<int,int>>pq;
    pq.push({0,start}); 
    d[start]=0;
    while(!pq.empty()) 
    {
        int dist = -pq.top().first; 
        int now = pq.top().second; 
        pq.pop();
        if(d[now]<dist)
            continue;
        for(int i=0; i<graph[now].size(); i++)
        {
            int cost = dist+graph[now][i].second;                                      
            if(cost<d[graph[now][i].first]) {
                d[graph[now][i].first]=cost;
                pq.push(make_pair(-cost,graph[now][i].first));
            }
        }
    }
}
int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
    int answer = 0;
    int noRide=0;
    vector <int> d4;
    fill(d1, d1 + 100001, INF);
    fill(d2, d2 + 100001, INF);
    for(long i=0;i<fares.size();i++){
        graph[fares[i][0]].push_back({fares[i][1], fares[i][2]});
        graph[fares[i][1]].push_back({fares[i][0], fares[i][2]});
    }
    dijkstra(s,d1);
    noRide+=d1[a];
    noRide+=d1[b];
    for(int i=1;i<=n;i++){
        fill(d2, d2 + 100001, INF);
        dijkstra(i,d2);
        d4.push_back(d1[i]+d2[a]+d2[b]);
    }
    int minNum=INF;
    for(int i=0;i<d4.size();i++){
        if(minNum>d4[i]&&d4[i]>0)
            minNum=d4[i];
    }
    answer=min(minNum,noRide);
    return answer;
}
