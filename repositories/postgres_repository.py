from database import SessionLocal
from models import Student


class PostgresStudentRepository:

    def create(self, student):

        db = SessionLocal()

        try:
            new_student = Student(
                name=student["name"],
                age=student["age"]
            )

            db.add(new_student)
            db.commit()
            db.refresh(new_student)

            return new_student

        finally:
            db.close()


    def get_all(self):

        db = SessionLocal()

        try:
            students = db.query(Student).all()

            return students

        finally:
            db.close()


    def delete(self, student_id):

        db = SessionLocal()

        try:
            student = db.query(Student).filter(
                Student.id == student_id
            ).first()

            if student:

                db.delete(student)
                db.commit()

                return student

            return None

        finally:
            db.close()
