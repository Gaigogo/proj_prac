import hashlib
def hash_message(message,function='sha256'):
    function=getattr(hashlib,function)
    message=message.encode('utf-8')
    return function(message).hexdigest()
class Node:

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
        a=[]
        b=[]
        a.append(root)
        print('/',root.hash)
        while a!=[]:
            if a[0].L==None:
                break
            for i in range(len(a)):
                print('/',a[i].L.hash,end='')
                print('/',a[i].R.hash,end='')
                b.append(a[i].L)
                b.append(a[i].R)
            print('')
            a=b
            b=[]
    def show_tree(self):
        root=self.root
        self.display(root)

s=Tree()
s.create(4)
s.update('0',hash_message('0'))
s.update('1',hash_message('1'))
s.update('2',hash_message('2'))
s.update('3',hash_message('3'))
s.update('4',hash_message('4'))

s.show_tree()
    
