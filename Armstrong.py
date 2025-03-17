n = int(input("Enter number:"))
temp = n
x = len(str(n))
res=0
for i in range(x+1):
    rem=n%10
    res+=pow(rem,x)
    n=n//10
if temp == res:
    print("Armstrong")
else:
    print("not a Armstrong")
