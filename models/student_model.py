from mongoengine import Document, StringField, DateTimeField, BooleanField
from datetime import datetime
import bcrypt

class Student(Document):
    name = StringField(required=True)
    studentId = StringField(unique=True, required=True)
    email = StringField(required=True, unique=True, max_length=120)
    password = StringField(required=True)
    dataCreated = DateTimeField(default=datetime.utcnow)
    courseEnrolled = BooleanField(default=False)

    @classmethod
    def add_student(cls, name, studentId, email, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        student = cls(name=name, studentId=studentId, email=email, password=hashed_password.decode('utf-8'))
        student.save()
        return student

    @classmethod
    def get_student_by_id(cls, student_id):
        return cls.objects(studentId=student_id).first()

    @classmethod
    def delete_student(cls, student_id):
        student = cls.objects(studentId=student_id).first()
        if student:
            student.delete()
            return True
        return False

    @classmethod
    def edit_student(cls, student_id, **kwargs):
        student = cls.objects(studentId=student_id).first()
        if student:
            for key, value in kwargs.items():
                if hasattr(student, key):
                    setattr(student, key, value)
            student.save()
            return student
        return None

    def to_json(self):
        return {
            "name": self.name,
            "studentId": self.studentId,
            "email": self.email,
            "dataCreated": self.dataCreated.isoformat(),
            "courseEnrolled": self.courseEnrolled
        }
