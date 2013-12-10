import httplib
import json
import urllib2
import requests

import csv
from collections import defaultdict
from types import InstanceType


class authentic_ping:
    "sample"
    def paramfun(self,param1,url1,val1):       
        
        count=1         
        columns = defaultdict(list) #we want a list to append each value in each column to
        with open('D:\\ViaWest\\automation\\values.csv', 'rb') as f:
            
                reader = csv.DictReader(f) #create a reader which represents rows in a dictionary form
                for row in reader:
                    #this will read a row as {column1: value1, column2: value2,...}
                   
                    for (k,v) in row.items(): #go over each column name and value 
                    #  columns[k].append(v) #append the value into the appropriate list based on column name k
                        for (k, v) in columns.items():
                            row[k].append(v)  
                        expvalfile = row['Expectedvalue'];
                        return expvalfile                   
                        url1 = row['Url'];
                        return url1                 
                        param1 = row['Parameter'];
                        return param1
                       
                        count=count+1  
                        print("for testcase number ", count)
                        print('Name in row1 is: ', row['Name'])
                        print('URL in row1 is: ', row['Url'])
                        print('Expected in row1 is: ', row['Expectedvalue'])
                        print('Parameter in row1 is: ', row['Parameter'])   
#                                 
                

                        


