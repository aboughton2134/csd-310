# 1007, 1008, and 1009.

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