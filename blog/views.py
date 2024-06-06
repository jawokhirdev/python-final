from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost

def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/blog_detail.html', {'post': post})

@login_required
def blog_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        BlogPost.objects.create(title=title, content=content)
        return redirect('blog_list')
    return render(request, 'blog/blog_form.html')

@login_required
def blog_update(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('blog_detail', pk=post.pk)
    return render(request, 'blog/blog_form.html', {'post': post})

@login_required
def blog_delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog_list')
    return render(request, 'blog/blog_confirm_delete.html', {'post': post})
