import json
from cryptography.fernet import Fernet
import mysql.connector
import csv
try:
	all_values=[] 
	csvpath="df_data.csv"
	jsonfile="mylinux.json"
	data=[]
	with open(jsonfile,"r") as file:
		data=json.load(file)

	username=data["username"]
	password=data["password"]


	encode_pass=password.encode("UTF-8")
	
	key=Fernet.generate_key()
	f=Fernet(key)

	encrypt_pass=f.encrypt(encode_pass)


	decode_pass=f.decrypt(encrypt_pass)
	mysql_pass=decode_pass.decode("UTF-8")
	
	mydb= mysql.connector.connect(host="192.168.100.12",user=username,password=mysql_pass,database="alnafi",)
	#mysql connection object create

	#Fetching data
	with open(csvpath) as csv_file:
		csvfile = csv.reader(csv_file,delimiter=',')
	
		for row in csvfile:
			value = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
			all_values.append(value)
	query= "insert into my_df_data (filesystem,size,used,avail,usage_with_per,mounted_on,hostname,ip_address,datetime) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	mycursor =mydb.cursor()
	mycursor.executemany(query,all_values)
	mydb.commit()
	mydb.close()
#Executing

 
	print("Data inserted into database")
	mydb.close() 
except Exception as e:
    print (e)