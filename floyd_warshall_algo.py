# floyd warshall algo is used for all pair shortest path ( for V vertices)
# if we use dijkstra algo for all pair shortest path time complexity will be n**3logn
# whereas floyd warshall will take only n**3 time
# if we have negative distance from a vertex to itself then we have a negative edge weight cycle which means shortest pair path could not be found

import sys
def floyd_warshall(graph):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
    print(dist)

graph = {0:{1:5,3:10},1:{2:3},2:{3:1},3:{}}
v = len(graph.keys())
inf = sys.maxsize
dist = []
for i in range(v):
    dist.append([0 for i in range(v)])
    for j in range(v):
        if i==j:
            dist[i][j]=0
        elif j in graph[i]:
            dist[i][j] = graph[i][j]
        else:
            dist[i][j] = inf 
floyd_warshall(dist)

#             10
#       (0)------->(3)
#        |         /|\
#      5 |          |
#        |          | 1
#       \|/         |
#       (1)------->(2)
#             3       