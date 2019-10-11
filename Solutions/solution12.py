n=int(input()) 
width = len("{0:b}".format(n)) 
for num in range(1,n+1):
    print ('  '.join(map(str,(num,oct(num).replace('0o',''),hex(num).replace('0x',''),bin(num).replace('0b','')))))
