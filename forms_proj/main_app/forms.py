from django import forms
from .models import StudentData

class StudentForm(forms.Form):
    GENDER_CHOICE=(
        ("male", 'Male'),
        ("female", 'Female'),
    )

    full_name=forms.CharField(max_length=200, min_length=4, label="Names")
    email=forms.EmailField(max_length=100, label="email Address")
    birth_date=forms.DateField(help_text="enter your correct date of birth")
    address=forms.CharField(widget=forms.Textarea)
    gender=forms.ChoiceField(choices=GENDER_CHOICE)

class StudentForm2(forms.ModelForm):
    class Meta:
        model=StudentData
        fields=["names", "email", "birth_date", "address", "gender"]
        widgets={
            "birth_date":forms.DateInput(attrs={'class': 'form-control'}),
            "address":forms.Textarea(attrs={'class':'form-control', 'placeholder': 'enter yopur address'})
        }

    