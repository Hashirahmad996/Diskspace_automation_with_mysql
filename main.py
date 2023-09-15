import os 
import paramiko
import json
import platform
import csv

# Define the SSH connection parameters
hostname = ""
username = ""
password = ""
databse = ""

# Initialize the SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the SSH server
client.connect(hostname=hostname, username=username, password=password)
sftp_client = client.open_sftp()

# Create an empty list to store JSON results
json_result = []

try:
    # Load JSON data from a file
    with open("mylinux.json", "r") as file:
        json_result = json.load(file)

    # Execute the OS flavor command
    os_stdin, os_stdout, os_stderr = client.exec_command(json_result["os_flavour"])
    my_os_output = os_stdout.read().decode().strip("\n")

    if my_os_output == "Ubuntu":
        # Execute the 'df' command
        df_stdin, df_stdout, df_stderr = client.exec_command(json_result["df_cmd"])
        mycmdout = df_stdout.read().decode()
        
        # Download a file from the remote server
        sftp_client.get("/home/hashir/myfile.csv", "df_data.csv")
        print("CSV file created in the current directory...")
    else: 
        print("Other OS found")    

except Exception as e:
    print("Someting went worng",e)
