x=int(input("Wuwedi chislo: "))
s={}
for i in range(x):
    key=input()
    value=input()
    s[key]=value
a=int(input("Wuwedi wtoro chislo: "))
z=[]
for i in range(a):
    z.append(input("Wuwedi stoynost: "))
print(s, z)
for i in range(len(z)):
    if z[i]  in s.keys():
        y=z[i]
        z[i]=s[z[i]]
        s.pop(y)
        print(s, z)