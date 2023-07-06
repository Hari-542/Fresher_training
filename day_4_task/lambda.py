n=int(input("Enter the number:"))
l=[]
for i in range(n):
    l.append(input())
c=input()
lst = lambda l,c:[(x) for x in l if c in x]
print(*lst(l,c))