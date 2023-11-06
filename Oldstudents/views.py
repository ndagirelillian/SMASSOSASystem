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
def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)  # Include 'request.FILES' to handle file uploads
        if form.is_valid():
            # Extract the new fields from the form data
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_field_of_work = form.cleaned_data['field_of_work']
            new_location = form.cleaned_data['location']
            new_profile_picture = form.cleaned_data['profile_picture']
            new_telephone_number = form.cleaned_data['telephone_number']

            # Create and save the new student instance
            new_student = Student(
                student_number=new_student_number,
                first_name=new_first_name,
                last_name=new_last_name,
                email=new_email,
                field_of_work=new_field_of_work,
                location=new_location,
                profile_picture=new_profile_picture,
                telephone_number=new_telephone_number
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

    # Handle the GET request
    else:
        return render(request, 'students/add.html', {
            'form': StudentForm()
        })
    


def edit(request, id):
    student = get_object_or_404(Student, pk=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit.html', {
                'form': form,
                'success': True,
                'student': student  # Pass the student object to the template
            })
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/edit.html', {
        'form': form,
        'student': student  # Pass the student object to the template
    })

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