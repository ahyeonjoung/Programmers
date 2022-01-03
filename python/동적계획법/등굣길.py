def solution(m, n, puddles):
    answer = 0
    matrix = [[0 for col in range(m)] for row in range(n)]
    
    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                matrix[0][0]=1
            elif i==0 or j==0:
                if [j+1,i+1] in puddles:
                    matrix[i][j]=0
                elif i==0:
                    matrix[i][j]=matrix[i][j-1]
                elif j==0:
                    matrix[i][j]=matrix[i-1][j]
            elif [j+1,i+1] in puddles:
                continue
            else:
                matrix[i][j]=(matrix[i-1][j]+matrix[i][j-1])
  
    return matrix[n-1][m-1]%1000000007