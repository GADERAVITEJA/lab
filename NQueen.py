def NQueens(n,x,i,c):
   for j in range(i):
     if(abs[i-j]==abs[x(j)-c]or x[j]==c):
        return False;
   return True; 
   
def NQU(n,x,i):
    if i==n:
       return True;
    if x[i]<=0:
       return False;
    for c in range(n):
       x[i]=c
       if NQU(n,x,i,c):
           retuen True;
       x[i]=-1
    return False;
n=int(input("Enter n:"))
x=[-1]*n 
if i in place(n,x,i,c):
   for i in range(n):
      for j in range(n):
        if x[i]==j:  
           print(Q,end='')
        else:
           print(-,end='')
else:
   print("Not Found")
   
