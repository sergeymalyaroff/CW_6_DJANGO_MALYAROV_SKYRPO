# users/views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.decorators import user_passes_test
from .models import CustomUser  # или другая модель, если вы используете другую для пользователей
from newsletters.models import Newsletter  # предполагая, что у вас есть модель Newsletter для рассылок


def is_manager(user):
    """
    Проверяет, является ли пользователь менеджером.

    Args:
    - user (CustomUser): экземпляр пользователя.

    Returns:
    - bool: True, если пользователь принадлежит к группе "Manager", иначе False.
    """
    return user.groups.filter(name='Manager').exists()


@user_passes_test(is_manager)
def manager_view(request):
    """
    Представление для менеджера. Показывает список всех пользователей и рассылок.

    Args:
    - request (HttpRequest): объект запроса.

    Returns:
    - HttpResponse: ответ с отображением списка пользователей и рассылок.
    """
    all_users = CustomUser.objects.all()
    all_newsletters = Newsletter.objects.all()

    context = {
        'users': all_users,
        'newsletters': all_newsletters,
    }

    return render(request, 'users/path_to_manager_template.html', context)


def user_login(request):
    """
    Представление для входа пользователя.

    Args:
    - request (HttpRequest): объект запроса.

    Returns:
    - HttpResponse: ответ с формой входа или перенаправление на главную страницу после успешного входа.
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
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
    return render(request, 'users/path_to_login_template.html', {'form': form})
