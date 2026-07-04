from home.models import *
import random
from django.db.models import Sum
from faker import Faker
fake=Faker()

def fakedata(n=10):
    try:
        for i in range(0,n):
            #selected department here:
            dep_obj=Department.objects.all()
            index=random.randint(0,len(dep_obj)-1)
            department=dep_obj[index]

            # making student id:
            id=f'STU-0{random.randint(100,999)}'
            name=fake.name()
            email=fake.email()
            age=random.randint(15,60)
            address=fake.address()

            student_id=StudentID.objects.create(student_id=id)
            student_obj=Student.objects.create(
                department=department,
                student_id=student_id,
                student_name=name,
                student_email=email,
                student_age=age,
                student_address=address,
            )

    except Exception as e:
        print(e)

            


def submarks():
    studobj=Student.objects.all()
    for stud in studobj:
        subjectobj=Subject.objects.all()
        for sub in subjectobj:
            submarks=subjectmarks.objects.create(
                student=stud,
                subject=sub,
                marks=random.randint(0,100)
            )

def rank():
    students=Student.objects.annotate(total_marks=Sum("studentmarks__marks")).order_by("-total_marks")
    for r,student in enumerate(students,start=1):
        student.rank=r
        student.save()