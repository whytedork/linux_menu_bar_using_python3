from os import system as sys
from termcolor import colored

print(colored("""
Enter 1 : to install docker
Enter 2 : to see docker information
Enter 3 : to start docker services
Enter 4 : to see docker status
Enter 5 : to see images 
Enter 6 : to launch container
Enter 7 : to see running containers
Enter 8 : to stop container
Enter 9 : to pull image from docker hub
Enter 10 : to see network list
Enter 11 : to execute container running in background
Enter 12 : to delete image permanently
Enter 13 : to exit from docker operations
""","white"))

while True:

	x = int(input("Enter no. of your choice : "))

	if x == 1: # install docker
		sys("sudo yum install docker-ce --nobest")

	elif x == 2: # to check docker information
		sys("sudo docker info")

	elif x == 3: # to start docker service
		sys("sudo systemctl start docker")

	elif x == 4: # To See Docker Status
		sys("systemctl status docker")

	elif x == 5: # To see docker images
		sys('sudo docker images')
		print()
	elif x == 6: # to lauch container
		os_name = input("Enter os_name : ")
		image_name = input("Enter image_name : ")
		sys("sudo docker run -dit --name {} {}".format(os_name,image_name))
		print()

	elif x == 7: # to see complete list of running container
		sys('sudo docker ps -a')
		print()

	elif x == 8: # to stop container
		os_name = input("Enter os_name which you want to stop : ")
		sys('sudo docker rm -f {}'.format(os_name))
		print()

	elif x == 9: # to pull image from docker hub
		image_name = input("Enter image_name : ")
		tag = input("Enter tag_name : ")
		sys('sudo docker pull {}:{}'.format(image_name,tag))
		print()

	elif x == 10: # to see network list
		sys('sudo docker network ls')
		print()

	elif x == 11: # to execute container running in bg
		os_name = input("Enter os_name : ")
		sys('sudo docker exec -it {} bash'.format(os_name))
		print()
	elif x == 12: # To Delete Docker Image
		doc_ima = input("Enter Image name to delete")
		os.system("sudo docker rmi {}".format(doc_ima))

	elif x == 13:
		sys("exit")
		break

	else :
		print(colored("Invalid input !!!","red"))