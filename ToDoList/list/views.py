from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Task
from .forms import *
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404

class Adduser(generic.CreateView):
    model=User
    template_name = 'add-user.html'
    success_url=reverse_lazy('login')
    form_class = UserCreationForm
    redirect_authenticated_user=True


class editUser(generic.UpdateView):
    model = User
    template_name="edit-user.html"
    form_class = EditUserForm
    success_url=reverse_lazy('list')



    
    
class TaskListView(ListView):
    model=Task
    template_name="list.html"

    def get_context_data(self,*args, **kwargs):
        
        context=super(TaskListView, self).get_context_data(*args, **kwargs)
        tasks=Task.objects.filter(user=self.request.user.id)
        search_input=self.request.GET.get('serch-input')
    
        if search_input:
            stuff=tasks.objects.filter(title__icontaning =search_input)
            context["tasks"]=stuff

        else:
            context["tasks"]=tasks


        return context
    
    
  

class TaskDetaileView(DetailView):
    model=Task
    template_name="detail.html"




class AddView(CreateView):
    model=Task
    template_name="add.html"
    form_class=TaskForm
    success_url=reverse_lazy('list')
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class EditView(UpdateView):
    model=Task
    template_name="edit.html"
    form_class=TaskForm
    success_url=reverse_lazy('list')
class deletView(DeleteView):
    model=Task
    template_name="delete.html"
    success_url=reverse_lazy('list')

    
