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