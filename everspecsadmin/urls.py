"""everspecsadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
#from updates.views import json_example, jsonCBV, JsonCBV2, SerializedListView, SerializedDetailView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/updates/', include('updates.api.urls')),
    # path('json_example', json_example, name='json_example'),
    # path('join/jsoncbv', jsonCBV.as_view()),
    # path('join/jsoncbv2', JsonCBV2.as_view()),
    # path('join/serialized/list', SerializedListView.as_view()),
    # path('join/serialized/details', SerializedDetailView.as_view())
]
