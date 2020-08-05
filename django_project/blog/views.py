from django.shortcuts import render
'''
2020.08.05
    post_list
'''
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Post

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
    my_git_url = 'https://www.github.com/zzid'
    git_icon_path = "https://github.githubassets.com/images/modules/logos_page/GitHub-Logo.png"

    post_list = Post.objects.all()
    # post_list = Post.objects.filter(published_date__gte = timezone.now())\
    #     .order_by('published_date')
    param = {
        'my_git_url' : my_git_url,
        'git_icon_path' : git_icon_path,
        'post_list' : post_list,
    }
    return render(request, 'blog/post_list.html', param)