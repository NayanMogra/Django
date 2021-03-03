from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author'    :   'Author1',
        'title'     :   'My First Blog',
        'content'   :   'First Post Content Must see',
        'date_posted' : 'Jan 1, 2021' 
    },

        {
        'author'    :   'Author2',
        'title'     :   'Second Blog',
        'content'   :   'Second Post Content Must see',
        'date_posted' : 'Jan 10, 2021' 
    },
]
def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html' , context = context)


def about(request):
    return render(request , 'blog/about.html' , {'title' : "About"})