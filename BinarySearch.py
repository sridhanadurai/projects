def fibo(i,j,n,c):
    if c == n:
        print(j)
    else:
        i,j=j,i+j
        print(i,end=" ")
        fibo(i,j,n,c+1)

fib_li=[]
fibo_num=int(input("Enter the number:"))
i,j,c=0,1,1
print(i,end=" ")
fibo(i,j,fibo_num,c)
