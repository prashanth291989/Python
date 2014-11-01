from random import randrange
while True:
	a=randrange(5)
	b=randrange(10)
	print("INTEGER DIVISIONS")
	s=str(b)+"/"+str(a)+"="
	c=input(s)
	try:
		temp=b//a
		if(temp==int(c)):
			print("Correct")
		else:
			print("Incorrect");
	except ValueError:
		print("Please enter Integer Only")
	except ZeroDivisionError:
		print("Divide by zero exception occured")
	