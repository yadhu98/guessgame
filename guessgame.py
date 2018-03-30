import random

while(1):
	name=str(raw_input("enter your name:"))
	print "hello"+" "+name+" "+"so the game is that I have think about  a number which is between  0 to 20,can you guess it,I will give you 6 chance to predict the number so are you ready?"
	ch=str(raw_input("yes(y)/no(n):"))
	if(ch=='n'):
			exit(0)
	elif(ch=='y'):
					no= random.randint(1, 20)
					for  i in range (0,6):
						pred=input("tell the number")
						if(no==pred):
							flag=1
							break
						elif(no>pred):
							print("less than the number")
						elif(no<pred):
							print("greater than the number")
					if(flag==1):
						print("your prediction was right")
						
					if(i>6):
						print("No more chances")
					

