adj = []
visited = [False] * 1001

def DFS(u):
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            DFS(v)

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)
    DFS(1)
    degree = 0
    for i in range(1, n + 1):
        if visited[i]:
            degree += 1
    if degree == n:
        print('NO')
    else:
        print('YES')