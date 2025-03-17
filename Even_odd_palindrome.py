n= int(input())
e=[]
o=[]
for i in range(n):
    if i%2==0:
        if i%11==0:
            e.append(i)
    else:
        if i%11==0:
            o.append(i)
print("Even Palindrome:", e) 
print("Odd Palindrome:", o)
