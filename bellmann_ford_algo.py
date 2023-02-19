# bellmann_ford can be used for negative and positive edge weights whereas dijkstra can only be used for positive edge weights

import sys
def bellmann_ford(graph, source, destination):
    inf = sys.maxsize
    node_data = {}
    for i in graph:
        node_data[i]={'cost':inf,'predecessor':[]}
    node_data[source]['cost'] = 0

    for i in range(5):
        for vertex in graph:
            for neighbour in graph[vertex]:
                cost = node_data[vertex]['cost'] + graph[vertex][neighbour]
                if cost < node_data[neighbour]['cost']:
                    node_data[neighbour]['cost'] = cost

                    if node_data[neighbour]['cost'] == inf:
                        node_data[neighbour]['predecessor'] = node_data[vertex]['predecessor'] + list(vertex)
                    else:
                        node_data[neighbour]['predecessor'].clear()
                        node_data[neighbour]['predecessor'] = node_data[vertex]['predecessor'] + list(vertex)
    
    print(node_data[destination]['cost'])
    print(node_data[destination]['predecessor'])



graph = {'a':{'b':6,'c':4,'d':5},'b':{'e':-1},'c':{'b':-2,'e':3},'d':{'c':-2,'f':-1},'e':{'f':3},'f':{}}
source = 'a'
destination = 'e'
bellmann_ford(graph,source,destination)

# https://www.youtube.com/watch?v=90lJ2rS39_k