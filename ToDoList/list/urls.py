from django.urls import path
from .views import *



urlpatterns = [

    path('', TaskListView.as_view(),name='list'),
    path('task/<int:pk>', TaskDetaileView.as_view(),name='description'),
    path('add', AddView.as_view(),name='add'),
    path('<int:pk>/edit', EditView.as_view(),name='edit'),
    path('delete/<int:pk>',deletView.as_view(),name='delete'),
    path('register', Adduser.as_view(),name='register'),
    path('edit/<int:pk>', editUser.as_view(),name='edit-user'),


    
]
