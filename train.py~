import math
with open("dataset.txt") as textFile:
	lines = [line.split() for line in textFile]

length=lines.__len__()
print "Length of training set :"+ str(length)
iter = 5
rate = .0001
q=[0.0,0.0,0.0,0.0]
count = 0

def sigmoid(z):
	return 1 / 1 + math.exp(-z)
def classify(j):
    logit = .0;
    i=0
    while i < 3 :
        logit += q[i] * int(lines[j][i])
	i += 1
    return sigmoid(logit)
while count < iter :
    print count
    count +=1
    j=0
    while j < length :
	i = 0
        print classify(j)
	print ' '
	while i < 3:	
		temp = int(lines[j][i]) * q[i]
		print  temp,		
		i+=1
	j+=1
    q[0]+= rate
    q[1]+= rate
    q[2]+= rate


    
print "out"

