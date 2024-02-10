"""
URL configuration for memoriamtest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from emailsender.views import test_email, schedule_emails, send_test_email

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test-email/', test_email, name='test_email'),
    path('test-schedule-emails/', schedule_emails, name='schedule_emails'),
    path('send-test-email/', send_test_email, name='send_test_email')
]
