from django.contrib import admin

## register the models from models.py
## Post is model name that i define
from .models import Post,Comment

'''
2020_08_05
    PostAdmin

'''

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'count_text']
    list_display_links = ['title']
    
    def count_text(self, obj):
        return f'{len(obj.text)} 글자'#'{}글자'.format(len(obj.text))
    
    count_text.short_description = 'text 글자수'


admin.site.register(Post, PostAdmin)
admin.site.register(Comment) ## 2020.8.7