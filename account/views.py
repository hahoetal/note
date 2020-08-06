from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    signup_form = UserCreationForm()

    if request.method =="POST":
        fiiled_form = UserCreationForm(request.POST)

        if fiiled_form.is_valid():
            fiiled_form.save()
            return redirect('home')
    return render(request, 'signup.html', {'signup_form':signup_form})
