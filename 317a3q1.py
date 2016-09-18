# CMPT317 Assignment 3 Question 1 Linear Classifier
# Yuqing Tan (Beatrice) (yut630, 11119129)

# point-line distance
# positive distance -> above ; negative distance -> below
def pointLineDist(x1, x2, a, b):
	return (a*x1 + b*x2 - 1) / (a*a + b*b)**0.5

# evaluation function
def eval(x1, x2, a, b):
	d = pointLineDist(x1, x2, a, b)
	#print("d=%f" % d)
	if d >= 0:
		return 1
	else:
		return 0

def updateAll(data, a, b, alpha):
	updatea = 0.0
	updateb = 0.0
	length = len(data)
	for i in range(0,length):
		d = data[i]
		x1 = d[0]
		x2 = d[1]
		y = d[2]
		h = eval(x1, x2, a, b)
		print("h=%f" % h)
		#print((y - h) * x1)
		#print((y - h) * x2)
		updatea = updatea + (y - h) * x1 * alpha
		updateb = updateb + (y - h) * x2 * alpha
	return (updatea, updateb)

def learn(data, a, b, numItr):
	print("a=%f b=%f" % (a,b))
	alpha = 1.0
	for i in range(1,numItr+1):
		updates = updateAll(data, a, b, alpha)
		a = a + updates[0]
		b = b + updates[1]
		#print(updates)
		print("a=%f b=%f i=%d" % (a,b,i))
		alpha = alpha * 0.99


data = ((1.0,1.0,0.0), (3.0,2.0,0.0), (2.0,3.0,1.0), (4.0,4.0,1.0))
#line equation: a*x1 + b*x2 = 1
#learn(data, 0, 0.4, 10) # y=2.5, separates
learn(data, 0, 0.2, 20) # y=5, doesn't separate
#learn(data, 0.4, 0, 20) # x=2.5, doesn't separate
