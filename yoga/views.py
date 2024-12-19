from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Staff
from .forms import StudentForm, StaffForm

# Homepage view
def home(request):
    return render(request, 'index.html')

# View for listing all students
def view_students(request):
    students = Student.objects.all()
    return render(request, 'view_students.html', {'students': students})

# View for listing all staff
def view_staff(request):
    staff_list = Staff.objects.all()  # Fetch all staff entries from the database
    return render(request, 'view_staff.html', {'staff_list': staff_list})

# Create or update a student
def manage_student(request, student_id=None):
    if student_id:
        student = get_object_or_404(Student, id=student_id)
    else:
        student = None

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('view_students')
    else:
        form = StudentForm(instance=student)

    return render(request, 'manage_student.html', {'form': form})

# Create or update staff
def manage_staff(request, staff_id=None):
    if staff_id:
        staff = get_object_or_404(Staff, id=staff_id)
    else:
        staff = None

    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('view_staff')
    else:
        form = StaffForm(instance=staff)

    return render(request, 'manage_staff.html', {'form': form})

# Delete a student
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('view_students')

# Delete staff
def delete_staff(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)
    staff.delete()
    return redirect('view_staff')
