a,b,c = map(int,input().split())
if a<b and a<c:
    print(a,'is Smaller')
elif b<c:
    print(b,'is Smaller')
elif c<b:
    print(c,'is Smaller')
elif a==b==c:
    print('All are Equal')
