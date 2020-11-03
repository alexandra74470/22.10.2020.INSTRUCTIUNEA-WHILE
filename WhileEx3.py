s=0
a=0
b=0
c=0
d=0
while c==0 or b!=0:
    d=eval(input("Introduceti cifra"))
    c=d%2
    b=d%3
    if c==0:
        s=d+a
        a=s
print(s)