n=int(input())
e=[]
o=[]
for i in range(10,n):
    if i%2==0:
        n=str(i)
        st=n[::-1]
        if st==n:
            e.append(i)
    else:
        n=str(i)
        st=n[::-1]
        if st==n:
            o.append(i)
print("Even palindrome:", e) 
print("Odd palindrome:",o)
