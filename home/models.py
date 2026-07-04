from django.db import models

# Create your models here.
class Department(models.Model):
    department=models.CharField( max_length=50)


    def __str__(self):
        return self.department

    class Meta:
        ordering=['department']


class StudentID(models.Model):
    student_id=models.CharField(max_length=10)

    def __str__(self):
        return self.student_id

    class Meta:
        ordering=['student_id']



class Student(models.Model):
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    student_id=models.ForeignKey(StudentID,on_delete=models.CASCADE)
    student_name=models.CharField(max_length=50)
    student_email=models.CharField(max_length=30)
    student_age=models.IntegerField()
    student_address=models.CharField(max_length=100)
    rank=models.IntegerField(default=0)

    def __str__(self):
        return self.student_name
    
    class Meta:
        ordering=['student_name']

class Subject(models.Model):
    subject=models.CharField(max_length=20)

    def __str__(self):
        return self.subject

class subjectmarks(models.Model):
    student=models.ForeignKey(Student,related_name='studentmarks',on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks=models.IntegerField()

    def __str__(self):
        return self.student.student_name
    
    class Meta:
        ordering=['student']