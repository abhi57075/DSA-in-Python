import sys
from heapq import heapify, heappush, heappop

def djikstra(graph,source,destination):
    inf = sys.maxsize
    node_data = {}
    for i in graph:
        node_data[i]={'cost':inf, 'predecessor':[]}
    
    node_data[source]['cost'] = 0
    visited = []
    
    temp = source
    min_heap = []

    for i in range(5): # 5 here because total no of nodes except the source node
        if temp not in visited: 
            visited.append(temp)
            min_heap = []

            #print(temp)
            #print(visited)

            for j in graph[temp]:

                if j not in visited:

                    #print(j)
                    
                    cost = node_data[temp]['cost'] + graph[temp][j]

                    #print(cost)
                    #print(node_data[j]['cost'])

                    if cost < node_data[j]['cost']:
                        node_data[j]['cost'] = cost
                        node_data[j]['predecessor'] = node_data[temp]['predecessor'] + list(temp)
                    heappush(min_heap,(node_data[j]['cost'],j))
                    
                    print(min_heap)
        
        heapify(min_heap)
        
        #print(min_heap)
        #print()
        
        temp = min_heap[0][1] # here after first iteration temp = B; here 0 means cost and 1 means predecessor

    print("\n")
    print(str(node_data[destination]['cost']))
    print(str(node_data[destination]['predecessor']+list(destination)))


graph = {'a':{'b':2,'c':4},'b':{'a':2,'d':8,'c':3},'c':{'a':4,'b':3,'d':2,'e':5},'d':{'b':8,'c':2,'f':22,'e':11},'e':{'c':5,'d':11,'f':1},'f':{'d':22,'e':1}}
source = 'a'
destination = 'f'
djikstra(graph,source,destination)

# https://www.youtube.com/watch?v=OrJ004Wid4o