from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('second page')
def help(request):
    my_dict={'insert_help':"HELP PAGE"}
    return render(request,'app1/help.html',context=my_dict)