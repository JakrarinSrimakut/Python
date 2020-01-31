from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.

# Take both GET and POST request for signing up user
def signup_view(request):
    if request.method == 'POST': 
        form = UserCreationForm(request.POST) # request.POST has all user data input
        if form.is_valid(): # Check if user already exist if so save to DB
            user = form.save() # save user to DB and return user
            # log the user in
            login(request, user)
            return redirect('articles:list') # send user to list
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form}) # will take GET request and POST that failed

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) # check user's authentication. request.POST is not 1st param so data= is required
        if form.is_valid():
            # log in user
            user = form.get_user() # extract user from authenticated form
            login(request, user)
            return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form}) # like def sign_up if authen POST fail send error to this render

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')