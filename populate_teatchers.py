import os
import random
import django
from faker import Faker
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
django.setup()
from first_app.models import Teacher

fakegen = Faker()

def populate(n=5):  # 5 tk tuleb neid või vastavalt nii palju mis nr sulgudes on
    #print(n)
    subjects = ['Maths', 'Art', 'English', 'Music', 'History', 'Science', 'Biology', 'Physical education']
    for entry in range(n):
        fake_name = fakegen.name()
        fake_subject = random.choices(subjects)[0]  #[0]- et ei näitaks tabelis kantsulgudes subjecte
        print(f'{fake_name}, {fake_subject}')
        # new entry to Student table
        teacher = Teacher.objects.get_or_create(name=fake_name, subject=fake_subject)

#populate()  # teeb 5 tk
#populate(20) # teeb 20 tk nimesid tabelisse
populate(10)