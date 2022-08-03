# https://www.acmicpc.net/problem/5585

잔돈 = 1000 - int(input())
답 = 0
arr = [500, 100, 50, 10, 5, 1]

for a in arr:
    답 += 잔돈 // a
    잔돈 %= a

print(답)
