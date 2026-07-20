from database import SessionLocal
from models import Student



class StudentRepository:


    def create(self, student):

        db = SessionLocal()


        new_student = Student(
            name=student["name"],
            age=student["age"]
        )


        db.add(new_student)

        db.commit()

        db.refresh(new_student)


        db.close()


        return new_student



    def get_all(self):

        db = SessionLocal()


        students = db.query(Student).all()


        db.close()


        return students



    def delete(self, student_id):

        db = SessionLocal()


        student = (
            db.query(Student)
            .filter(Student.id == student_id)
            .first()
        )


        if student:

            db.delete(student)

            db.commit()


        db.close()
