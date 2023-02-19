# the code works perfectly fine in google collab and pycharm
from queue import Queue
def bfs(adj_list,start):
  visited = {}
  level = {} # distance dictionary
  parent = {}
  bfs_output = []
  q = Queue()

  for node in adj_list.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1

  visited[start] = True
  level[start] = 0

  q.put(start)
  while not q.empty():
    first = q.get()
    bfs_output.append(first)
    for vertex in adj_list[first]:
      if visited[vertex] == False:
        visited[vertex] = True
        parent[vertex] = first
        level[vertex] = level[first]+1
        q.put(vertex)
  
  print(bfs_output)
  print(level) # shortest distance of all nodes from source node
  print(parent)

# path from node to source node
  node = 'g'
  path = []
  while node is not None:
    path.append(node)
    node = parent[node]
  path.reverse()
  print(path)


adj_list = {'a':['b','d'],'b':['a','c'],'c':['b'],'d':['a','e','f'],'e':['d','f','g'],'f':['d','e','h'],'g':['e','h'],'h':['g','f']}
bfs(adj_list,'a')
