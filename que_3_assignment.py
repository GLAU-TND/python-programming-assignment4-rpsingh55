a=eval(input())
s=input()
d=[]
for i in a:
    for j in range (len(i)):
        if i[:j]==s:
            d.append(i)
            berak
print(d)
