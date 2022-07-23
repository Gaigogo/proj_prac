#sm2 key exchange

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
qlen=16
h=46007
a=49877
b=18407
xa_p=(a*x_g)%q
ya_p=(a*y_g)%q
xb_p=(b*x_g)%q
yb_p=(b*y_g)%q

#for a:
r_a=random.randint(2,50123)
while(gcd(r_a,q)!=1):
    r_a=random.randint(2,50123)
x1=(r_a*x_g)%q
y1=(r_a*y_g)%q
w=int((qlen*0.5)-1)
x1_n=2**w+(x1&((2**w)-1))
d_a=random.randint(1,50121)
t_a=(d_a+x1_n*r_a)%q

#for b:
r_b=random.randint(2,50123)
while(gcd(r_b,q)!=1):
    r_b=random.randint(2,50123)
x2=(r_b*x_g)%q
y2=(r_b*y_g)%q

x2_n=2**w+(x2&((2**w)-1))
d_b=random.randint(1,50121)
t_b=(d_b+x2_n*r_b)%q

x_u=(h*t_a)*(xb_p+x2_n*x2)
y_u=(h*t_a)*(yb_p+x2_n*y2)

x_v=(h*t_b)*(xa_p+x1_n*x1)
y_v=(h*t_b)*(ya_p+x1_n*y1)

s=(get_hash(str(x_u)+str(x1)+str(y1)+str(x2)+str(y2)))
S1=(get_hash('2'+str(y_u)+s))
SA=(get_hash('3'+str(y_u)+s))
print(S1,'/',SA)
m=(get_hash(str(x_v)+str(x1)+str(y1)+str(x2)+str(y2)))
S2=(get_hash('3'+str(y_v)+m))
SB=(get_hash('2'+str(y_v)+m))
print(S2,'/',SB)
