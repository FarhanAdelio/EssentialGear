from django.urls import path
from main.views import show_main
from django.urls import path, include
from django.contrib import admin
from .views import index

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]