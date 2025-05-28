from faker import Faker
import random
from app.models import *

faker = Faker()
def generate(n=100):

    for i in range(n):

        alldepts = department.objects.all()

        dept = alldepts[random.randint(0,len(alldepts)-1)]
        name = faker.name()
        email = faker.email()
        age = random.randint(20,35)
        
        sid = f"STD_{random.randint(100,999)}"

        studentid = stid.objects.create(stid=sid)

        student.objects.create(dept=dept,stid=studentid,name=name,email=email,age=age)

def setmarks():
    allstudent = student.objects.all()
    for students in allstudent:
        allsubject = subject.objects.all()
        for subjects in allsubject:
            marks.objects.create(student=students,subject=subjects,marks=random.randint(0,100))