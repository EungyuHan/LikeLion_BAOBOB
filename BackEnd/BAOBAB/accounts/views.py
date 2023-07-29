from django.shortcuts import render, redirect
from .forms import SignUpForm
#from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def signup(request):
    if request.method == "GET":
        form = SignUpForm()
        context = {'form': form}
        return render(request, "accounts/accounts.html")
    
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect("index")
        else:
            return redirect("accounts:signup")