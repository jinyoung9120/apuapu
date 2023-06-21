from django.shortcuts import render
from boardapp.models import Board
from django.http import HttpResponse
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    rsBoard = Board.objects.all().order_by('-b_no')
    page = int(request.GET.get('page', 1))
    pagenator = Paginator(rsBoard, 5)
    page_obj = pagenator.get_page(page)
    context = {'rsBoard' : page_obj}
    return render(request,
                    "mainapp/index2.html",
                    {"rsBoard" : page_obj})

    
def pill_register(request):
    return render(request, 
                    "mainapp/pill_register.html",
                    {})