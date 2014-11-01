class Animal:
	
	def __init__(self, name):
		self.name=name
		if(self.name=="elephant"):
			self.hints=["I am the largest land-living mammal in the world","I am herbivorous","I am belong to the family Elephantidae"]
		elif(self.name=="tiger"):
			self.hints=["I come in black and white or orange and black","I am carnivorous","I am the largest cat species"]
		else:
			self.hints=["I am pet animal","I am herbivorous","I am having mustache"]
	
		
	def guess_who_am_i(self):
		print("I will give you 3 hints, guess what animal I am\n");
		count=1
		while True:
			if(count==1):
				print(self.hints[0])
			elif(count==2):
				print(self.hints[1])
			elif(count==3):
				print(self.hints[2])
			str=input("Who am I?:")
			if(str==self.name):
				print("You got it! I am ",self.name,"\n")
				break;
			elif(count==3):
				print("I'm out of hints! The answer is: ",self.name,"\n") 
				break;
			else:
				print("Nope, try again!","\n")
				count=count+1;
				
			
e =Animal("elephant")
t = Animal("tiger")
b = Animal("cat")
e.guess_who_am_i()
t.guess_who_am_i()
b.guess_who_am_i()

