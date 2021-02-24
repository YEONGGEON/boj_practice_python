import sys

prices = []
house = int(sys.stdin.readline())
for _ in range(house):
    A = list(map(int, sys.stdin.readline().split()))
    prices.append(A)

for i in range(1, house):
    prices[i][0] += min(prices[i-1][1], prices[i-1][2])
    prices[i][1] += min(prices[i-1][0], prices[i-1][2])
    prices[i][2] += min(prices[i-1][0], prices[i-1][1])

print( min(prices[-1][0],prices[-1][1],prices[-1][2]))