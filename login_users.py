import pickle as p
import hashlib
fout=open("users.txt",'w+b')
p1="ironman"
p2="vergis"
p3 = hashlib.md5(p1.encode())
p3 = p3.hexdigest()
p4 = hashlib.md5(p2.encode())
p4 = p4.hexdigest()
d={'Kevin':p3,'Adarsh':p4}
p.dump(d,fout)
fout.close()
