def isprime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
        
s=int(input())
e=[]
o=[]
for i in range(1,s):
    if isprime(i):
        if i%2==0:
            e.append(i)
        else:
            o.append(i)
print("Even prime:",e)
print("Odd prime:",o)
            
    
