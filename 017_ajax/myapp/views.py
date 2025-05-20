from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

from myapp.models import *

# Create your views here.
def index(request):
    return render(request,"index.html")

def search(request):
    data = request.GET['data']
    # row="<ul>"
    # if data=="sports":
    #     row+='<li>Cricket</li>'
    #     row+='<li>Football</li>'
    #     row+='<li>Hockey</li>'
    # row+="</ul>"

    products = Product.objects.filter(name__startswith=data)

    return JsonResponse({"data":list(products.values())})

def countries(request):
    allcounty = country.objects.all()
    return JsonResponse({"data":list(allcounty.values())})

def states(request):
    cid = request.GET['cid']
    allstates = state.objects.filter(country_id=cid)
    return JsonResponse({'data':list(allstates.values())})

def cities(request):
    sid = request.GET['sid']
    allcities = city.objects.filter(state_id=sid)
    return JsonResponse({'data':list(allcities.values())})
