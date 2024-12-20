from django.urls import path
from usuario import views
from usuario.views import CadastroUsuarioView, LogoutUsuarioView

urlpatterns = [

    path('cadastrar/', CadastroUsuarioView.as_view(), name='cadastrar'),

    path('login/', views.LoginUsuarioView.as_view(), name='loginuser'),
    path('logout/', LogoutUsuarioView.as_view(), name='logoutuser'),
]