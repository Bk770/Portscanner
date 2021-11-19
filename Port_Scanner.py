
'''
Created on Nov 14, 2021

@author: 16308
'''
import socket


from datetime import datetime
import time




 #Takes a string input domain or IP 
target = input("Enter the host to be scanned (IP or Domain): ") 


#Displays User input
print ("Scanning started at: " + str(datetime.now())


# Resolve target to IPv4 address
target_IP = socket.gethostbyname(target)


start = time.time()


end = time.time()

elapsed = end-start


print ("Target: " + target_IP + "\n" + "It took " + str(elapsed) + " seconds" )
    

while True:
    
    
     # Enter the port to be scanned
    target_Port = int(input("Enter the port: "))
    
    
                 
    
    #Try block to test a block of code for errors
    try:
        
        start1 = time.time()
        #Create a new socket 
        sock = socket.socket()    
                
        #Establich connection to the host and ports        
        res = sock.connect((target_IP, target_Port))
        
        
        end1 = time.time()
        
        elapsed1 = end1-start1
        
        print ("Port {}: Open" .format(target_Port) + "\n" + " That took " + elapsed1 + " seconds")
        
    
        
        
        sock.close()
    except:
        print ("Port {}: Closed" .format(target_Port) + "\n" + " That took " + elapsed1 + " seconds")
        
timeSecondScan = datetime.now()

     
totalScan = timeSecondScan - timeFirstScan
 
print ("Total scan completed in: "+ totalScan)