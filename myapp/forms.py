from django import forms
class Employeeform(forms.Form):
    
    name=forms.CharField()

    department=forms.CharField()

    salary=forms.IntegerField()

    location=forms.CharField()

    email=forms.EmailField()

    address=forms.CharField()

