from conta.views import LoginView, login_view
from django.urls import path, include
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('authenticate/', login_view, name='authenticate'),
    path('social-auth/', include('social_django.urls', namespace='social')),
]
