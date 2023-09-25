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
