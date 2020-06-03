"""css URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import capp.views
import account.urls
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', capp.views.home, name="home"),
    path('detail/<int:css_id>', capp.views.detail, name="detail"),
    path('edit/<int:css_id>', capp.views.edit, name="edit"),
    path('update/<int:css_id>', capp.views.update, name="update"),
    path('mypage/', capp.views.mypage, name="mypage"),
    path('review/', capp.views.review, name="review"),
    path('account/', include(account.urls)),   
    path('delete/<int:css_id>', capp.views.delete, name="delete"),     
] 

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
