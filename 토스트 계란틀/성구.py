'''
1<= n<=50
1<=L<=R<=100
0<= 계란 양<=100
계란 이동 총수 <= 2000
'''
import sys
from collections import deque
input = sys.stdin.readline

# input
n, L, R = map(int, input().split())
eggs = [list(map(int, input().split())) for _ in range(n)]

# define
dir = [(0,1), (1,0), (-1,0), (0,-1)]


def bfs(y,x):
    # define
    que = deque([(y,x)])
    egg = eggs[y][x]
    eggs_lst = []
    # bfs 
    while que:
        i, j = que.popleft()
        for di, dj in dir:
            ni, nj = i+di, j+dj
            if 0<= ni<n and 0<=nj<n and L <= abs(eggs[ni][nj]-eggs[i][j])<=R and not visited[ni][nj]:
                visited[ni][nj] = 1
                # 계란물 총량
                egg += eggs[ni][nj]
                # 위치
                eggs_lst.append((ni,nj))
                que.append((ni,nj))
    # 위치가 있으면
    if len(eggs_lst):
        # '나'도 껴줘
        eggs_lst.append((y,x))
        # 벽 허물고 같아진 계란물
        newEgg = egg // len(eggs_lst)
        # 위치에 적용
        for i, j in eggs_lst:
            eggs[i][j] = newEgg
        return 1
    else:
        return 0 
    

for cnt in range(2001):
    # 변화가 있는지 판단
    change = 0
    # 방문을 턴당으로 판별
    visited = [[0] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if not visited[y][x]:
                visited[y][x] = 1
                # 변화가 있으면 1 없으면 0
                change += bfs(y,x)
    # 변환 없으면 중단
    if not change:
        print(cnt)
        break