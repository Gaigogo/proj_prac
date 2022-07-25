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
M='helloworld'
e=get_hash(M)

k=random.randint(2,50123)
while(gcd(k,q)!=1):
    k=random.randint(2,50123)

#ECDSA：
x=(k*x_g)%q
r=x%q
k_ni=ModInverse(k,q)
s=((int(e,16)+r*d)*k_ni)%q

u=random.randint(2,50123)
while(gcd(u,q)!=1):
    u=random.randint(2,50123)
v=random.randint(2,50123)
while(gcd(v,q)!=1):
    v=random.randint(2,50123)

x_f=(u*x_g+v*x_p)
r_f=x_f%q
v_ni=ModInverse(v,q)
e_f=r_f*u*v_ni
s_f=r_f*v_ni

#verify:
w=ModInverse(s_f,q)
r_check=(e_f*w*x_g+r_f*w*x_p)%q

print(r_f)
print(r_check)
