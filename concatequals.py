a=0
b=0
equals=[[0,0]]
while a<1000:
    while b<1000:
        p=a+b
        sp=str(p)
        sa=str(a)
        sb=str(b)
        ip=sa+sb
        if sp==ip:
            equals.append([a,b])
        b=b+1
    b=0
    a=a+1
equals.sort()
print(equals)