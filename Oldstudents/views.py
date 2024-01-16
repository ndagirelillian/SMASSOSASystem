from django.shortcuts import render
from .models import Student
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404


from .forms import StudentForm

# Create your views here.
def index(request):
    return render (request, 'students/index.html', {
        'students': Student.objects.all()
    })
 
def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def reports(request):
    return render (request,'students/reports.html')


def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_field_of_work = form.cleaned_data['field_of_work']
            new_location = form.cleaned_data['location']
            new_profile_picture = form.cleaned_data['profile_picture']
            new_telephone_number = form.cleaned_data['telephone_number']

            # Extract the new fields for Year of Entry and Year of Completion
            new_year_of_entry = form.cleaned_data['year_of_entry']
            new_year_of_completion = form.cleaned_data['year_of_completion']

            # Create and save the new student instance
            new_student = Student(
                student_number=new_student_number,
                first_name=new_first_name,
                last_name=new_last_name,
                email=new_email,
                field_of_work=new_field_of_work,
                location=new_location,
                profile_picture=new_profile_picture,
                telephone_number=new_telephone_number,
                year_of_entry=new_year_of_entry,
                year_of_completion=new_year_of_completion,
            )
            new_student.save()

            return render(request, 'students/add.html', {
                'form': StudentForm(),
                'success': True
            })
        else:
            return render(request, 'students/add.html', {
                'form': form
            })
    else:
        return render(request, 'students/add.html', {
            'form': StudentForm()
        })


    
def edit(request, id):
    # Retrieve the student instance or return a 404 response if not found
    student = get_object_or_404(Student, pk=id)

    if request.method == 'POST':
        # If the request method is POST, process the form data
        form = StudentForm(request.POST, instance=student)
        
        if form.is_valid():
            # Save the changes if the form is valid
            form.save()
            return render(request, 'students/edit.html', {
                'form': form,
                'success': True,
                'student': student,
            })
        else:
            # If the form is not valid, print errors for debugging
            print(form.errors)
    else:
        # If the request method is not POST, display the form
        form = StudentForm(instance=student)

    return render(request, 'students/edit.html', {
        'form': form,
        'student': student,
    })

# def edit(request, id):
#     student = get_object_or_404(Student, pk=id)

#     if request.method == 'POST':
#         form = StudentForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             return render(request, 'students/edit.html', {
#                 'form': form,
#                 'success': True,
#                 'student': student  # Pass the student object to the template
#             })
#     else:
#         form = StudentForm(instance=student)

#     return render(request, 'students/edit.html', {
#         'form': form,
#         'student': student  # Pass the student object to the template
#     })

def delete(request, id):
    try:
        student = get_object_or_404(Student, pk=id)
    except Student.DoesNotExist:
        # Handle the case where the student doesn't exist (e.g., show an error message).
        # You can customize this based on your requirements.
        return HttpResponseRedirect(reverse('index'))

    if request.method == 'POST':
        student = get_object_or_404(Student, pk=id)
        student.delete()
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'students/delete.html', {'student': student})



def all_students(request):
    students = Student.objects.all()
    return render(request, 'all_students.html', {'students': students})

def students_by_field(request, field_name):
    students = Student.objects.filter(field_of_work=field_name)
    return render(request, 'students_by_field.html', {'students': students, 'field_name': field_name})

def students_by_year(request, year):
    students = Student.objects.filter(year_of_completion=year)
    return render(request, 'students_by_year.html', {'students': students,})