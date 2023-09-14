import os 
import paramiko
import json
import platform
import csv
hostname=""
username=""
password=""
databse=""






client= paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname,username=username,password=password)
sftp_cleint=client.open_sftp()

json_result=[]

try:
    
    with open("mylinux.json","r") as file:
        json_result=json.load(file)
        
    
    
    os_stdin, os_stdout, os_stderr = client.exec_command(json_result["os_flavour"])
    my_os_output=os_stdout.read().decode().strip("\n")
    
    if my_os_output == "Ubuntu":
        df_stdin, df_stdout, df_stderr = client.exec_command(json_result["df_cmd"])
        mycmdout=df_stdout.read().decode()
        print(mycmdout)
        sftp_cleint.get("/home/hashir/myfile.csv","df_data.csv")
            
        print ("CSV file created in the current directory...")
        
    else: 
        print("other os found")    
        
    
    
except Exception as e:
    print(e)
    