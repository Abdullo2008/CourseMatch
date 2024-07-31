from django import forms
from .models import CourseModel, BlogModel


class CourseEditForm(forms.ModelForm):
    class Meta:
        model = CourseModel
        fields = ['course', 'image', 'title', 'body', 'category']
        widgets = {
            'course': forms.TextInput(attrs={'class': 'form-class'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-class'}),
            'title': forms.TextInput(attrs={'class': 'form-class'}),
            'body': forms.Textarea(attrs={'class': 'form-class'}),
            'category': forms.TextInput(attrs={'class': 'form-class'}),
        }


class BlogEditForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['course', 'blog']
        widgets = {
            'course': forms.TextInput(attrs={'class': 'form-class'}),
            'blog': forms.Textarea(attrs={'class': 'form-class'}),
        }

