'''from collections import deque

N = int(input())

first_word = list(input())
cnt = 0



for _ in range(N-1):
    deque = list(input())
    for i in range(len(deque)):
        for j in range(len(first_word)):
            if first_word[j] == deque[i]:
                deque.pop()
                break
    if abs(len(deque)) <= 1:
         cnt += 1
    stack = []
    deque = []

print(cnt)'''


N = int(input())
target = list(input()) 
answer = 0

for _ in range(N-1):
    compare = target[:] 
    word = input() 
    cnt = 0

    for w in word:
        if w in compare:
            compare.remove(w)
        else:
            cnt += 1

    if cnt < 2 and len(compare) < 2:
        answer += 1

print(answer)