def dfs_cycle(given, adj_list):

    global color
    global parent
    color[given] = 'G'

    for vertex in adj_list[given]:
        if color[vertex] == 'W':
            cycle = dfs_cycle(vertex, adj_list)
            if cycle == True:
                return True
       
        elif color[vertex] == 'G': # Cycle condition
            #print("cycle found",given,vertex)
            return True
    
    color[given] = 'B'
    return False



adj_list = {'a':['c','b'],'b':['d'],'c':[],'d':['a','e'],'e':[]}

color = {}
parent = {}

for vertex in adj_list.keys():
    color[vertex] = 'W'
    parent[vertex] = None

ans = dfs_cycle('a',adj_list)
print(ans)



