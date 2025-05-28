from django.shortcuts import render
from app.models import *
from django.core.paginator import Paginator
from django.db.models import Sum

# Create your views here.
def index(request):
    allstudents = student.objects.all()
    paginator = Paginator(allstudents, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"index.html",{"students":page_obj})

def marksheet(request):
    id = int(request.GET['id'])
    allstudents = marks.objects.filter(student_id=id)
    # sum=0
    # for st in allstudents:
    #     sum+=st.marks

    sum = allstudents.aggregate(total=Sum("marks"))

    rankstudent = student.objects.annotate(total=Sum("marks__marks")).order_by("-total")
    count=0
    for rank in rankstudent:
        count+=1
        if rank.id==id:
            break

    return render(request,"marksheet.html",{'students':allstudents,'sum':sum,'count':count})