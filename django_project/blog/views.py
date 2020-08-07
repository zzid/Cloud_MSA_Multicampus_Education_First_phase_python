'''
2020.8.6
    postForm
'''
from django.shortcuts import render
from .forms import PostModelForm, PostForm, CommentModelForm
'''
2020.08.05
    post_list
'''
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Post,Comment
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

'''
2020.8.7
    Comment

'''

## this is naive
# def post_list(request):
#     name = 'Django'
#     my_git_url = 'https://www.github.com/zzid'
#     git_icon_path = "https://github.githubassets.com/images/modules/logos_page/GitHub-Logo.png"
#     return HttpResponse(
#         f'''
#             <h1>Post list</h1>
#             <p> Welcome to {name}!</p>
#             <p>{request.user}</p>
#             <div>
#             <a href = {my_git_url} target = "_blank">
#                 <img src = {git_icon_path} width = 100>
#             </a>
#             </div>
#         '''
#     )

## Rending with use html static file
def post_list(request):
    post_list = Post.objects.all().order_by('-created_date')
    # post_list = Post.objects.filter(published_date__gte = timezone.now())\
    #     .order_by('published_date')
    param = {
        'post_list' : post_list,
    }
    return render(request, 'blog/post_list.html', param)



## 2020.8.6 
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    param ={
        'post' : post,
    }
    return render(request, 'blog/post_detail.html', param)

@login_required
def post_edit(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance = post) ## this is different with post_new
        if form.is_valid():
            post = form.save(commit=False) ## commit = False :: not gonna store that to DB now
            post.author = User.objects.get(username = request.user.username)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk = post.pk)
    else:
        form = PostModelForm(instance=post)
    return render(request,'blog/post_edit.html', {'form' : form})

@login_required
def post_new(request):
    if request.method == "POST": ## if save button has been clicked >> I set that to POST method.
        form = PostForm(request.POST)  
        if form.is_valid(): # PostForm class
            # print(form.cleaned_data)
            post = Post.objects.create(
                        author = User.objects.get(username= request.user.username),
                        published_date = timezone.now(),
                        title=form.cleaned_data['title'],
                        text= form.cleaned_data['text']
                    )
            # post = form.save(commit=False) 
            # post.author = User.objects.get(username = request.user.username)
            # post.published_date = timezone.now()
            # post.save()
            return redirect('post_detail', pk=post.pk)
    else: ## GET Method
        form = PostForm() 
    return render(request,'blog/post_edit.html',{'form' : form})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk = pk)
    post.delete()
    return redirect('post_list')

## 2020.8.7
@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
        return redirect('post_detail', pk=post.pk)
    else:
        form = CommentModelForm()
    return render(request, 'blog/add_comment_to_post.html',{'form' :form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk = comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)
