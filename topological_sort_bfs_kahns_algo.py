# using source removal algorithm
# topological_sorting using bfs (kahn's algo)

def topological_sort(visited):
    while d != {}:
        for i in indegree.keys():
            if indegree[i] == 0 and visited[i] == False:
                visited[i] = True
                for j in d[i]:
                    indegree[j]-=1
                output.append(i)
                d.pop(i)
    print(output)


output = []
indegree = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0}
visited = {}
for i in indegree.keys():
    visited[i]=False

from collections import defaultdict  
d = defaultdict(list)
v,e = map(int,input().split())
for i in range(e):
    u,v = map(str,input().split())
    d[u].append(v)
    indegree[v]+=1

print(d)
print(indegree)

topological_sort(visited)

# input should be like this. Here 5 represents num of nodes and 7 represents num of edges
# 5 7
# A C
# A D
# B A
# B D
# C E
# D C
# D E
