# 8th_study

[백준 문제집](https://www.acmicpc.net/workbook/view/16888)

[코드트리 문제](https://www.codetree.ai/training-field/frequent-problems/problems/toast-eggmold/description?page=1&pageSize=20&name=%ED%86%A0%EC%8A%A4%ED%8A%B8)

<br><br>

# 토스트 계란틀

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](<./토스트 계란틀/민웅.py>)

```py
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

```

## [병국](<./토스트 계란틀/병국.py>)

```py

```

## [상미](<./토스트 계란틀/상미.py>)

```py

```

## [서희](<./토스트 계란틀/서희.py>)

```py

```

## [성구](<./토스트 계란틀/성구.py>)

```py
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
```

</div>

</details>

<br><br>

# 비슷한 단어

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](<./비슷한 단어/민웅.py>)

```py

```

## [병국](<./비슷한 단어/병국.py>)

```py

```

## [상미](<./비슷한 단어/상미.py>)

```py

```

## [서희](<./비슷한 단어/서희.py>)

```py

```

## [성구](<./비슷한 단어/성구.py>)

```py

```

</div>

</details>

<br><br>

# 문자열 게임2

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](./문자열%20게임2/민웅.py)

```py
# 20437_문자열게임2_stringgame2
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    W = input().strip()
    K = int(input())

    s_dict = {}
    l_dict = {}

    m_value = [float('inf'), '']
    M_value = [0, '']

    if K == 1:
        m_value = [0, 'pass']
        M_value = [0, 'pass']
    else:
        for i in range(len(W)):
            w = W[i]
            if w in s_dict.keys():
                s_dict[w].append(i)
                l_dict[w] += 1
                if l_dict[w] >= K:
                    temp = s_dict[w][-1] - s_dict[w][0]
                    if temp < m_value[0]:
                        m_value = [temp, w]
                    if temp > M_value[0]:
                        M_value = [temp, w]
                    s_dict[w].popleft()
                    l_dict[w] -= 1
            else:
                s_dict[w] = deque()
                s_dict[w].append(i)
                l_dict[w] = 1

    if m_value[1] != '':
        print(m_value[0]+1, M_value[0]+1)
    else:
        print(-1)


```

## [병국](./문자열%20게임2/병국.py)

```py

```

## [상미](./문자열%20게임2/상미.py)

```py

```

## [서희](./문자열%20게임2/서희.py)

```py

```

## [성구](./문자열%20게임2/성구.py)

```py

```

</div>

</details>

<br><br>

# 성냥개비

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](./성냥개비/민웅.py)

```py
# 3687_성냥개비_matchstick
import sys
input = sys.stdin.readline
# 2 5 5 4 5 6 3 7 6 6
N = int(input())

ms = [0, 0, 1, 7, 4, 2, 0, 8]


for _ in range(N):
    num = int(input())
    if num > 3:
        temp_num = num
        temp = ''
        while temp_num > 3:
            temp = temp + '1'
            temp_num -= 2
        if temp_num == 2:
            M_value = int('1' + temp)
        else:
            M_value = int('7' + temp)
    else:
        M_value = ms[num]

    if num <= 7:
        if num != 6:
            m_value = ms[num]
        else:
            m_value = 6
    elif num == 10:
        m_value = 22
    elif num == 11:
        m_value = 20
    elif num == 17:
        m_value = 200
    else:
        temp_num = num
        temp2 = ''
        while temp_num > 8 and temp_num != 10 and temp_num != 11 and temp_num != 17:
            temp2 += '8'
            temp_num -= 7
        if temp_num == 8:
            m_value = int('10'+temp2)
        elif temp_num == 6:
            m_value = int('6'+temp2)
        elif temp_num == 10:
            m_value = int('22'+temp2)
        elif temp_num == 11:
            m_value = int('20'+temp2)
        elif temp_num == 17:
            m_value = int('200'+temp2)
        else:
            m_value = int(str(ms[temp_num])+temp2)

    print(m_value, M_value)

```

## [병국](./성냥개비/병국.py)

```py

```

## [상미](./성냥개비/상미.py)

```py

```

## [서희](./성냥개비/서희.py)

```py

```

## [성구](./성냥개비/성구.py)

```py

```

</div>

</details>

<br><br>
