import csv
import time as t
for i in range(10,-1,-1):
    print(i)
    print('')
def  n():
    with open('teams_timetable.csv','r',newline='') as f:
    ##    writerobj=csv.writer(f,delimiter=',')
    ##    writerobj.writerow(['Subject','Teacher','Class','Time','Day'])
            readerobj=csv.reader(f)#returns a list of lists
            #print(list(readerobj))
            for row in readerobj:
                print(row)
            
    print('Done')
def q():
    with open('teams_timetable.csv','w+',newline='') as f:
        writerobj=csv.DictWriter(f,fieldnames=['Subject','Teacher'])
        writerobj.writeheader()
        writerobj.writerow({'Subject':'Chem','Teacher':'Sheena'})
        writerobj.writerow({'Subject':'Comp','Teacher':'Jincy'})
        writerobj.writerow({'Subject':'Maths','Teacher':'Melani'})
        readerobj=csv.DictReader(f)#returns a list of dictionaries
        if readerobj:print('True Reader')
        else:print('None:ReaderObj')
        #print(list(readerobj))
        for row in readerobj:
            print(row)
            if row:
                pass
            else:
                print("None")
def m():
##    with open('myf.bin','wb+') as f:
##        msg="1234"
##        f.write(msg.encode())
##        print(f.tell())
##        print(f.read())
    with open('mytxt.txt','w+') as f:
        msg="1234"
        f.write(msg)
        f.flush()
        
        print(f.tell())
        f.seek()
        print("text:",f.read(3))
def qw():
    with open('textfile.txt','w+') as f:
        f.write('Hey,I am Stark,\n')
        f.write('\tI am Iron Man\n')
        f.write('Spiderman\n')
        f.write('Captain America\n')
def er():
    with open('textfile.txt','r+') as f:
        print(f.readline())
