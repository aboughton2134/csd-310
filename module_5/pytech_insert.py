# 1007, 1008, and 1009.

MongoDB: insert_one()
ida = {
 “first_name”: “Ida”
}

MongoDB: insert_one()
sara = {
 “first_name”: “Sara”
}

MongoDB: insert_one() 
linus = {
 “first_name”: “Linus”
}

ida_student_id = students.insert_one(ida).inserted_id
sara_student_id = students.insert_one(sara).inserted_id
linus_student_id = students.insert_one(linus).inserted_id

print(ida_student_id)
print(sara_student_id)
print(linus_student_id)