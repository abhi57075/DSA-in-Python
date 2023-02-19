import math as m
for i in range(int(input())):
  x,y = map(int,input().split())
  a,b = min(x,y),max(x,y)
  count = 0

  if b!=0  and a!=0:
    g = b//a
    d = int(m.log(g,2))
    e = 2**d
    if g != 0:
      a = a*e
      count += d
    if a == b:
      print(count+a)
    else:
      diff2 = b-a
      k = a - diff2
      count+=k
      a = diff2
      b = diff2*2
      count+=1
      count+=b
      print(count)
  
  else:
    print(-1)

