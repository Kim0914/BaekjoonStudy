import sys
input = sys.stdin.readline

def dfs(v):
    print(v, end = ' ') # 방문한 vertex 출력
    visited[v] = 1 # 방문한 vertex를 방문했다고 체크
    for i in range(1, n+1): # 1 ~ n 전체 vertex를 체크하며
        if visited[i] == 0 and mat[v][i] == 1: # 방문하지 않은 vertex이고 v 정점과 연결되어 있으면
            dfs(i)

def bfs(v):
    queue = [v]
    visited[v] = 0
    while queue:
        v = queue[0]
        print(v, end = ' ')
        del(queue[0])
        for i in range(1, n+1):
            if visited[i] == 1 and mat[v][i] == 1:
                queue.append(i)
                visited[i] = 0
                

n, m, v = map(int, input().split())
mat = [[0] * (n + 1) for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(m):
    i, j = map(int, input().split())
    mat[i][j] = 1
    mat[j][i] = 1

dfs(v)
print()
bfs(v)
    