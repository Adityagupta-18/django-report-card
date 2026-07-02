from home.models import *
import random
from faker import Faker
fake=Faker()

def fakedata(n=10):
    dep_obj=Department.objects.all()
    index=random.randint(0,len(dep_obj)-1)