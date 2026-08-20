from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage,InvalidPage
from blog.models import Post

# Create your views here.
def blog_view(request, **kwargs):
    posts = Post.objects.filter(status = True)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    posts = Paginator(posts, 3)
    print(posts.num_pages)

    try:
        page_number = request.GET.get('page')
        posts = posts.page(page_number)
    except PageNotAnInteger:
        posts = posts.page(1)
    except InvalidPage:
        posts = posts.page(1)

    
    contex = {'posts': posts}
    return render(request, "blog/blog-home.html", contex)

def blog_single(request, pid):
    posts = Post.objects.filter(status = True)
    post = get_object_or_404(posts, pk=  pid) 
    contex = {'post': post}
    return render(request, 'blog/blog-single.html', contex)

def blog_category(request, cat_name):
    posts = Post.objects.filter(status = True)
    posts = posts.filter(category__name = cat_name)
    contex = {'posts': posts}
    return render(request, "blog/blog-home.html", contex)

def blog_search(request):
    posts = Post.objects.filter(status = True)
    if request.method == "GET":
        if s:=request.GET.get('s'):
            posts = posts.filter(content__contains = s)
    contex = {'posts': posts}
    return render(request, 'blog/blog-home.html', contex)


def test(request):
   
    return render(request, 'test.html')
