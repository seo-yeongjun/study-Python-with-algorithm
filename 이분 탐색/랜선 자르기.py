"""
https://www.acmicpc.net/problem/1654
"""

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]


def cut(lan, n):
    start, end = 1, max(lan)
    while start <= end:
        mid = (start + end) // 2
        if sum(lan[i] // mid for i in range(k)) >= n:
            start = mid + 1
        else:
            end = mid - 1
    return end


print(cut(lan, n))
