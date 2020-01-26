from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post
# Create your views here.

postes = [
    {
        "title": "How To Use ReactJS with Django",
        "ahutor": "yazan al monshed",
        "date": 'Aug 13 2020',
        "post": "you can using django and react by add more cabiblity to your code and ..." 
    },
     {
        "title": "How To Use Larvel with vueJs",
        "ahutor": "Othman Omar",
        "date": 'Aug 23 2020',
        "post": "you can using django and react by add more cabiblity to your code and ..." 
    },
     {
        "title": "How To Use Larvel with React",
        "ahutor": "Othman Omar",
        "date": 'Aug 23 2020',
        "post": "you can using django and react by add more cabiblity to your code and ..." 
    }
]


def show_data(request):
    context = {
        'postes': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)

def show_info(request):

    return render(request, 'blog/contact.html',{'title': 'React'})