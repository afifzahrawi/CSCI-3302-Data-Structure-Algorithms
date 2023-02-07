def floyd_warshall(d):
    n = len(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

d = [[0, 3, 8, float('inf'), -4],
     [float('inf'), 0, float('inf'), 1, 7],
     [float('inf'), 4, 0, float('inf'), float('inf')],
     [2, float('inf'), -5, 0, float('inf')],
     [float('inf'), float('inf'), float('inf'), 6, 0]]

result = floyd_warshall(d)

print(result)