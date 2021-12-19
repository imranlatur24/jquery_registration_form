
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage,name='register'),
    path('reg/', views.reg,name='reg'),
]
