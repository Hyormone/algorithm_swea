import sys

sys.stdin = open('input.txt')
dx = [0, 0, -1]
dy = [1, -1, 0]

for tests in range(10):
    case = int(input())
    n = 100
    lst = [list(map(int, input().split())) for _ in range(100)]
    y = lst[-1].index(2)
    x = n - 1

    while x > 0:
        for d in range(3):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= ny < n and lst[nx][ny] == 1:
                lst[x][y] = 0
                x = nx
                y = ny
    print(f'#{case} {y}')

