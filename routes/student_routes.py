from flask import Blueprint, request, jsonify
from services.students_service import StudentService


student_bp = Blueprint(
    "students",
    __name__
)


service = StudentService()



@student_bp.route("/students", methods=["POST"])
def create_student():

    data = request.json

    student = service.create_student(data)

    return jsonify({
        "id": student.id,
        "name": student.name,
        "age": student.age
    })



@student_bp.route("/students", methods=["GET"])
def get_students():

    students = service.get_students()


    return jsonify([
        {
            "id": s.id,
            "name": s.name,
            "age": s.age
        }

        for s in students
    ])



@student_bp.route(
    "/students/<int:id>",
    methods=["DELETE"]
)
def delete_student(id):

    service.delete_student(id)


    return jsonify({
        "message":"Student deleted"
    })
