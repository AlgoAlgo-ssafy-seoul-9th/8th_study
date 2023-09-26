# 20437 문자열 게임 2
# 24160 KB 540 ms
import sys
from collections import deque

input = sys.stdin.readline
# 테스트 케이스 T
for _ in range(int(input())):
    # 문자입력 W, 개수 입력 K
    W = input().strip()
    K = int(input())
    # W 문자열 길이 N
    N = len(W)
    # 각 글자 마다 개수와 인덱스 체크용 dictionary
    str_cnt = {}
    # 길이 담을 정답 리스트
    answer = []
    # W 길이만큼 반복
    for j in range(N):
        # 문자가 딕셔너리 키로 이미 있으면
        if W[j] in str_cnt.keys():
            # 개수 +1
            str_cnt[W[j]][0] += 1
            # 인덱스 ++
            str_cnt[W[j]][1].append(j)
        else:
            # 없으면 생성
            str_cnt[W[j]] = [1, deque([j])]
        # 개수가 K개가 되면
        if str_cnt[W[j]][0] == K:
            # K 가 1일 때 체크
            if K == 1:
                # 1이면 그냥 1임
                answer.append(1)
            else:
                # 1이 아니면 마지막 인덱스와 처음 인덱스 빼서 길이 구함
                answer.append((str_cnt[W[j]][1][-1] - str_cnt[W[j]][1][0] + 1))
                # 개수 1개 빼고, 처음 인덱스 제거
                str_cnt[W[j]][0] -= 1
                str_cnt[W[j]][1].popleft()
    # K 개를 만족하는 글자가 있으면
    if answer:
        # 정답 리스트 정렬해서 처음과 마지막 출력
        answer.sort()
        print(answer[0], answer[-1])
    # 아니면 -1 출력
    else:
        print(-1)
