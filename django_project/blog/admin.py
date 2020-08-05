from django.contrib import admin

from .models import Post    ## register the models from models.py
                            ## Post is model name that i define

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
