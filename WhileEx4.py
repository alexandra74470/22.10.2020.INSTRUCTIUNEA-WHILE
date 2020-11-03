n=eval(input("Introduceti numarul maxim "))
i=1
s=0
p=1
ma=0
m=0
while(i <= n):
    s+=i
    p*=i
    m+=1
    ma=s/m
    i+=1
print(s)
print(p)
print(ma)
