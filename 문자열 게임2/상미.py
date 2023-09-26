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
