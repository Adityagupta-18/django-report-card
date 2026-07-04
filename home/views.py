from django.shortcuts import render , HttpResponse
from home.models import *
from django.core.paginator import Paginator
from django.db.models import Q , Sum
# Create your views here.

def get_data(request):
    data=Student.objects.all()
    if request.GET.get('search'):
        search=request.GET.get('search')
        data=data.filter(
            Q(student_name__icontains=search) | Q(student_id__student_id__icontains=search)
        )
    paginator = Paginator(data, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context={"data": page_obj}
    return render(request,'home.html',context)

def result(request,student_id):
    queryset=subjectmarks.objects.filter(student__student_id__student_id=student_id)
    total=queryset.aggregate(total_marks=Sum('marks'))
    
    student=Student.objects.get(student_id__student_id=student_id)
    context={'queryset':queryset,'total':total,'student':student}
    return render(request,'result.html',context)

