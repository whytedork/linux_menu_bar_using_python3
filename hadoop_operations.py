import os
from termcolor import colored

print(colored("""
Press 1 : To configure and start the name node 
Press 2 : To configure and start the data node 
Press 3 : To stop name node 
Press 4 : To stop data node 
Press 5 : To contribute limited amount of space to data node/hadoop cluster (static storage )
Press 6 : To exit from Hadoop Operations
""","white"))

while True:
    z = int(input("Enter a number of your choice : "))

    if z == 1:
        remote_ip = int(input("Enter the ip which you want to configure as a Namenode "))
        print ("\t\t\tNOTE \n\n Software should be present under the root directory(root/jdk-8u171-linux-x64.rpm , hadoop-1.2.1-1.x86_64.rpm )  ")
        os.system("ssh -l root {} rpm -iv /root/jdk-8u171-linux-x64.rpm".format (remote_ip))
        os.system("ssh -l root {} rpm ivh /root/hadoop-1.2.1-1.x86_64.rpm --force".format(remote_ip))
    
        #Configuring core-site.xml file 
    
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<configuration\> >> core-site.xml\"".format(remote_ip))
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<property\> >> core-site.xml\"".format(remote_ip))
    
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<name\> fs.default.name \<\/name\> >> core-site.xml\"".format(remote_ip))
    

        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<value\> hdfs://0.0.0.0:9001 \<\/value\> >> core-site.xml\"".format(remote_ip))
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<\/property\> >> core-site.xml\"".format(remote_ip))
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<\/configuration\> >> core-site.xml\"".format(remote_ip))
    
        #configuring hdfs-site.xml file
    
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<configuration\> >> core-site.xml\"".format(remote_ip))
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<property\> >> core-site.xml\"".format(remote_ip))
    
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<name\> dfs.name.dir \<\/name\> >> core-site.xml\"".format(remote_ip))
    
        dir = input("Enter the name of the directory you want to create for the name node ")
        os.system("ssh -l root -o PasswordAuthenticatio=yes {} mkdir /{}".format(remote_ip,dir) )
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<value\> /{} \<\/value\> >> core-site.xml\"".format(remote_ip,dir))
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<\/property\> >> core-site.xml\"".format(remote_ip))
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<\/configuration\> >> core-site.xml\"".format(remote_ip))
    
        #starting the namenode 
              
        os.system("ssh -l root -o PasswordAuthentication=yes {} hadoop namenode -format ".format(remote_ip))
    
        os.system("ssh -l root -o PasswordAuthenticatio=yes {} hadoop-daemon.sh start namenode ".format(remote_ip))

    elif z == 2:
        remote_ip = int(input("Enter the ip which you want to configure as a Datanode "))
        print ("\t\t\tNOTE \n\n Software should be present under the root directory(root/jdk-8u171-linux-x64.rpm , hadoop-1.2.1-1.x86_64.rpm )  ")
        os.system("ssh -l root {} rpm -iv /root/jdk-8u171-linux-x64.rpm".format (remote_ip))
        os.system("ssh -l root {} rpm ivh /root/hadoop-1.2.1-1.x86_64.rpm --force".format(remote_ip))
    
        #Configuring core-site.xml file 
    
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<configuration\> >> core-site.xml\"".format(remote_ip))
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<property\> >> core-site.xml\"".format(remote_ip))
    
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<name\> fs.default.data \<\/name\> >> core-site.xml\"".format(remote_ip))
    
        ip = input("Enter namenode ip ")

        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<value\> hdfs://{}:9001 \<\/value\> >> core-site.xml\"".format(remote_ip,ip))
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<\/property\> >> core-site.xml\"".format(remote_ip))
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<\/configuration\> >> core-site.xml\"".format(remote_ip))
    
        #configuring hdfs-site.xml file
    
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<configuration\> >> core-site.xml\"".format(remote_ip))
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<property\> >> core-site.xml\"".format(remote_ip))
    
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<name\> dfs.name.dir \<\/name\> >> core-site.xml\"".format(remote_ip))
    
        dir = input("Enter the name of the directory you want to create for the data node ")
        os.system("ssh -l root -o PasswordAuthenticatio=yes {} mkdir /{}".format(remote_ip,dir) )
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<value\> /{} \<\/value\> >> core-site.xml\"".format(remote_ip,dir))
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<\/property\> >> core-site.xml\"".format(remote_ip))
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<\/configuration\> >> core-site.xml\"".format(remote_ip))
    
        os.system("ssh -l root -o PasswordAuthentication=yes {} hadoop-daemon.sh start datanode ".format(remote_ip))
  
 
    elif z == 3:
        remote_ip = int(input("Enter the Datanode ip which you want to stop "))
        os.system("ssh -l root -o PasswordAuthentication=yes {} hadoop-daemon.sh stop datanode ".format(remote_ip))  

              
    elif z == 4:
        remote_ip = int(input("Enter the Datanode ip which you want to stop "))
        os.system("ssh -l root -o PasswordAuthentication=yes {} hadoop-daemon.sh stop datanode ".format(remote_ip))
              
    elif z == 5:
                       
        remote_ip = int(input("Enter the ip which you want to configure as a Datanode "))
        print ("\t\t\tNOTE \n\n Software should be present under the root directory(root/jdk-8u171-linux-x64.rpm , hadoop-1.2.1-1.x86_64.rpm )  ")
        os.system("ssh -l root {} rpm -iv /root/jdk-8u171-linux-x64.rpm".format (remote_ip))
        os.system("ssh -l root {} rpm ivh /root/hadoop-1.2.1-1.x86_64.rpm --force".format(remote_ip))
    
        #Configuring core-site.xml file 
    
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<configuration\> >> core-site.xml\"".format(remote_ip))
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<property\> >> core-site.xml\"".format(remote_ip))
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<name\> fs.default.data \<\/name\> >> core-site.xml\"".format(remote_ip))
    
        ip = input("Enter namenode ip ")

        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<value\> hdfs://{}:9001 \<\/value\> >> core-site.xml\"".format(remote_ip,ip))
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<\/property\> >> core-site.xml\"".format(remote_ip))
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<\/configuration\> >> core-site.xml\"".format(remote_ip))
    
        #configuring hdfs-site.xml file
    
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<configuration\> >> core-site.xml\"".format(remote_ip))
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<property\> >> core-site.xml\"".format(remote_ip))
    
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<name\> dfs.name.dir \<\/name\> >> core-site.xml\"".format(remote_ip))
        #creating a limited storage and mounting to the datanode dir .
    
        partition = input("Enter the name of the partition ")
        size = int (input("Enter the size of the directory you want to make "))
              
        os.system("ssh -l root -o PasswordAuthentication=yes {} fdisk {}  ".format(remote_ip,partition))
        os.system("ssh -l root -o PasswordAuthentication=yes {}  n ".format(remote_ip))
        os.system("ssh -l root -o PasswordAuthentication=yes {}  p ".format(remote_ip))
        os.system("ssh -l root -o PasswordAuthentication=yes {}  1 ".format(remote_ip))
    
        os.system("ssh -l root -o PasswordAuthentication=yes {}  1024 ".format(remote_ip))
    
        os.system("ssh -l root -o PasswordAuthentication=yes {}  {} ".format(remote_ip,size))
    
        #formatting the partition.
              
        device_name =input("Enter the device name you created ")         
        os.system("ssh -l root -o PasswordAuthentication=yes {} mkfs.ext4 {} ".format(remote_ip,device_name))
     
        #mount the partition.
              
        dir = input("Enter the name of the directory you want to create for the data node ")
              
        os.system("ssh -l root -o PasswordAuthentication=yes {}  mount {} {} ".format(remote_ip,device_name,dir))
              
    
    
        os.system("ssh -l root -o PasswordAuthenticatio=yes {} mkdir /{}".format(remote_ip,dir) )
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<value\> /{} \<\/value\> >> core-site.xml\"".format(remote_ip,dir))
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<\/property\> >> core-site.xml\"".format(remote_ip))
    
        os.system("ssh -l root -o PasswordAuthentication=yes  {} \"cd /etc/hadoop ;echo \<\/configuration\> >> core-site.xml\"".format(remote_ip))
    
        os.system("ssh -l root -o PasswordAuthenticatio=yes {} hadoop-daemon.sh start datanode ".format(remote_ip))

    elif z == 6:
        os.system("exit")
        break
    else:
        print(colored("Invalid Input!!!!!!","red"))