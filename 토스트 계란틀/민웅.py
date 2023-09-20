import sys
import math
from collections import deque
input = sys.stdin.readline
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(a, b):
    global visited
    global eggs
    temp = eggs[a][b]
    q = deque()
    q.append([a, b])
    temp_list = [[a, b]]
    while q:
        x, y = q.popleft()
        for d in dxy:
            nx = x + d[0]
            ny = y + d[1]
            
            if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                if visited[nx][ny] == 0:
                    if L <= abs(eggs[x][y] - eggs[nx][ny]) <= R:
                        q.append([nx, ny])
                        temp += eggs[nx][ny]
                        temp_list.append([nx, ny])
                        visited[nx][ny] = 1
    ans = int(math.floor(temp/len(temp_list)))

    return [ans, temp_list]



n, L, R = map(int, input().split())

eggs = [list(map(int, input().split())) for _ in range(n)]

# print(eggs)
cnt = 0

while True:
    visited = [[0]*n for _ in range(n)]
    changed = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                check = bfs(i, j)

                if len(check[1]) != 1:
                    changed = True
                    for v in check[1]:
                        eggs[v[0]][v[1]] = check[0]
    
    if not changed:
        break
    else:
        cnt += 1
        
print(cnt)