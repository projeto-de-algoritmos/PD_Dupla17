# https://www.spoj.com/problems/KNAPSACK/

def knapSack(n, w, weight, value):
    K = [[0 for x in range(w+1)] for x in range(n+1)]

    for i in range(n+1):
        for j in range(w+1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif weight[i-1] <= j:
                K[i][j] = max(value[i-1] + K[i-1][j-weight[i-1]], K[i-1][j])
            else:
                K[i][j] = K[i-1][j]

    return K[n][w]


S, N = list(map(int, input().split()))

weight, value = [], []

for _ in range(N):
    w, v = list(map(int, input().split()))
    weight.append(w)
    value.append(v)

maximum_value = knapSack(N, S, weight, value)

print(maximum_value)