import os;
import sys;
import ats
import schedule;
import time;
import Mail_Attacher

def DuplicateRemoval(path):
    print("Files are....");
    data = {};
    for Folder,Subfolder,Files in os.walk(path):
        for name in Files:
            #print(name);
            name = os.path.join(Folder,name);
            
            checksum = ats.hashfile(name);
            #print(checksum);

            if checksum in data:
                data[checksum].append(name);
            else:
                data[checksum] = [name];

    newdata = [];
    newdata = list(filter(lambda x: len(x)>1,data.values()));
    
 
    cpath = os.path.join(path,"Marvellous") 
    if not os.path.isdir(cpath):	
     os.mkdir(cpath)     
    count = 0;
    dis = '_'*40
    fpath = os.path.join(cpath,"Log-%s.txt"%time.ctime())
    print(os.listdir(cpath))
    fobj=open(fpath,"w+")
    for outer in newdata:
        icnt = 0;
        for inner in outer:
            icnt+=1;
            if icnt >= 2:
                count+=1    
                fobj.write(dis+"\n")
                fobj.write("File Name :- %s \n"%os.path.basename(inner))
                fobj.write("Created At :- %s \n"%time.ctime(os.path.getctime(inner)))
                fobj.write(dis+"\n")
                
                
                                	
                print("Delete",inner);
                os.remove(inner);
                
    fobj.write("Total number of files deleted "+str(count))
    fobj.close();
    mailUser=sys.argv[3]
    Mail_Attacher.Attach(fpath,mailUser) 

def main():
    print("Duplicate file removal...");
    schedule.every(int(sys.argv[2])).minutes.do(DuplicateRemoval,path=sys.argv[1]);
    while True:
        schedule.run_pending();
        time.sleep(1);


if __name__ == "__main__":
    main();

