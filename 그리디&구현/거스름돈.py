잔돈 = int(input())
답 = 0
arr = [500, 100, 50, 10]

for a in arr:
    답 += 잔돈 // a
    잔돈 %= a

print(답)
