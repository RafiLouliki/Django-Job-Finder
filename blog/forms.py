from django import forms

from .models import Comment,Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields="__all__"
        exclude=('slug','author','created_on','updated_on')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['email','body']