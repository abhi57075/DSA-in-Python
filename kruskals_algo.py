def find(graph,node):
    if graph[node]<0:
        return node
    else:
        temp = find(graph,graph[node])
        return temp


def union(graph,a,b,d,answer):
    tempa = a
    tempb = b
    a = find(graph,a) # find returns leader of the family
    b = find(graph,b)
    if a == b: # it means a loop will be formed
        pass
    else:
        global cost
        cost+=d
        answer.append((tempa,tempb))
        if graph[a] < graph[b]: # a has more members than b
            graph[a] = graph[a]+graph[b]
            graph[b] = a
        else:
            graph[b] = graph[a]+graph[a]
            graph[a] = b


graph = [[1,2,1],[1,3,3],[2,6,4],[3,6,2],[3,4,1],[4,5,5],[5,6,6],[5,7,7],[6,7,2]] 
no_of_nodes = 7
graph = sorted(graph, key = lambda graph:graph[2])
# here in graph [1,2,1] 1 and 2 are the nodes and 1 is the distance
# graph:graph[2] --> here graph means it is passed as input and :graph[2] means it is sorted based on values at index 2
final_graph = [-1]*(no_of_nodes+1)
answer = []

cost = 0


for u,v,d in graph:
    union(final_graph,u,v,d,answer)
   
print(cost)
print(final_graph)
print(answer)

# https://www.youtube.com/watch?v=hupbSXllSIc
# https://www.youtube.com/watch?v=WQbbFhPGBN0