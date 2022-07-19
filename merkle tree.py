import hashlib

class Node:
    def hash_message(message,function='sha256'):
        function=getattr(hashlib,function)
        message=message.encode('utf-8')
        return function(message).hexdigest()
    def __init__(self):
        self.L=None
        self.R=None
        self.P=None
        self.hash=''
        self.data=''

    def upload_hash(self,data):
        self.data=data
        self.hash=hash_message('00000000'+data)
        return self.hash
class Tree:
    def __init__(self):
        self.root=0
        self.h=0
        self.leaf=0
    def add(self,item,h):
        L=Node()
        R=Node()
        L.P=item
        item.L=L
        R.P=item
        item.R=R
        h=h-1
        if h==0:
            return
        else:
            self.add(L,h)
            self.add(R,h)
    def create(self,h):
        self.root=Node()
        self.h=h
        self.leaf=2**h
        self.add(self.root,h)
        return self.root
    def update(self,data,hashres):
        if self.leaf==0:
            print('Full!')
            return
        temp=self.root
        h=self.h
        leaf=self.leaf
        while(h!=0):
            if leaf>2**(h-1):
                leaf=leaf-2**(h-1)
                temp=temp.L
            else:
                temp=temp.R
            h=h-1
        self.leaf=1
        temp.data=data
        temp.hash=hashres
        self.upload_update(temp)
        return temp
    def upload_update(self,temp):#在此次做判断，对叶子数做判断
        if temp.P!=None:
            b='00000000'
            c='00010000'
            temp=temp.P
            if temp.R!=None and temp.L!=None:
                temp.hash=hash_message(c+temp.R.hash+temp.L.hash)
            else:
                temp.hash=hash_message(b+temp.R.hash+temp.L.hash)
            self.upload_update(temp)
    def display(self,root):
        if root.L!=None:
            print('<-',end="")
            self.show(root.L)
            print('->',end="")
            self.show(root.R)
        else:
            print(root.hash)
            print(root.data)
    



def tob(x):
    return ''.join([bin(ord(c)).replace('0b','')for c in x])
def tostr(x):
    return ''.join([chr(i)for i in [int(b,2)for b in x.split(' ')]])

#x=['1','0','0','1','1','0','1','0','1']
"""a=''
for i in x:
    a+=tob(i)
    
