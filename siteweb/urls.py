from django.urls import path

from siteweb import views
from siteweb.views import PlanoDetailView, PlanosAdquiridosView

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('plano/<int:pk>/', PlanoDetailView.as_view(), name='adquirir_plano'),
    path('planos-adquiridos/', PlanosAdquiridosView.as_view(), name='planos_adquiridos'),
]
