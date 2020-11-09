from os import system as sys
from termcolor import colored

print(colored(""" 
Enter 1 :launch python 
Enter 2 :Create or edit a python code 
Enter 3 :Run your python file
Enter 4 :Install a package
Enter 5 : To exit from python operations""","red"))

while True:
	x = int(input("Enter no. of your choice:"))
	if x == 1:
		sys('python3')
	elif x == 2 :
		fn = input("Enter file name to start writing code :")
		sys("subl {}".format(fn)) #sublime text editor
	elif x == 3 :
		pth = input("Enter name of the file you want to run :")
		sys("python3 {}".format(pth))
	elif x == 4 :
		nm = input ("Enter package name :")
		sys("pip3 install {}".format(nm))
	elif x == 5:
		sys("exit")
		break
	else :
		print(colored("Invalid input !!!","red"))