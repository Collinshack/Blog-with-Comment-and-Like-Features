from django import forms 
from .models import Comment

class CommentForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Name:'
    }))
    
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Email:'
    }))
    
    comment_body = forms.CharField(widget=forms.Textarea(attrs={
        'id': 'form-textarea', 'placeholder': 'Comment Here...:'
    }))
    
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment_body']