from django import forms
from django.forms import fields


from .models import apply,Job

class ApplyForm(forms.ModelForm):
    class Meta():
        model = apply
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'website': forms.URLInput(attrs={'placeholder': 'Website/Portfolio link'}),
            'cv': forms.FileInput(attrs={'placeholder': 'Upload CV','id':'inputGroupFile03', 'aria-describedby':'inputGroupFileAddon03'}),
            'cover_letter': forms.Textarea(
                attrs={'placeholder': 'Enter CoverLetter here','cols':'30', 'rows':'10'}),
        }

        fields = ['name','email','website','cv','cover_letter']



class JobForm(forms.ModelForm):
    class Meta():
        model=Job
        fields="__all__"
        exclude=('slug','owner')







        