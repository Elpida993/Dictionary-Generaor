import time

length=int(raw_input("Enter the maximum of characters: "))
name='wl.txt'    
tic = time.clock()
print ("Running")
lista=[0 for x in xrange(length)]
x=length-1
string="abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLNMOPQRSTUVQXYZ1234567890"
list_of_results=[]
file1=file(name,"a")
while(x>-1):
    result=""
    if lista[x]==len(string)-1:
        for z in xrange(length):
            result+=string[lista[z]]
        lista[x]=0
        x-=1
    elif x==length-1:
        for z in xrange(length):
            result+=string[lista[z]]
        lista[x]+=1
    else:
        for z in xrange(length):
            result+=string[lista[z]]
        lista[x]+=1
        if x>0:
            x+=1
        else:
            x=length-1
    file1.write(result+"\n")
toc = time.clock()
ttn = toc - tic
print ("Done! in "+str(ttn)+" seconds.");
print ("Please check "+str(name)+" in your directory");

