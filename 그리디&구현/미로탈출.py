from collections import deque

xx = [-1, 1, 0, 0]
yy = [0, 0, -1, 1]
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input())))
print(arr)


def miro(x, y):
    que = deque()
    que.append((x, y))

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + xx[i]
            ny = y + yy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if arr[nx][ny] == 0:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                que.append((nx, ny))
    return arr[n-1][m-1]


print(miro(0, 0))
print(arr)
