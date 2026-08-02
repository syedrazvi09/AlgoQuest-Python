import sys


def solve(N, M, F, A, B, C, MOD=None):
    A = [0] + A
    B = [0] + B
    C = [0] + C

    INF = float('inf')

    dpA = [[INF] * (M + 1) for _ in range(N + 1)]
    dpB = [[INF] * (M + 1) for _ in range(N + 1)]

    if N >= 1:
        dpA[1][0] = 0
    if M >= 1:
        dpB[0][1] = 0

    for i in range(2, N + 1):
        dpA[i][0] = dpA[i - 1][0] + abs(A[i] - A[i - 1])

    for j in range(2, M + 1):
        dpB[0][j] = dpB[0][j - 1] + abs(B[j] - B[j - 1])

    for i in range(0, N + 1):
        for j in range(0, M + 1):
            if i == 0 and j == 0:
                continue
            step = i + j

            if i >= 1:
                best = INF
                if j == 0:
                    pass
                else:
                    if i - 1 >= 1:
                        best = min(best, dpA[i - 1][j] + abs(A[i] - A[i - 1]))
                    best = min(best, dpB[i - 1][j] + abs(A[i] - B[j]) + F * C[step])
                    if best < INF:
                        dpA[i][j] = best

            if j >= 1:
                best = INF
                if i == 0:
                    pass
                else:
                    if j - 1 >= 1:
                        best = min(best, dpB[i][j - 1] + abs(B[j] - B[j - 1]))
                    best = min(best, dpA[i][j - 1] + abs(B[j] - A[i]) + F * C[step])
                    if best < INF:
                        dpB[i][j] = best

    if N == 0:
        return dpB[0][M]
    if M == 0:
        return dpA[N][0]
    return min(dpA[N][M], dpB[N][M])


# ---- Test case from the prompt ----
N = 2
M = 2
F = 10
A = [10, 20]
B = [100, 110]
C = [1, 2, 1, 3]

result = solve(N, M, F, A, B, C)
print("Got:", result)
print("Expected: 110")
print("Match!" if result == 110 else "Mismatch!")