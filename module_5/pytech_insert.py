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

MongoDB: insert_one()
ida = {
 “first_name”: “Ida”
 "last_name": "Hope"
}

MongoDB: insert_one()
sara = {
 “first_name”: “Sara”
 "last_name": "Tachin"
}

MongoDB: insert_one() 
linus = {
 “first_name”: “Linus”
 "last_name": "Yodlee"
}

ida_student_id = students.insert_one(1007).inserted_id
sara_student_id = students.insert_one(1008).inserted_id
linus_student_id = students.insert_one(1009).inserted_id

print(ida_student_id)
print(sara_student_id)
print(linus_student_id)