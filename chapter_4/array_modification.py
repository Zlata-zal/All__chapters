MOD = 1000000007

def precompute_binomials(max_n, max_k):
    binom = [[0] * (max_k + 1) for _ in range(max_n + 1)]

    for n in range(max_n + 1):
        binom[n][0] = 1
        for k in range(1, min(n, max_k) + 1):
            binom[n][k] = (binom[n - 1][k - 1] + binom[n - 1][k]) % MOD

    return binom


def solve(n, m, a, queries):
    max_k = 100
    binom = precompute_binomials(n, max_k)

    diff = [0] * (n + 2)

    for l, r, k in queries:
        l -= 1
        r -= 1
        for j in range(r - l + 1):
            add_value = binom[j + k][k]
            diff[l + j] = (diff[l + j] + add_value) % MOD

    result = [0] * n
    curr_add = 0
    for i in range(n):
        curr_add = (curr_add + diff[i]) % MOD
        result[i] = (a[i] + curr_add) % MOD

    return result

n, m = map(int, input().split())
a = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

result = solve(n, m, a, queries)

print(' '.join(map(str, result)))
