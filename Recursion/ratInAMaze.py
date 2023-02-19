def isSafe(newx,newy,visited,m,n,arr):
    if (newx>=0 and newx<=m-1) and (newy>=0 and newy<=n-1): 
        if visited[newx][newy] == 0 and arr[newx][newy] == 1:
            return True
    return False

def RatInAMaze(m,n,ans,x,y,visited,path,arr):
    # We have reached the end of the matrix here (that is the bottom right corner)
    if x == m-1 and y == n-1:
        ans.append(path)
        return

    visited[x][y] = 1

    # 4 Choices -> D, L, R, U

    # Down
    newx = x+1
    newy = y
    if isSafe(newx,newy,visited,m,n,arr):
        path+='D'
        RatInAMaze(m,n,ans,newx,newy,visited,path,arr)
        path = path[0:len(path)-1]
    
    # Left
    newx = x
    newy = y-1
    if isSafe(newx,newy,visited,m,n,arr):
        path+='L'
        RatInAMaze(m,n,ans,newx,newy,visited,path,arr)
        path = path[0:len(path)-1]

    # Right
    newx = x
    newy = y+1
    if isSafe(newx,newy,visited,m,n,arr):
        path+='R'
        RatInAMaze(m,n,ans,newx,newy,visited,path,arr)
        path = path[0:len(path)-1]
    
    # Up
    newx = x-1
    newy = y
    if isSafe(newx,newy,visited,m,n,arr):
        path+='U'
        RatInAMaze(m,n,ans,newx,newy,visited,path,arr)
        path = path[0:len(path)-1]


    visited[x][y] = 0


arr = [[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
m,n = len(arr),len(arr[0])
srcx,srcy = 0,0
ans = []

if arr[srcx][srcy] == 0:
    print(ans)

visited = []
for i in range(m):
    visited.append([0]*n)

path = ""

RatInAMaze(m,n,ans,srcx,srcy,visited,path,arr)
ans.sort() # Since the ans we want is in lexicographically order
print(ans)