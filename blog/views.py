from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status = True)
    contex = {'posts': posts}
    return render(request, "blog/blog-home.html", contex)

def blog_single(request, pid):
    posts = Post.objects.filter(status = True)
    post = get_object_or_404(posts, pk=  pid) 
    contex = {'post': post}
    return render(request, 'blog/blog-single.html', contex)

def test(request, pid):
    #post = Post.objects.get(id= pid)
    # we use (Page not found (404) ) error instead (Post matching query does not exist) error  
    post = get_object_or_404(Post, pk=  pid) 
    contex = {'post': post}
    return render(request, 'test.html', contex)