def dfs(node,visited):
    visited[node] = True
    for v in adj_list[node]:
        if visited[v] == False:
            dfs(v,visited)
    stack.append(node)


indegree = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0}
visited = {}
stack = []
for i in indegree.keys():
    visited[i] = False

adj_list = {'a':['c','d'],'b':['a','d'],'c':['e'],'d':['c','e'],'e':[]}
for i in adj_list.keys():
    for j in adj_list[i]:
        indegree[j]+=1

dfs('b',visited)
stack.reverse()
print(stack)
