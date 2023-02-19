from collections import deque
def bfs(graph,root):
    visited = [] # unique elements will be stored
    queue = deque([root]) # now queue = [0]; it can contain repetitive elements
    check = dict() # Write this when the graph is cyclic
    for i in graph.keys(): # Write this when the graph is cyclic
       check[i] = False # Write this when the graph is cyclic
    while queue: # while queue is not empty
        vertex = queue.popleft()
        visited.append(vertex)
        for i in graph[vertex]: # here i will be the values in  graph[0] which is 1,2,3
            if i not in visited and check[i] == False:
                queue.append(i)
                check[i] = True # Write this when the graph is cyclic
    print(visited)

graph = {0:[1,2,3],1:[0,2],2:[0,1,4],3:[0],4:[2]}
bfs(graph,0)

graph2 = {0:[1,5],5:[0,4,2],3:[2,1],2:[5,3],4:[5],1:[0,3]} # this graph is forming a cycle
bfs(graph2,0)

# https://www.youtube.com/watch?v=tswq532WVF4