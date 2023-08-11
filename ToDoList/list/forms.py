from django import forms
from .models import *
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title','discription']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder':'title'
                }),
            'discription': forms.Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder':'description'
                }),
                }
        

class EditUserForm(forms.ModelForm):
            
            username = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
            first_name = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
            email = forms.EmailField(max_length=150,widget=forms.EmailInput(attrs={'class':'form-control'}))     
            last_name = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
   
    
            class Meta:
                 
                 model=User           
                 fields=['first_name', 'username', 'email', 'last_name']
    




class RigestreamForm(forms.ModelForm):
         class Meta:
            model = User
            fields = ['first_name', 'username', 'password']
            widgets = {
                'password': forms.PasswordInput()
            }

            def save(self):
                self.clean()
                user = self.Meta.model(
                    username = self.cleaned_data['username'], 
                    email = self.cleaned_data['email'], 
                )
                user.set_password(self.cleaned_data['password2'])
                user.save()
                return user