from django.db import models
from django.utils import timezone
from django import forms

def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요.')

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete= models.CASCADE)
    title = models.CharField(max_length =200, validators=[min_length_3_validator])
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null =True)
    

    ## 2020.08.05
    ## Field for testing 
    
    # test = models.TextField()

    '''
        publish :
            to make published_date
            same with created_date

        __str__ : 
            to see as a title in the admin,
            not like 'Post object(1)'(object address)
    '''

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    

    def __str__(self):
        return self.title