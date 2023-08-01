from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict={'insert_content':'hello im from second app'}
    return render(request, 'second_app/index.html',context=my_dict)
