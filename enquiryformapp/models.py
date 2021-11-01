from django.db import models
from multiselectfield import MultiSelectField


class Enquiry_data(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    mobile = models.BigIntegerField()

    COUSESE_CHOICES = (
        ('python','PYTHON'),
        ('django','DJANGO'),
        ('ui','UI')
    )
    course = MultiSelectField(max_length=100,choices=COUSESE_CHOICES)

    FACULTY_CHOICES = (
        ('Narayana','NARAYANA'),
        ('hari','HARI'),
        ('Mohit','MOHIT')
    )
    faculties = MultiSelectField(max_length=100,choices=FACULTY_CHOICES)

    LOCATION_CHOICES = (
        ('hyd','HEYDRABAD'),
        ('up','UP'),
        ('bang','BANGLURU')
    )
    locations = MultiSelectField(max_length=20,choices=LOCATION_CHOICES)
    COLOR_CHOICE = (
        ('green','GREEEN'),
        ('red','RED'),
        ('borwn','Brown'),
        ('white','White'),
        ('Black','Black')
    )
    color = models.CharField(max_length=10,choices=COLOR_CHOICE,default='White')

    gender = models.CharField(max_length=10)
    start_date = models.DateField(max_length=31)