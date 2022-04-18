# https://www.spoj.com/problems/ELIS/

def longest_increasing_subsequence(a):
    n = len(a)
    l = [1]*n
 
    for i in range(1, n):
        for j in range(0, i):
            if a[i] > a[j] and l[i] < l[j] + 1:
                l[i] = l[j]+1
 
    maximum = 0
    for i in range(n):
        maximum = max(maximum, l[i])
 
    return maximum


N = int(input())
sequence = list(map(int, input().split()))

print(longest_increasing_subsequence(sequence))