# SER-531-Project-Team_13
Team 13 - Team members:
1. Yogaleena Mandalapu
2. Praneeth Sai Kumar Reddy Kallam
3. Yashwanth Dantanoor
4. Saiteja Reddy Cheela
5. Sanjana Mukundan

How to run the project:
1. Fetch the data from API_auth.py
2. Run the data.html file to get the events for that particular location on an HTML page.
3. Fuseki can be used to query through the data.
4. Owl files are deployed onto Fuseki server using AWS instances.

To start fuseki instances:
   ("brew install putty" if not already installed)
1. Go to the API folder containing the .pem file to run the instances.
2. And to connect with shell instance from terminal we need to use SSH protocol(Note: Go to the project folder with .pem file before executing command):
   1. ssh -i "fusekitester.pem" ec2-user@ec2-18-216-12-185.us-east-2.compute.amazonaws.com
   2. ssh -i "fusekitester.pem" ec2-user@ec2-18-224-190-72.us-east-2.compute.amazonaws.com
   3. ssh -i "fusekitester.pem" ec2-user@ec2-3-144-164-66.us-east-2.compute.amazonaws.com
3. Then run these commands to start fuseki server in each terminal execute: "cd apache-jena-fuseki-4.2.0/"  and :
   1. for instance one "./fuseki-server --file /home/ec2-user/yasheventdata.owl /eventcategory"
   2. for instance one "./fuseki-server --file /home/ec2-user/yashtweetdata.owl /projecttweetdata"
   3. for instance one "./fuseki-server --file /home/ec2-user/yashuserdata.owl /userdata"
5. The 3 instances are:
   1. http://ec2-18-216-12-185.us-east-2.compute.amazonaws.com:3030/
   2. http://ec2-18-224-190-72.us-east-2.compute.amazonaws.com:3030/
   3. http://ec2-3-144-164-66.us-east-2.compute.amazonaws.com:3030/




Youtube - https://youtu.be/QbS8mHNWHLc

Google Drive - https://drive.google.com/drive/folders/17jc7ZQadIOLMwQt8P7wJsQUv2W5gb_T1?usp=sharing
