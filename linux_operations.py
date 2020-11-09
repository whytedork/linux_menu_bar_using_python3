from os import system as sys
from termcolor import colored
import getpass
import smtplib

print(colored("""Enter 1  : to login as root user
Enter 2  : to see date & time 
Enter 3  : to open calculator
Enter 4  : to create new user
Enter 5  : to install new software or tool
Enter 6  : to open new terminal 
Enter 7  : to open text-editor
Enter 8  : to update whole system
Enter 9  : to scan website using nmap
Enter 10 : to check ip address
Enter 11 : to ping
Enter 12 : to configure web server
Enter 13 : to create banners
Enter 14 : to run any command
Enter 15 : to launch browser
Enter 16 : to search location of installed software/tool
Enter 17 : to open website
Enter 18 : to send an email
Enter 19 : to exit from linux operations
	""","white"))

while True:
	choice = int(input("Enter the no of your choice:"))

	if(choice == 1):
		sys("sudo su")
		print()

	elif choice == 2:
		sys("date")
		print()

	elif choice == 3:
		sys("bc")
		print()

	elif choice == 4:
		print("Enter user name : ",end="")
		create_user = input()
		sys("useradd {}".format(create_user))
		print()

	elif choice == 5:
		print("Enter software name : ",end="")
		software_name=input()
		sys("sudo yum install {}".format(software_name))
		print()

	elif choice == 6:
		sys("gnome-terminal")
		print()

	elif choice == 7:
		sys("vim new.txt") #open a new txt file in sublime text editor
		print()

	elif choice == 8:
		sys("sudo yum update")
		print()

	elif choice == 9:
		print("Enter Website or IP : ",end="")
		website = input()
		sys("nmap {}".format(website))
		print()

	elif choice == 10:
		sys("ifconfig")
		print()

	elif choice == 11:
		print("Enter Website or IP : ",end="")
		website = input()
		sys("ping {}".format(website))
		print()

	elif choice == 12:
		sys("sudo apt-get install apache2")
		print()

	elif choice == 13:
		print("enter banner name : ",end="")
		banner_name = input()
		sys("figlet {}".format(banner_name))
		print()

	elif choice == 14:
		print("enter command : ",end="")
		new_cmd = input()
		sys("{}".format(new_cmd))
		print()

	elif choice == 15:
		sys("firefox")
		print()

	elif choice == 16:
		print("Enter name : ",end="")
		s_file = input()
		sys("which {}".format(s_file))
		print()

	elif choice == 17:
		print("Enter website name : ",end="")
		website = input()
		sys("firefox {}".format(website))
		print()

	elif choice == 18:
		sender_email = input(str("Enter your email :"))
		rec_email = input(str("Enter receiver_email :"))
		message = input("Enter your message : ")
		password = getpass.getpass("Enter Your Password : ")
		server = smtplib.SMTP('smtp.gmail.com',587)
		server.ehlo()
		server.starttls()
		server.login(sender_email,password)
		print("LogIn Successfull")
		server.sendmail(sender_email,rec_email,message)
		print("Your Email has been sent to : ",rec_email)

	elif choice == 19:
		sys("exit")
		break

	else:
		print(colored("Invalid Choice","red"))