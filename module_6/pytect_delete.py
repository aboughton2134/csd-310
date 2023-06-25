import python
import pip
import pymongo
import pymongo[srv]
import pyodbc 

# creation of MongoClient
client=MongoClient()
# Connect with the portnumber and host
url = "mongodb+srv://admin:admin@cluster0.wpmaubp.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
# Access database
mydatabase = client.pytech
# Access collection of the database
mycollection=mydatabase.students

# This should return the entire thing. Then it prints.
doc = mycollection.find()
print(doc)

#This is the insert_one and then displaying results.
record = { "first_name": "Ginny",
          "last_name": "Kray",
          "student_id": 1010}

new_student = mycollection.insert_one(record)
doc = mycollection.find()
print(doc)

#This is the delete_one for student_id 1010.
query ={"student_id":"1010"}
mycollection.delete_one(query)

# This should return the entire thing. Then it prints.
doc = mycollection.find()
print(doc)