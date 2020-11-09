from os import system as sys
import getpass
from termcolor import colored
import smtplib

#code for banner and designs
print(sys("figlet ARTH  2020"))
print()

#read password from file
f = open("password.txt",'r')
password = f.readline()

#password setup
x = getpass.getpass("Enter Your Password : ")
if x == password:
	print(colored("LogIn Successfull !","red"))
	print()
else :
	print(colored("Password is Incorrect !","red"))

#menu-program-features

if x == password:
	while True:
		print(colored("""Enter 1  : For Linux Operations
Enter 2  : For Python Operations 
Enter 3  : For Docker Operations
Enter 4  : For AWS Operations
Enter 5  : For Hadoop Operations
Enter 6  : To Exit from Main Program
	""","blue"))

		choice = int(input("Enter Your Choice : "))

		if choice == 1:
			sys("python linux_operations.py")
			
		elif choice == 2:
			sys("python python_operations.py")
		
		elif choice == 3:
			sys("python docker_operations.py")

		elif choice == 4:
			sys("python aws_operations.py")

		elif choice == 5:
			sys("python hadoop_operations.py")

		elif choice == 6:
			sys("exit")
			print(colored("Thanks For Using","red"))
			break
		else :
			print(colored("Invalid Choice","red"))