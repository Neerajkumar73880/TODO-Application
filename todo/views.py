from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as loginUser , logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from todo.forms import TODOForm
from todo.models import TODO
from django.contrib.auth.decorators import login_required



# Create your views here.


# This is the home views
@login_required(login_url='login')
def home(request):
    # This will check the user status either authenticated or not 
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user=user).order_by('priority')
        return render(request, 'index.html',context={'form':form, 'todos' :todos})


# This is the login views
def login(request):
    if request.method == "GET":
        form = AuthenticationForm()
        context = {
            "form" : form
        }
        return render(request, 'login.html', context=context)
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                loginUser(request, user)
                return redirect('home')

        else:
            context = {
                "form" : form
            }
            return render(request, 'login.html', context=context)






# This is the signup views
def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form" : form
        }
        return render(request, 'signup.html' , context=context)
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)
        context = { 
            "form" : form  
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
            return render(request, 'signup.html', context=context)
        


# This is the Add todo views it is for add the new todo
@login_required(login_url='login')
def add_todo(request):
    # This will check the user status either authenticated or not 
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form=TODOForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            print(todo)
            return redirect("home")
        else:
            return render(request, 'index.html',context={'form':form})
        

# This is the signout views
def signout(request):
    logout(request)
    return redirect('login')


# This is the Delete todo views it is for delete the todo
def delete_todo(request , id):
    print(id)
    TODO.objects.get(pk=id).delete()
    return redirect("home")



# This is for changing the todo from completed to pending and vice versa
def change_todo(request , id, status):
    todo = TODO.objects.get(pk=id)
    todo.status = status
    todo.save()
    return redirect("home")