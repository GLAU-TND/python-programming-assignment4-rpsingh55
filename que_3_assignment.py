a=eval(input())
s=input()
d=[i for i in a if i[:len(s)]==s]
print(d)
