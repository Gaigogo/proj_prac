import math
import random
import time
import hashlib

#1.Eculid求最大公因子
def gcd(a,b):
    r=a%b
    while(r!=0):
        a=b
        b=r
        r=a%b
    return b

#2.求模逆的扩展欧几里得
def ModInverse(a,m):
    if gcd(a,m)!=1:
        return None
    u1,u2,u3=1,0,a
    v1,v2,v3=0,1,m
    while v3!=0:
        q=u3//v3
        v1,v2,v3,u1,u2,u3=((u1-q*v1),(u2-q*v2),(u3-q*v3),v1,v2,v3)
    return u1%m
def get_hash(string0):
    sha256=hashlib.sha256()
    sha256.update(string0.encode('utf-8'))
    res=sha256.hexdigest()
    return res
#此处使用sage生成2^16素数
q=50123
a=1097
b=4093
x_g=40982
y_g=66

#d=random.randint(1,50121)
#print(d)
d=46007
#x_p=(d*x_g)%q
#y_p=(d*y_g)%q
#print(x_p)
#print(y_p)
x_p=32106
y_p=29082
M1='helloworld'
e1=get_hash(M1)

k=random.randint(2,50123)
while(gcd(k,q)!=1):
    k=random.randint(2,50123)
x=(k*x_g)%q

r1=(int(e1,16)+x)%q
c=ModInverse(1+d,q)
s1=(c*(k-r1*d))%q

M2='123'
e2=get_hash(M2)

r2=(int(e2,16)+x)%q
s2=(c*(k-r2*d))%q
l=s2-s1
n=s1-s2+r1-r2
n_ni=ModInverse(n,q)
d_leaking=(l*n_ni)%q
print(d_leaking)
