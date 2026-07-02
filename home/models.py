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
    student_email=models.CharField(max_length=20)
    student_age=models.IntegerField()
    student_address=models.CharField(max_length=100)