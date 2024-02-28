from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentData
from .forms import StudentForm, StudentForm2
from django.contrib.auth.decorators import login_required

# Create your views here.
# def home_page_view(request):
#     student_form=StudentForm()
#     if request.method =='POST':
#         full_name=request.POST.get("full_name")
#         email=request.POST.get("email")
#         birth_date=request.POST.get("birth_date")
#         address=request.POST.get("address")
#         gender=request.POST.get("gender")
#         StudentData.objects.create(names=full_name, email=email, birth_date=birth_date, address=address, gender=gender)
#     students=StudentData.objects.all()
#     context={
#             "students":students,
#             "forms":student_form
#     }
#     return render(request, "main/index.html", context)



def home_page_view(request):
    student_form=StudentForm2()
    if request.method =='POST':
        form_data=StudentForm2(request.POST)
        if form_data.is_valid():
            form_data.save()

    students=StudentData.objects.all()
    context={
            "students":students,
            "forms":student_form
    }
    return render(request, "main/index.html", context)

def delete_post(request, post_id):
    post=StudentData.objects.get(id=post_id)
    post.delete()
    return redirect("home")

@login_required
def edit_post(request, post_id):
    post_obj=get_object_or_404(StudentData, id=post_id)
    edit_form=StudentForm2(instance=post_obj)
    if request.method == "POST":
        form_data=StudentForm2(request.POST, instance=post_obj)
        if form_data.is_valid():
            form_data.save()
            return redirect("home")
    context={
        "edit_form":edit_form   
    }
    return render(request, "main/edit-post.html", context)




