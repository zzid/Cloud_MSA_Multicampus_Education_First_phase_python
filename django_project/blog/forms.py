from django import forms
from .models import Post

def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요.')

class PostForm(forms.Form):
    title = forms.CharField(validators = [min_length_3_validator])
    text = forms.CharField(widget = forms.Textarea)


## 2020.8.6
class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', )