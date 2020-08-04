from django.contrib import admin
from .models import Post    ## register the models from models.py
                            ## Post is model name that i define
# Register your models here.
admin.site.register(Post)
