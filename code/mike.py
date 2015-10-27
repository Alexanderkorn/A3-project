from collections import deque

NUM_LINES=5 #The number of lines to process.  Should equal the deque maxlen    

lines = open("database.csv").readlines()[-NUM_LINES:] #Assumes the file can fit into memory
mydata = [line.split()[0] for line in lines]
d = deque(mydata, maxlen=NUM_LINES)
print (d)