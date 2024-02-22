from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from auth_app.views import AuthView

router = DefaultRouter()
router.register('users', AuthView, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products_app.urls')),
    path('', include(router.urls)),
]
