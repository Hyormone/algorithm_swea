import sys

sys.stdin = open('input.txt')

for tests in range(10):
    case = int(input())
    di = [0, 0, 1]
    dj = [-1, 1, 0]
    arr = [list(map(int, input().split())) for _ in range(100)]

    for s in range(100):
        i_s = 0
        j_s = 0

        if arr[0][s] == 1:
            j_s = s
            while i_s != 99:
                b = 0
                if 0 < j_s < 100:
                    for a in range(3):
                        if arr[i_s + di[a]][j_s + dj[a]]:
                            i_s += di[a]
                            j_s += dj[a]
                            if a == 0:
                                b = 0
                            elif a == 1:
                                b = 1
                        # while b != 2:
                        #     if a == 0:
                        #         for a in [0, 2]:
                        #             if arr[i_s + di[a]][j_s + dj[a]]:
                        #                 i_s += di[a]
                        #                 j_s += dj[a]
                        #                 b = a
                        #     elif a == 1:
                        #         for a in range(1, 3):
                        #             if arr[i_s + di[a]][j_s + dj[a]]:
                        #                 i_s += di[a]
                        #                 j_s += dj[a]
                        #                 b = a
                    break
                elif j_s == 0:
                    for a in range(1, 3):
                        if arr[i_s + di[a]][j_s + dj[a]]:
                            i_s += di[a]
                            j_s += dj[a]
                        break
                    break
                elif j_s == 99:
                    for a in [0, 2]:
                        if arr[i_s + di[a]][j_s + dj[a]]:
                            i_s += di[a]
                            j_s += dj[a]
                        break
                    break
        if arr[i_s][j_s] == 2:
            bb = s
            break
        print(f'#{case}')