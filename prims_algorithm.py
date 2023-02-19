import sys
inf = sys.maxsize

# Returns true if edge u-v is a valid edge to be include in MST. An edge is valid if one end is already included in MST and other is not in MST.
def isValidEdge(u, v, inMST):
	if u == v:
		return False
	if inMST[u] == False and inMST[v] == False:
		return False
	elif inMST[u] == True and inMST[v] == True:
		return False
	return True

def primMST(cost):
    nodes = []
    inMST = [False] * V

	# Include first vertex in MST
    inMST[0] = True

	# Keep adding edges while number of included edges does not become V-1.
    edge_count = 0
    mincost = 0

    while edge_count < V - 1:
        
        for i in range(V):
            minn = inf
            a = -1
            b = -1
            for j in range(V):
                if cost[i][j] < minn and isValidEdge(i,j,inMST):
                    minn = cost[i][j]
                    a = i
                    b = j

            if a!=-1 and b!=-1:
        
                nodes.append((a,b))
                edge_count+=1
                mincost+=minn
                inMST[a] = inMST[b] = True

    print(mincost)
    print(nodes)


cost = [[inf, 4, inf, 5],
        [4, inf, 1, 3],
        [inf, 1, inf, 2],
        [5, 3, 2, inf]]
V = len(cost[0])

primMST(cost)

# https://www.geeksforgeeks.org/prims-algorithm-simple-implementation-for-adjacency-matrix-representation/