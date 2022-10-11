import time as t
import pickle as p
f=open(r'C:\Users\user\Desktop\students.dat','w+b')
d={'name':'Kev'}
p.dump(d,f)
f.seek(0)

ds=p.load(f)
for i in range(10):
    print(i,end="")
    t.sleep(1)
    print('\b',end='',flush=True)
print(ds)
