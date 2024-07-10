from faker import Faker
from .models import * 
from django.db.models import Sum
import random
fake = Faker()

def seed_db(n)->None:
    for i in range(0,n):
        department_obj = Department.objects.all()
        random_index = random.randint(0,len(department_obj)-1)
        department = department_obj[random_index]
        student_id = f'STU-0{random.randint(100,999)}'
        subjects = Subject.objects.all()

        student_name = fake.name()
        student_email = fake.email()
        student_age = random.randint(20,30)
        student_address = fake.address()

        student_id_obj = StudentId.objects.create(student_id = student_id)

        student_obj = Student.objects.create(
            department = department,
            student_id = student_id_obj,
            student_name = student_name,
            student_email = student_email,
            student_age = student_age,
            student_address = student_address
        )

        for sub in subjects:
            SubjectMarks.objects.create(
                student = student_obj,
                subject = sub,
                marks = random.randint(20,100)
            )


def genearte_report_card():
    current_rank = -1
    i  = 1

    ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks' , 'student_age')

    for rank in ranks:
        ReportCard.objects.create(
            student = rank,
            student_rank = i
        )
            
        i += 1    
    

        

