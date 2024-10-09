from django.contrib import admin
from django.urls import path, include
from initialpage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include("account.urls")),
    path('menuselection/', include("menuselection.urls")),
    path('payment/', include("payment.urls")),
    path('', views.index, name='pagina_inicial'),
]