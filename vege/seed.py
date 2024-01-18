from faker import Faker
fake=Faker()
import random
from . models import *

def create_subject_marks(n):
    try:
        student_objs=Student.objects.all()
        for student in student_objs:
            subjects = Subject.objects.all()
            for subject in subjects:
                SubjectsMarks.objects.create(
                    student = student,
                    subject = subject,
                    marks = random.randint(0,100)
                )
    except Exception as e:
        print(e)
def seed_db(n=10)->None:
    try:
        for i in range(0,n):
            department_objs = Department.objects.all()
            random_index = random.randint(0,len(department_objs)-1)
            department = department_objs[random_index]
            student_id =  f'STU-0{random.randint(100, 999)}' 
            student_name = fake.name()
            student_email = fake.email()
            student_age=fake.random_int(min=18, max=99)            
            student_address = fake.address()


            student_id_obj = StudentID.objects.create(student_id = student_id )

            student_obj = Student.objects.create(
                department = department,
                student_id = student_id_obj,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age,
                student_address = student_address,
            )
    except Exception as e:
        print(e)



