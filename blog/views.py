from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from django.core.paginator import Paginator
from .models import Blog
from .models import Portfolio
from .form import Blogpost

def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')
    posts= paginator.get_page(page)
    return render(request, 'home.html', {'blogs': blogs, 'posts':posts})

    
def detail(request, pk):
    blog_detail = get_object_or_404(Blog, pk = pk)
    return render(request, 'detail.html', {'blog':blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
	blog = Blog()
	blog.title = request.GET['title']
	blog.pub_date = timezone.datetime.now()
	blog.body = request.GET['body']
	blog.save()
	
	return redirect('/blog/'+str(blog.pk))

def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio.html', {'portfolios': portfolios})

def blogpost(request):
    if request.method =='POST':
        form = Blogpost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()

            return redirect('home')
    else:
        form = Blogpost()
        return render(request, 'new.html', {'form':form})