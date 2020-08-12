n=int(input("Enter number of rows "))
m=int(input("Enter number of columns "))
mat=[]
print("Enter elements :")
for i in range(0,n):
    arr=[]
    for j in range(0,m):
        z=int(input())
        arr.append(z)
    mat.append(arr)

top=0
down=n-1
left=0
right=m-1
dir=0
arr=[]
while(top<=down and left<=right):
    if(dir==0):
        for i in range(left,right+1):
            arr.append(mat[top][i])
        top=top+1

    elif(dir==1):
        for i in range(top,down+1):
            arr.append(mat[i][right])
        right=right-1

    elif(dir==2):
        for i in range(right,left-1,-1):
            arr.append(mat[down][i])
        down=down-1

    elif(dir==3):
       for i in range(down,top-1,-1):
            arr.append(mat[i][left])
       left=left+1


    dir=(dir+1)%4


print("2D matrix after spiral traversal")
for i in arr:
    print(i,end=" ")
    
    