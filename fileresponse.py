import requests,sys
import json

class fileresponse(object):
    def init(self,test ):
        self.test= test
        
    def fileresp(self,datafile):
        self.datafile=datafile
        responsedata=datafile[0]
        tc=datafile[1]    
            
        outfile="D:\\ViaWest\\Cloud-Elements\\insparato\\jenkinsgitrepo\\temp.txt"
        f=open(outfile,'a')  
        f.write("Testcase number is :")
        f.write('\n')    
        f.write(str(tc))
        f.write('\n')
        f.write("The output is:")
        f.write('\n') 
        f.write(str(responsedata))
        f.write('\n')
        f.close()    
        return
