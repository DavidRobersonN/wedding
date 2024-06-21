from django.views.generic import TemplateView
# conta/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


class LoginView(TemplateView):
    template_name = 'login.html'


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirecionar para uma página de sucesso, por exemplo:
            return redirect('index')  # substitua 'index' pelo nome da sua view inicial após o login
        else:
            # Lidar com o erro de login inválido, por exemplo:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return redirect('login')  # Redirecionar para a página de login se a solicitação não for POST
