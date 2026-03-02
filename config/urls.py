"""
URL configuration for promodoro_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from timer import views  # 確保這裡導入的是你的 app 名稱

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),               # 這裡會對應到首頁
    path('update/', views.update_count, name='update'), # 這是給 JavaScript 呼叫的 API
]
