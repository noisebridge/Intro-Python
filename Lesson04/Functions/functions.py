
x = 3
L = [0, 1]

def times(x, y):
	return x * y

def varscope():
	x = 2
	return x

def globalscope():
	global x
	x = 99

def changeme(a,b):
	x = 2
	b[0] = 'Spam'

def useDef(a = 1, b = 2, c = 3): print(a,b,c)

def unlimited(*args): print(args)






if __name__ == '__main__':

	print times(2,3)
	print times(2.5,6)
	print times("Spam! ", 4)

	print "x before function: %s" % (x)
	print "x inside function: %s" % (varscope())
	print "x after the function %s" % (x)

	globalscope()
	print "Using Global in a function: %s" % (x)

	changeme(x,L)
	print "X has not changed: %s" % (x)
	print "L has changed: %s" % (L)

	useDef()
	useDef("kellan")

	useDef(c="Jacobs", a="Kellan")

	unlimited(1,2,3,4,5,6,7,8,)