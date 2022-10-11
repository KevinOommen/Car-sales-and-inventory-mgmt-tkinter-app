import pickle as p
import datetime
def log(name,pwd):
    fout=open("users.txt",'w+b')  
    d={name:pwd}
    p.dump(d,fout)
    fout.close()

if __name__=='main':
	log('Kevin','ironman')
	log('Adarsh','vergis')
