a=list(eval(input()))
a.append("00")
k = int(input())
r,c=[set()],0
re=[]
result=[]
for i in range(1,len(a)):
    if a[i-1][0]==a[i][0]:
        r[c].add(a[i-1][0])
        r[c].add(a[i-1][1])
    else:
        r[c].add(a[i-1][1])
        re.append(a[i-1][0])
        c+=1
        r.append(set())
for i in range(len(r)):
    for j in range(i+1,len(r)-1):
        d=str(len(r[i].intersection(r[j])))+str(abs(len(r[i])-len(r[j])))
        result.append((d,re[i],re[j]))
p=lambda result:int(result[0][0][0])
result.sort(key=p,reverse=True)
a=result
for i in range (len(a)):
    for j in range(i,len(a)):
        if a[i][0][0]==a[j][0][0] and int(a[i][0][1]) > int(a[j][0][1]):
            a[i],a[j]=a[j],a[i]
        elif a[i][0][0] != a[j][0][0]:
            break
for i in range(k):
    print(tuple(a[i][1:]))
