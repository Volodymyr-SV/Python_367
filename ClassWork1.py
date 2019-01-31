a=int(input("a="))
b=int(input("b="))
if a<b:
    print(b,">",a,", b bilshe")
elif a>b:
    print(a,">",b,", a bilshe")
else: print(a,"=",b,", rivni")

#######################

c=int(input("c="))
if c % 2 == 0 :
    print("parne")
else: print("neparne")

########################   

d=int(input("d=")) 
f=1
for i in range(1,d+1):
    f=f*i
print("factorial=",f)