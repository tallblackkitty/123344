#!/usr/bin/env python
# coding: utf-8

# In[3]:


n1 = 'm'
n2 = '5'
for x in range(2):
    print(n1, " ", n2, " ", "; ", end = ' ')
    n1=chr(ord(n1)+2)
    n2+=5


# In[ ]:


y = 6
for x in range (5, 0, -1):
    print(x, " ", y, end = ' ')
    


# In[5]:


s = 0
ctrl = 0
ctrl2 = 0
p = 1
for x in range (10):
    n = int(input())
    s+=n
    if n < 0:
        ctrl+=1    
    if n>= 8 and n<=10:
        ctrl2+=1
    if n<12 and n!=5:
        p*=n
    if n%3 == 0 and n>10:
        nume+=n
        deno+=1
    
ave = s / 10
min = p**0.5
d = 3*(nume-deno)
sub = nume/deno
print(s,ave)
print(ctrl1)
print(ctrl2)
print(d)


# In[6]:


t23 = 0
nume = 0
deno = 0
n = int(input())
S = n
L = n
for x in range (9):
    n = int(input())
    if n > L:
        L = n
    if n < S:
        S = n
    if n % 2 == 0 and n%3==0:
        t23+=n
    if n%2 == 1:
        nume+=n
        deno+=1
ave = (L+S) / 2
c = (nume/deno)**0.333


# In[ ]:




