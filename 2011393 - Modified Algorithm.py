# Muhammad Afif Danial Bin Mohd Zuhairi
# 2011393

def risk_arbitrage(d, r):
    n = len(d)
    sharpe = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                sharpe[i][j] = (d[i] - r[i]) / (d[j] - r[j])
            else:
                sharpe[i][j] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                sharpe[i][j] = min(sharpe[i][j], sharpe[i][k] + sharpe[k][j])

    return sharpe

d = [0.1, 0.2, 0.3]         # expected return
r = [0.01, 0.02, 0.03]      # risk-free rate

sharpe = risk_arbitrage(d, r)

print(sharpe)
