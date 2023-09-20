# 8th_study

[백준 문제집](https://www.acmicpc.net/workbook/view/16888)

[코드트리 문제](https://www.codetree.ai/training-field/frequent-problems/problems/toast-eggmold/description?page=1&pageSize=20&name=%ED%86%A0%EC%8A%A4%ED%8A%B8)

<br><br><br>

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

```

</div>

</details>

<br><br><br>

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

<br><br><br>

# 문자열 게임2

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](./문자열%20게임2/민웅.py)

```py

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

<br><br><br>

# 성냥개비

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](<./성냥개비/민웅.py>)

```py

```

## [병국](<./성냥개비/병국.py>)

```py

```

## [상미](<./성냥개비/상미.py>)

```py

```

## [서희](<./성냥개비/서희.py>)

```py

```

## [성구](<./성냥개비/성구.py>)

```py

```

</div>

</details>

<br><br><br>
