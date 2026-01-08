import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","JobPortal.settings")
import django
django.setup()
from Job.models import BiharJob,Punejob,BangJob
from faker import Faker 
fake = Faker()
from random import randint
def phonenumber():
    num=randint(1000000000,9000000000)
    return num
def insertion_Bihar(n):
    for i in range(n):
        date=fake.date()
        company=fake.company()
        title=fake.random_element(['Software developer','Tester','Teacher'])       
        sal=fake.random_int(min=10000,max=50000)   
        address=fake.address()
        email=fake.email()
        phone=phonenumber()

        BiharJob.objects.get_or_create(
            date=date,
            company=company,
            title=title,
            address=address,
            email=email,
            salary=sal,
            phone=phone
        )

def insertion_Pune(n):
    for i in range(n):
        date=fake.date()
        company=fake.company()
        title=fake.random_element(['Software developer','Tester','Teacher'])       
        sal=fake.random_int(min=10000,max=50000)   
        address=fake.address()
        email=fake.email()
        phone=phonenumber()

        Punejob.objects.get_or_create(
            date=date,
            company=company,
            title=title,
            salary=sal,
            address=address,
            email=email,
            phone=phone
        )

def insertion_Bang(n):
    for i in range(n):
        date=fake.date()
        company=fake.company()
        title=fake.random_element(['Software developer','Tester','Teacher'])    
        sal=fake.random_int(min=10000,max=50000)   
        address=fake.address()
        email=fake.email()
        phone=phonenumber()

        BangJob.objects.get_or_create(
            date=date,
            company=company,
            title=title,
            address=address,
            salary=sal,
            email=email,
            phone=phone
        )

num1 = int(input('Enter Number of Records for Pune: '))
insertion_Pune(num1)
print(f'{num1} records inserted Successfully')
num2 = int(input('Enter Number of Records for Banglore: '))
insertion_Bang(num2)
print(f'{num2} records inserted Successfully')
num3 = int(input('Enter Number of Records for Bihar: '))
insertion_Bihar(num2)
print(f'{num3} records inserted Successfully')

        
