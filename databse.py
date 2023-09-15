import json
from cryptography.fernet import Fernet
import mysql.connector
import csv

try:
    # Create an empty list to store CSV values
    all_values = [] 

    # Define the path to the CSV file
    csvpath = "df_data.csv"

    # Define the path to the JSON file
    jsonfile = "mylinux.json"

    # Initialize the 'data' variable
    data = []

    # Load data from the JSON file
    with open(jsonfile, "r") as file:
        data = json.load(file)

    # Extract the 'username' and 'password' from the JSON data
    username = data["username"]
    password = data["password"]

    # Encode the password to bytes
    encode_pass = password.encode("UTF-8")

    # Generate an encryption key
    key = Fernet.generate_key()

    # Create a Fernet cipher object
    f = Fernet(key)

    # Encrypt the password
    encrypt_pass = f.encrypt(encode_pass)

    # Decrypt the password
    decode_pass = f.decrypt(encrypt_pass)

    # Convert the decrypted password back to a string
    mysql_pass = decode_pass.decode("UTF-8")

    # Establish a connection to the MySQL database
    mydb = mysql.connector.connect(host="192.168.100.12", user=username, password=mysql_pass, database="alnafi")

    # Open the CSV file for reading
    with open(csvpath) as csv_file:
        csvfile = csv.reader(csv_file, delimiter=',')

        # Iterate through the CSV rows and create a list of values
        for row in csvfile:
            value = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            all_values.append(value)

    # Define the SQL query to insert data
    query = "INSERT INTO my_df_data (filesystem, size, used, avail, usage_with_per, mounted_on, hostname, ip_address, datetime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

    # Create a cursor object
    mycursor = mydb.cursor()

    # Execute the query with the list of values
    mycursor.executemany(query, all_values)

    # Commit the changes to the database
    mydb.commit()

    # Close the database connection
    mydb.close()

    print("Data inserted into the database")
    
except Exception as e:
    print("something went wrong",e)
