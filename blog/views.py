# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage,InvalidPage
from blog.models import Post, Comment
from blog.form import CommentForm
from django.contrib import messages



def blog_view(request, **kwargs):
    posts = Post.objects.filter(status = True)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])   
    if kwargs.get('tag_name') != None:       
        posts = Post.objects.filter(tag__name__in=[kwargs['tag_name']])

    posts = Paginator(posts, 3)

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
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your comment was submitted')
        else:           
            messages.add_message(request, messages.ERROR, 'your comment did not submit')
    posts = Post.objects.filter(status = True)
    post = get_object_or_404(posts, pk=  pid) 
    comments = Comment.objects.filter(post=post.id, approved = True)
    form = CommentForm()
    contex = {'post': post, 'comments': comments, 'form':form }
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
