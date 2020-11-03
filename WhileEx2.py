l=0
t=0
p=0
n=0
np=0
nn=0
while l<12:
    t=eval(input("Introduceti temperatura"))
    if t>0:
        p+=t
        np+=1
    else:
        n+=t
        nn+=1
    l+=1
print("Media temperaturilor pozitive este", round(p/np,2))
print("Media tempraturilor negative este", round (n/nn,2))