st=[int(x)for x in input("spusok").split()]
print("max",max(st))
print("min",min(st))
##############Task2#######
a=[print(x,"na 2") for x in range(1,11) if x%2==0]
b=[print(x,"na 3") for x in range(1,11) if x%3==0]
c=[print(x,"krim 2 i 3") for x in range(1,11) if x%3!=0 and x%2!=0] 
##############Task3#######
n=int(input("n="))
k=1
b=[x for x in range(1,n+1)]
for i in b:
    k=k*i
print(k)
##############Task4#######
login=input('your login:')
while login=='First':
    print('hello, First')
    break
if login!='First':
    print('error  bad login ')

##############Task5#######
while True:
    n=int(input('some number:'))
    if n<=0:
        print(' 0 or negative')
        break
##############Task6#######
size=int(input('rozmir progresii:'))
my_list=[]
while len(my_list)<size:
    number=int(input('some number:'))
    if number>0:
        my_list.append(number)
    else:
        print(my_list, ' negative number or 0')
        break