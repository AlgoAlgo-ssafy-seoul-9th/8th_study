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
