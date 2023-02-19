# dfs is a recursive algorithm
# this is the code for connected graph
def dfs(given):
    global time
    global color
    global parent
    global trav_time
    global dfs_output
    global adj_list

    color[given] = 'G'
    trav_time[given][0] = time
    dfs_output.append(given)
    time+=1

    for vertex in adj_list[given]:
        if color[vertex] == 'W':
            parent[vertex] = given
            dfs(vertex)

    color[given] = 'B'
    trav_time[given][1] = time
    time+=1


adj_list = {'a':['b','c'],'b':['d','e'],'c':['b','f'],'d':[],'e':['f'],'f':[]}
time = 0
color = {} # color will keep track of visited nodes. this will contain 3 colors
           # white will be initial color of all nodes
           # when we first explore a vertex we will change its colour to grey
           # when it is fully explored we will change its colour to black
parent = {}
trav_time = {}
dfs_output = []


for node in adj_list.keys():
    color[node] = 'W'
    parent[node] = None
    trav_time[node] = [-1,-1]


dfs('a')

# if graph is disconnected then write this piece of code
# for i in adj_list.keys():
#    if color[i] == 'W':
#       dfs(i)

print(dfs_output)
print(trav_time)
print(parent)

# https://www.youtube.com/watch?v=FvGCzzfdOLw
