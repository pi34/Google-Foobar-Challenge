visited = []
def bfs(s, d, g, n):
    visited = [-1 for i in range(n)]
    queue = [s]
    visited[s] = s
    while len(queue) > 0:
        curr = queue.pop(0)
        for i in range(n):
            if (g[curr][i][1] - g[curr][i][0]) != 0 and visited[i] == -1:
                if i == d:
                    visited[d] = curr
                    path = [d]
                    temp = d
                    while temp != s:
                        temp = visited[temp]
                        path.append(temp)
                    path.reverse()
                    temp = 1
                    total = float("inf")
                    curr = s
                    while temp != len(path):
                        entry = g[curr][path[temp]]
                        diff = abs(entry[1]) - entry[0]
                        total = min(total, diff)
                        curr = path[temp]
                        temp += 1
                    temp = 1
                    curr = s
                    while temp != len(path):
                        entry = g[curr][path[temp]]
                        if entry[1] < 0: 
                            entry[1] += total
                        else:
                            entry[0] += total
                        entry = g[path[temp]][curr]
                        if entry[1] <= 0: 
                            entry[1] -= total
                        else:
                            entry[0] += total
                        curr = path[temp]
                        temp += 1
                    return True
                else:
                    visited[i] = curr
                    queue.append(i)
    return False

def solution(entrances, exits, path):
    max_val = sum(list(map(sum, path)))
    m = []
    for i in range(len(path)):
        m.append([])
        for j in range(len(path[i])):
            m[i].append([0, path[i][j]])
        m[i].append([0, 0])
        if i in exits:
            m[i].append([0, max_val])
        else:
            m[i].append([0, 0])
    m.append([])
    m.append([])
    for i in range(len(path[0]) + 2):
        if i in entrances:
            m[-2].append([0, max_val])
        else:
            m[-2].append([0, 0])
        m[-1].append([0, 0])
    while bfs(len(m)-2, len(m)-1, m, len(m)):
        pass
    total = 0
    for i in range(len(m)):
        total += m[-2][i][0]
    return total
