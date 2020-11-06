# pages/views.py
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Post

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'pages/post_list.html', {'posts': posts})
