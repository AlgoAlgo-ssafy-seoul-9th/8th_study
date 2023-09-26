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



