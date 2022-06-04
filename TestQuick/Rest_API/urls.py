"""Rest_API App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from .views import CRUDBills, CRUDClients, CRUDProducts

# template_patterns = [
#     path('', TemplateView.as_view(template_name="patient_list.html")),
#     path('patient/list/', TemplateView.as_view(template_name="patient_list.html"), name="list"),
#     path('patient/create/', TemplateView.as_view(template_name="patient_create.html")),
#     path('patient/<int:pk>/edit/', TemplateView.as_view(template_name="patient_update.html")),
#     # path('camera/<int:pk>/delete/', TemplateView.as_view(template_name="camera_delete.html")),
# ]
urlpatterns = [
    path('api/clients/all/', csrf_exempt(CRUDClients.as_view())),
    path('api/client/<int:pk>/', csrf_exempt(CRUDClients.as_view())),
    path('api/bills/all/', csrf_exempt(CRUDBills.as_view())),
    path('api/bill/<int:pk>/', csrf_exempt(CRUDBills.as_view())),
    path('api/products/all/', csrf_exempt(CRUDProducts.as_view())),
    path('api/product/<int:pk>/', csrf_exempt(CRUDProducts.as_view())),

    # path('', include(template_patterns)),
]
