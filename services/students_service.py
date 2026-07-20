from repositories.postgres_repository import PostgresStudentRepository



repository = PostgresStudentRepository()



class StudentService:


    def create_student(self, student):

        return repository.create(student)



    def get_students(self):

        return repository.get_all()



    def delete_student(self, student_id):

        return repository.delete(student_id)
