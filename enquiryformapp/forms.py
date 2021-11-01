from django import forms
from multiselectfield import MultiSelectFormField

class EnquiryForm(forms.Form):
    name = forms.CharField(
        label='enter your name:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your name:'
            }
        )
    )

    email = forms.EmailField(
        label='Enter your email id:',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'email.id'
            }
        )
    )

    mobile = forms.IntegerField(
        label='enter your mobile number:',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'mobile number'
            }
        )
    )

    COURSESE_CHOICES = (
        ('python', 'PYTHON'),
        ('django', 'DJANGO'),
        ('ui', 'UI')
    )
    course = MultiSelectFormField(label="select require course(s):",choices=COURSESE_CHOICES)

    FACULTY_CHOICES = (
        ('Narayana', 'NARAYANA'),
        ('hari', 'HARI'),
        ('Mohit', 'MOHIT')
    )
    faculties = MultiSelectFormField(label="select require faculty(s):",choices=FACULTY_CHOICES)

    COLOR_CHOICE = (
        ('green', 'GREEEN'),
        ('red', 'RED'),
        ('borwn', 'Brown'),
        ('white', 'White'),
        ('Black', 'Black')
    )
    color = forms.ChoiceField(label="Please select your color:",
                            widget=forms.Select,
                            choices=COLOR_CHOICE)

    LOCATION_CHOICES = (
        ('hyd','HEYDRABAD'),
        ('up','UP'),
        ('bang','BANGLURU')
    )
    locations = MultiSelectFormField(label="enetr your location:",choices=LOCATION_CHOICES)

    GENDER_CHOICES = (
        ('male','Male'),
        ('female','Female')
    )
    gender = forms.ChoiceField(label="select your gender:",
                               widget=forms.RadioSelect,
                               choices=GENDER_CHOICES)

    start_date = forms.DateField(label="select comfirtable date:",
        widget=forms.SelectDateWidget()
    )