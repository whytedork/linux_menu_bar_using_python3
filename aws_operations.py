import os
from termcolor import colored

print (colored("""
Press 1  : to create a Key Pair .
Press 2  : to create a security group .
Press 3  : to create an EBS Volume .
Press 4  : to create a instance .
Press 5  : to create a S3 bucket.
Press 6  : to delete a S3 bucket.
Press 7  : to delete key pair.
Press 8  : to launch a instance with configured Web server 
Press 9  : to start a instance.
Press 10 : to stop a instance .
Press 11 : to terminate a instance .
Press 12 : to create a cloudfront distribution .
Press 13 : to attach the extra volume .
Press 14 : to exit from aws operations . 
""","red"))

while True:
    z = int (input ("Enter a no of your choice :"))

    if z == 4: #Creating a Instance 
     
        q = input ("Enter Image id :")
        w = input ("Specify Instance type : ")
        a = input ("Specify Key-pair : ")
        e = input ("Enter Security Group id : ")
        r = input ("Enter subnet-id : ")
        os.system ("aws ec2 run-instances  --image-id  {}  --instance-type {} --key-name {}  --security-group-ids {} --subnet-id {} --count 1   ".format(q,w,a,e,r))
    
     
    elif z == 1: #Creating a key-pair
        
        key_name =input("Enter key-name : ")
        os.system ( "aws ec2 create-key-pair --key-name {} ".format(key_name))
        print ("Task completed")        
            
    elif z == 2: #creating a security group
        
        description = input("Why are you creating this security group ? : ")
        group_name = input ("Enter a group name : ")
        os.system ( " aws ec2 create-security-group --description “ Making this security group for testing ”,format(description,group_name) --group-name “testing” " )
    
    elif z == 3: #creating a new ebs volume 
    
        size = int(input("Enter the size you want : "))
        az = input("Enter the zone where you want EBS volume to be deployed : ")
        type =input("Enter the volume type you want : ")
        os.system ( " aws ec2 create-volume availibilty-zone {} --size {} --volume-type {} ".format(az,size,type))

       
    elif z == 5: #creating a s3 bucket
    
        a = input(" Specify bucket name : ")
        b = input ("Specify Access Control List : ")
        c = input ("Mention region for the bucket to be deployed : ")
        os.system("aws s3api create-bucket --bucket {} --acl {} --create-bucket-configuration LocationConstraint={} ".format(a,b,c))

    elif z == 6: #to delete a s3 bucket
    
        a = input("Mention the name of the bucket to be deleted : ")
        os.system("aws s3api delete-bucket --bucket {}".format(a))

    elif z == 7: #to delete a keypair
    
        a = input("Mention the name of the key-pair to be deleted : ")
        os.system("aws ec2 delete-key-pair --key-name {} ".format(a))

    elif z == 8: #To run a instance with a configured web_server
    
    #creating a new instance 
    
        q = input ("Enter Image id : ")
        w = input ("Specify Instance type : ")
        a = input ("Specify Key-pair : ")
        e = input ("Enter Security Group id : ")
        r = input ("Enter subnet-id : ")
        os.system ("aws ec2 run-instances  --image-id  {}  --instance-type {} --key-name {}  --security-group-ids {} --subnet-id {} --count 1   ".format(q,w,a,e,r))
    
    
        #Configuring webpage
    
        ip = input ("Enter  ip of the instance : " )
        print("\t\t\tNOTE \nCheck the key downloaded and the program is in the same folder.")
        key = input ("Enter key-name without any extension :")
        os.system("ssh -l ec2-user {} -i {}.pem sudo yum install httpd  ".format(ip,key))
        webpage = input ("Enter the path where the web page is located : ")
        os.system("ssh -l ec2-user {} -i {}.pem sudo cp {} /var/www/html/".format(ip.key,webpage))
        os.system("ssh -l ec2-user {} -i {}.pem sudo systemctl start httpd ".format(ip,key))
    
    elif z == 9: #to start a instance
    
        instance_id = input("Enter Instance ids : ")
        os.system("aws ec2 start-instances --instance-ids {}".format(instance_id))

    elif z == 10: #to stop a instance 
    
        instance_id = input("Enter Instance ids : ")
        os.system("aws ec2 stop-instances --instance-ids {}".format(instance_id))

    elif z == 11: #to terminate a instance
     
        instance_id = input("Enter Instance ids : ")
        os.system("aws ec2 terminate-instances --instance-ids {}".format(instance_id))

    elif z == 12: #to create a cloudfront distribution
    
        origin = input("Enter origin domain name :")
        object1 = input ("Enter object name : ")
        os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazon.aws.com --default-root-object {}".format(origin,object1))

    elif z == 13: #to attach volume
 
        q = input ("Provide with a device name of the Volume to be attached (for ex: /dev/sdh) : ")
        w = input ("Provide with a instance id to which you want to connect the volume with : ")
        e = input ("Specify the Volume id : ")
        os.system("aws ec2 attach-volume  --device {} --instance-id {} --volume-id {} ".format(q,w,e))

    elif z == 14:
        os.system("exit")
        break

    else:
        print(colored("Invalid Input !!!!","red"))