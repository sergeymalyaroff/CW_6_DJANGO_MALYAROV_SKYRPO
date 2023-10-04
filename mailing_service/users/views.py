# views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('desired_redirect_url')  # например, 'home'
                else:
                    # Добавьте сообщение о том, что аккаунт не активен
                    pass
            else:
                # Добавьте сообщение о неверных учетных данных
                pass
    else:
        form = LoginForm()
    return render(request, 'path_to_login_template.html', {'form': form})
