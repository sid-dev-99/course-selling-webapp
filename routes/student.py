from flask import jsonify, request, Blueprint
from mongoengine import connect
from models.student_model import Student
from dotenv import load_dotenv
import os

load_dotenv()

student_bp = Blueprint('student', __name__)
mongo_url = os.getenv('url')

connect('students_db', host=mongo_url)

@student_bp.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.get_student_by_id(student_id)
    if student:
        return jsonify(student.to_json())
    else:
        return jsonify({'error': 'Student not found'}), 404

@student_bp.route('/students/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    if Student.delete_student(student_id):
        return jsonify({'message': 'Student deleted successfully'})
    else:
        return jsonify({'error': 'Student not found'}), 404

@student_bp.route('/students', methods=['POST'])
def add_student():
    print("received a post req ")
    data = request.get_json()
    student = Student.add_student(
        name=data['name'],
        studentId=data['studentId'],
        email=data['email'],
        password=data['password']
    )
    return jsonify(student.to_json()), 201


