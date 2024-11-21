MOD = 10**9 + 7

def count_paths(K, y1, y2):
    vertical_steps = abs(y2 - y1)
    total_steps = K + vertical_steps
    return total_steps + 1

def solve():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        total_paths = 0
        for y1 in range(1, N+1):
            for y2 in range(1, N+1):
                total_paths += count_paths(K, y1, y2)
                total_paths %= MOD
        print(total_paths)


solve()

