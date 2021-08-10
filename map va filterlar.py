#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random


# In[3]:


# map funksiyasi
# 1
import random
def triple(x):
    return x**3
a = [random.randint(1,10) for i in range(7)]
print(a)
print(list(map(triple,a)))


# In[12]:


import random
a = [random.randint(1,10) for i in range(7)]
b = [random.randint(1,10) for i in range(7)]
c = [random.randint(1,10) for i in range(7)]
print(a,b,c,end='\n')
print(list(map(lambda a,b,c :a+b+c,a,b,c)))


# In[5]:


# 3
a=['Salom','hello','drive']

print(list(map(list,a)))


# In[39]:


# 4
a = [random.randint(1,10) for i in range(7)]
index = [random.randint(1,10) for i in range(7)]
print(a,index)
print(list(map(lambda a,index : a**index , a,index)))


# In[38]:


# 5
A=[random.randint(1,10) for i in range(7)]
print(A)
print(list(map(lambda i:i**2,A)))


# In[8]:


# 6
def try1(a):
    return a.upper(),a.lower()
satr=['a','h','l','s']
print(satr)
satr = set(satr)
print(list(map(try1,satr)))


# In[89]:


# 7
import random
def top(a,b):
    return a+b,a-b
a = [random.randint(1,10) for i in range(7)]
b = [random.randint(1,10) for i in range(7)]
print(a,b)
print(list(map(top,a,b)))


# In[94]:


# 8
a=[2,4,5,6,7,8]
b=(21,5,9,11,6)
print(list(map(str,a)),list(map(str,b)))


# In[4]:


# 9   
a=[('Kate',"USA","1989"),('Jack',"UK","1992"),('Tom',"Germay","1987")]
ismlar=list(map(lambda i:i[0],a))
davlatlar=list(map(lambda i:i[1],a))
yillar=list(map(lambda i:i[2],a))
print(ismlar,davlatlar,yillar,end='      ')


# In[15]:


# 10
def d(f1,f2,n):
    a=[]
    for i in range(n+1):
        fn=f1+f2
        f1=f2
        f2=fn
        a.append(fn)
    return a
f1=1
f2=1
n=10
A=d(f1,f2,n)
print(list(map(lambda i:i**2,A)))


# In[25]:


# 11
import random
S=[]
def sum1(f):
    S.append(f)
    return sum(S)
F=[random.randint(1,10) for i in range(10)]    
print(F)
print(list(map(sum1,F))[-1:])


# In[74]:


# 12
a=[]
def ishora(x):
    if x>0:
        a.append(1)
    elif x<0:
        a.append(-1)
    else:
        a.append(0)
    m=a.count(1)
    s=a.count(-1)
    v=a.count(0)
    return m*100/len(a),' % musbat', s*100/len(a) ,'% manfiy',v*100/len(a), '% 0' 
F=[random.randint(-1,1) for i in range(10)]   
print(F)
print(list(map(ishora,F))[-1:])


# In[16]:


# 13
S=[]
def Same(f,d):
    if f==d:
        return 1
    return 0
F=[random.randint(1,10) for i in range(10)]  
D=[random.randint(1,10) for i in range(10)]
print(F)
print(D)
print(list(map(Same,F,D)).count(1))


# In[17]:


# 14
f=[random.randint(-5,10) for i in range(10)]
a=[random.randint(-5,10) for i in range(10)]
print(f,a)
a+=f
a=random.sample(a,len(a))
print(a)


# In[31]:


# 15
D={"1": [1,3,2],"2": [2,4,5],"3" : [3,5,7]}
print(list(map(dict,zip(*[[(key,value) for value  in values] for key,values in D.items()]))))


# In[21]:


# 16
S=[['1', '3', '4', '6'],['3', '5', '2', '3']]
s=[]
for i in S:
    s.append(list(map(lambda i:int(i),i)))
print(s)


# In[22]:


# 17
s=[(1,3,4,6,9),(3,5,2,3),(1,3,2)]
S=[]
for j in s:
    S.append(list((map(lambda i:str(i),list(j)))))
print(S)

