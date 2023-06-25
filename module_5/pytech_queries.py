import python
import pip
import pymongo
import pymongo[srv]
import pyodbc 

#python -m pip install pymongo
#python -m pip install pymongo[srv]

# creation of MongoClient
client=MongoClient()
# Connect with the portnumber and host
url = "mongodb+srv://admin:admin@cluster0.wpmaubp.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
# Access database
mydatabase = client.pytech
# Access collection of the database
mycollection=mydatabase.students
  
# dictionary to be added in the database
rec={
title: 'MongoDB and Python', 
description: 'MongoDB is no SQL database', 
tags: ['mongodb', 'database', 'NoSQL'], 
viewers: 104 
}
  
# inserting the data in the database
rec = mydatabase.myTable.insert(record)

MongoDB: find()
docs = db.collection_name.find({})
 
for doc in docs:
 print(doc)
 
MongoDB: find_one() 
doc = db.collection_name.find_one({“student_id”: “1007”})
doc = db.collection_name.find_one({“student_id”: “1008”})
doc = db.collection_name.find_one({“student_id”: “1009”})

print(doc[“student_id”])