from   fastapi import APIRouter

from models.student import   Student
from config.database import   connection
from schemas.student import  student_entity, list_of_student_entity
from bson import ObjectId


student_router = APIRouter()

@student_router.get('/student/{studentid}')
async  def find_student_by_id(studentid):
    student = connection.local.student.find_one({"_id": ObjectId(studentid)})
    return  student_entity(student)

@student_router.get('/students')
async  def find_all_students():
    return list_of_student_entity(connection.local.student.find())

@student_router.post('/student')
async  def create_student(student: Student):
    connection.local.student.insert_one(dict(student))
    print(student)
    return  list_of_student_entity(connection.local.student.find())

@student_router.put('/student/{studentid}')
async  def update_student(studentid, student: Student):
    connection.local.student.find_one_and_update(
        {"_id": ObjectId(studentid)},
        {"$set": dict(student)}
    )
    student_data = connection.local.student.find_one({"_id": ObjectId(studentid)})
    return student_entity(student_data)

@student_router.delete('/student/{studentid}')
async  def delete_student(studentid):
    student = connection.local.student.find_one_and_delete({"_id": ObjectId(studentid)})
    return  student_entity(student)