from django.views.decorators.csrf import csrf_exempt

from django.urls import path
from .views import CRUDUser
from rest_framework.authtoken import views
urlpatterns = [
    path('api/register/', csrf_exempt(CRUDUser.as_view())),
    path('login/', views.obtain_auth_token),
]
