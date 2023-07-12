
from django.contrib import admin
from django.urls import path
from todo.views import home, login, signup, add_todo, signout, delete_todo,change_todo

# All the app urls is here

urlpatterns = [
    # default page loded first
    path('', home, name='home'),
    # url for login page
    path('login/',login, name='login'),
    # url for signup page 
    path('signup/', signup),
    # url for todo page
    path('add-todo/',add_todo),
    # url for signout page
    path('logout/',signout),
    path('delete-todo/<int:id>',delete_todo),
    path('change-status/<int:id>/<str:status>',change_todo),
]
