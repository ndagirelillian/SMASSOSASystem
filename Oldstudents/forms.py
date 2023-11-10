from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number', 'first_name', 'last_name', 'email', 
                  'field_of_work', 'location', 'profile_picture', 'telephone_number', 'year_of_entry', 'year_of_completion']
        labels = {
            'student_number': 'Person Number',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'field_of_work': 'Field of Work',
            'location': 'Location',
            'profile_picture': 'Profile Picture',
            'telephone_number': 'Telephone Number',
            'year_of_entry': 'Year of Entry',
            'year_of_completion': 'Year of Completion',
        }

        widgets = {
            'student_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'field_of_work': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'telephone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'year_of_entry': forms.Select(attrs={'class': 'form-control'}),
            'year_of_completion': forms.Select(attrs={'class': 'form-control'}),
        }
