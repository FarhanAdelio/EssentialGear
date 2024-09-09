from django.urls import path
from main.views import show_main
from django.urls import path, include
from django.contrib import admin
from .views import index

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('', include('main.urls')),
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('bonus_tdd', include('bonus_tdd.urls')),
]