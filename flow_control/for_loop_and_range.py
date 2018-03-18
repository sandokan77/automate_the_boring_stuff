for i in range(5):
    print ('My name\'s Jemmy',str(i))

#equivalent while loop
i = 0
while i < 5:
    print ('My name\'s Jemmy',str(i))
    i = i + 1

for i in range(12,16):#12,13,14,15
    #16 will not be present 
    print ('My name\'s Jemmy',str(i))

for i in range(0,10,2):#0,2,4,6,8
    #10 will not be present 
    print ('My name\'s Jemmy',str(i))

for i in range(5,-1,-1):
    #5,4,3,2,1,0
    #-1 will not be present 
    print ('My name\'s Jemmy',str(i))
