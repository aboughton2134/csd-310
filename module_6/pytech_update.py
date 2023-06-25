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

#This is updating the last name for student_id 1007.
filter = {“student_id”: “1007”}
new_values = {"$set":{"last_name": "Little"}}
mycollection.update_one(filter, newvalues)

#This is finding the student_id with 1007 and then printing it.
doc = db.students.find_one({“student_id”: “1007”})
print(doc)