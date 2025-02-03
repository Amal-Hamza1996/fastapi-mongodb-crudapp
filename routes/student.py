from models.student import Student
from fastapi import APIRouter
from config.database import connection
from schemas.student import list_of_students_entity, student_entity
from bson import ObjectId
student_router = APIRouter()

"""
this is the endpoint that will be used to test if the server is running
"""
@student_router.get('/hello')
async def hello_world():
    return "Hello world"

"""
this is the endpoint that will be used to get all the students from the database
getting all the students from the database 
"""
@student_router.get('/students')
async def find_all_students():
    return connection.local.student.find()

"""
this is the endpoint that will be used to get a student by id
"""
@student_router.get('/students/{student_id}')
def find_students_by_id(student_id: str):
    return student_entity(connection.local.student.find_one({"_id": ObjectId(student_id)}))

"""
this is the endpoint that will be used to create a student
"""
@student_router.post('/students')
async def create_student(student: Student):
    connection.local.student.insert_one(dict(student))
    return list_of_students_entity(connection.local.student.find())

"""
this is the endpoint that will be used to update a student
"""
@student_router.put('/students/{student_id}')
async def update_student(student_id: str, student: Student):
    # find the student by id and update it with the new student data
    connection.local.student.find_one_and_update(
        {"_id": ObjectId(student_id)},
        {"$set": dict(student)}
    )
    return student_entity(connection.local.student.find_one({"_id": ObjectId(student_id)}))

"""
this is the endpoint that will be used to delete a student
"""
@student_router.delete('/students/{student_id}')
async def delete_student(student_id: str):
    return student_entity(connection.loal.student.find_one_and_delete({"_id": ObjectId(student_id)})) # find the student deletes it and also return the same object
