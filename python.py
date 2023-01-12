a=list(map(int,input().split()))
b=list(map(int,input().split()))
def fun(a,b):
    count=0
    for i in range(len(a)):
        if sum(a[:i+1])==sum(a[i+1:]) and sum(a[i+1:])==sum(b[:i+1]) and sum(b[:i+1])==sum(b[i+1:]):
            if b[i+1:]!=[] and b[:i+1]!=[] and a[i+1:]!=[] and a[:i+1]!=[] :
                count+=1
    if count>0:
        print(count)
    else:
        print(0)
fun(a,b)
