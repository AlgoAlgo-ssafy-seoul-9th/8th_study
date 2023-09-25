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


