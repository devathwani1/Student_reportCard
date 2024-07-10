from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import * 
from django.db.models import Q,Sum
from .seed import * 

# Create your views here.

def mainpage(request):
    return render(request,"base.html")

def get_students(request):
    queryset = Student.objects.all().order_by("student_id__student_id")

    search = request.GET.get('search');
    if request.GET.get('search'):
        queryset = queryset.filter(
            Q(student_name__icontains = search) |
            Q(student_id__student_id__icontains = search) |
            Q(student_age__icontains = search) )

    paginator = Paginator(queryset, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request,'report/students.html',{'queryset' : queryset,'page_obj' : page_obj})


def see_marks(request,student_id):
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
    total_marks = queryset.aggregate(total_marks = Sum("marks"))

  

    return render(request,'report/see_marks.html',{'queryset' : queryset,'total' : total_marks})