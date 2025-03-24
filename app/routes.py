from flask import Blueprint, request, jsonify
from datetime import datetime

students_bp = Blueprint('students', __name__)

# In-memory storage
students = []
next_id = 1

@students_bp.route('/students', methods=['POST'])
def create_student():
    global next_id
    data = request.get_json()
    
    student = {
        'id': next_id,
        'first_name': data['first_name'],
        'last_name': data['last_name'],
        'date_of_birth': data['date_of_birth'],
        'grade': data['grade'],
        'phone': data['phone'],
        'email': data['email']
    }
    
    students.append(student)
    next_id += 1
    return jsonify(student), 201

# Add all other route functions here...
