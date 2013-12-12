import requests,sys
import json
from compiler.ast import List
from fileresponse import fileresponse 
class Test15_DelCampaign():
    
        
    name=Test1
    url1="http://google.com"    
    
    #r1 = requests.auth.HTTPBasicAuth("madhusudan.vyas@snstech.com","cloud!23") 
    r = requests.get(url1)
    status = r.status_code
    responsedata = r.text
    print str(r.text)   
    responsedata = r.text       
    print ("Testcase passed")    
    datafile=List  
    datafile=[responsedata,status]     
    type(fileresponse)     
    fr=fileresponse()
    filewrite= fr.fileresp(datafile)
