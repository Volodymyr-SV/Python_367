#########task1###########
a=0
while a<100:
    if a%2==0:
        print(a)
    a+=1    
for a in range(100):
    if a%2==0:
        print(a)
###########task2############
for a in range(100):
    if a%2==0:
        continue
    else: print(a)
for a in range(100):
    if a%2==1:
#         print(a)
############task3#############
a=[2,4,6,8,7,6,4,2]
for i in a:
    if int(i)%2==1:
        print("mistut ne parni")
        break
##############task4###########
a=[1,2,3,45,6]
j=0
for i in a :
    a[j]=float(i)
    j+=1
print(a)   
#############task5########### 
n=int(input("do n="))
a=0
b=1
st=[]
st.append(a)
st.append(b)
while 1:
    p=a+b
    if p>n:
        break
    st.append(p)
    a=b  
    b=p  
print(st)    
##############task6########### 
st=["dama","data","tara","fara"]
for i in st:
    print(i)
