print('\033[1;34;40m            Body mass index (BMI) CALCULATOR   \n ')
print("\033[1;32;40m")
print(" Enter the following details to calculate your Body mass index (BMI) \n ")
Height=float(input(" Enter your height in centimeters(ex:175) : "))
Weight=float(input(" Enter your Weight in Kg: "))
Height = Height/100
BMI=Weight/(Height*Height)
print("your Body Mass Index is: ",BMI)
if(BMI>0):
	if(BMI<=16):
		print("you are severely underweight")
	elif(BMI<=18.5):
		print("you are underweight")
	elif(BMI<=25):
		print("you are Healthy")
	elif(BMI<=30):
		print("you are overweight ")
	else: print("you are severely overweight")

else:("enter valid details")

print("\n\033[1;37;40m  ©DEEPAK DHARSHAN \033[0;37;40m\n")

