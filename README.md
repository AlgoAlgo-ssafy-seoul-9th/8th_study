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
# 틀림,, ㅠ
n = int(input())
first_word = list(input())
first_dict = {}
# 첫번째단어 dict 생성
for i in range(len(first_word)):
    if first_word[i] in first_dict:
        first_dict[first_word[i]] += 1
    else:
        first_dict[first_word[i]] = 1

answer = 0
cnt = 0
for i in range(n-1):
    flag = False
    check_dict = {}
    check_word = list(input())

    # 비교할 단어 dict 생성
    for j in range(len(check_word)):
        if check_word[j] in check_dict:
            check_dict[check_word[j]] += 1
        else:
            check_dict[check_word[j]] = 1

    # 아예 구성 같으면 +1 하고 넘기기
    if check_dict == first_dict:
        answer+= 1
        continue
    cnt = 0
    tmp = []

    # 길이는 같은데 구성이 다르다면 ?
    if len(first_word) == len(check_word):
        cnt = 0

        # 첫번째단어하나씩 돌리면서 비교할단어 하나씩 삭제 (1개남으면 비슷한단어)
        for k in range(len(first_word)):
            if first_word[k] in check_word:
                check_word.remove(first_word[k])

    # 삭제했더니 1개남았다 ? +1 하고 넘기기
        if len(check_word)==1:
            answer+=1
            continue

    # word2가 무조건 길게끔 만들어줬음 (편한 비교를 위해)
    if len(first_word) > len(check_word):
        tmp = first_word
        first_word = check_word
        check_word = tmp
    check_word.sort()
    first_word.sort()
    check_word_copy = check_word[:]


    # 하나씩 빼가면서 비교
    for m in range(len(check_word)):
        check_word.pop(m)
        if check_word == first_word:
            flag = True
            break
        else:
            check_word = check_word_copy[:]

    # 끝났을떄 flag == True면 +1 하고 끝
    if flag == True:
        answer+=1
print(answer)
```

## [상미](<./비슷한 단어/상미.py>)

```py
## 백준 2607_ 비슷한단어

# import collections

# N = int(input())
# words = list(input() for _ in range(N))

# n = 1
# target = words[0]  # 비교 기준 단어
# letters_t = []
# for t in target:
#     letters_t.append(t)
# dict_t = collections.Counter(letters_t)
# ans = 0

# while n < N:
#     compare = words[n]
#     letters_c = []
#     cnt = 0
#     diff = 0
#     for i in compare:
#         letters_c.append(i)
#     dict_c = collections.Counter(letters_c)
#     for i in range(len(letters_t)):
#         if dict_t[letters_t[i]] != dict_c[letters_t[i]]:
#             diff += abs(dict_t[letters_t[i]] - dict_c[letters_t[i]])
#             cnt += 1    # 개수가 다른게 있으면 cnt + 1
#         if letters_t[i] not in dict_c.keys():   # 타겟의 알파벳이 비교 문자에 없으면
#             cnt += 1
#     n += 1  # 다음 비교 단어 설정

#     if cnt < 2 and diff <=1:     # 개수 다른게 0개나 1개면  ans + 1
#         ans += 1

# print(ans)


import collections

N = int(input())
words = [input() for _ in range(N)]

target = words[0]
dict_t = collections.Counter(target)
ans = 0

for compare in words[1:]:
    dict_c = collections.Counter(compare)
    diff = sum((dict_t - dict_c).values()) + sum((dict_c - dict_t).values())

    if len(target) == len(compare):  # 같은 길이일 때
        if diff <= 2:
            ans += 1
    else:  # 길이가 다를 때
        if abs(len(target) - len(compare)) == 1 and diff <= 1:
            ans += 1

print(ans)

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
#시간초과,,
# k개 포함하는 가장짧은 연속 문자열의 길이
# 둘다 양끝이 특정문자이긴해야해
import sys
# 인덱스로풀어보자..................
from collections import defaultdict
def shortlong(str_dict):
    global minn
    global maxx
    for idx in str_dict.values():
        for j in range(len(idx)-K+1):
            # start = idx[j]
            # end = idx[j+K-1]
            tmp = idx[j+K-1]-idx[j]
            minn = min(tmp+1,minn)
            maxx = max(tmp+1,maxx)
    print(minn,maxx)

T = int(sys.stdin.readline())

for _ in range(T):
    minn = 10001
    maxx = 0
    W = list(sys.stdin.readline())
    K = int(sys.stdin.readline())
    str_dict = defaultdict(list)
    for i in range(len(W)):
        if W.count(W[i]) >=K:
            str_dict[W[i]].append(i)
    if str_dict:
        shortlong(str_dict)
    else:
        print(-1)

```

## [상미](./문자열%20게임2/상미.py)

```py
# ## 백준 20437 _ 문자열게임2

# T = int(input())
# for _ in range(T):
#     word = input()
#     cnt_t = int(input())
#     left = 0
#     right = 1
#     min_len = 10000
#     while left< len(word):
#         # 3번
#         # 문자열의 첫 글자와 막 글자가 다르면
#         if word[left] != word[right]:
#             # 막 글자 우로 한 칸
#             right += 1
#             # 가다가 끝에 도달하면 첫 글자 우로 한칸
#             if right == len(word):
#                 left += 1
#                 right = left + 1
#         # 첫 글자와 막 글자 같으면
#         else:
#             # 해당 문자열에서 이 글자 몇 갠지 세기
#             cnt = word[left:right].count(word[left])
#             # 개수가 원하는 개수면
#             if cnt == cnt_t:
#                 # 문자열 길이 구해서 최솟값과 비교
#                 leng = right - left
#                 if leng < min_len:
#                     min_len = leng
#         # for w in word[left:right]:

#         # 4번
#         # if word[left] == word[right]:
#     print(min_len)


T = int(input())
for _ in range(T):
    word = input()
    K = int(input())

    # 각 문자의 위치 정보 저장
    position = {}
    for i, w in enumerate(word):
        if w in position:
            position[w].append(i)
        else:
            position[w] = [i]

    min_len = float('inf')
    max_len = -1

    for key, values in position.items():
        if len(values) >= K:
            for i in range(len(values) - K + 1):
                length = values[i + K - 1] - values[i] + 1
                min_len = min(min_len, length)
                max_len = max(max_len, length)

    if min_len == float('inf'):
        print(-1)
    else:
        print(min_len, max_len)

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
