from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from auth_app.views import AuthView
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

router = DefaultRouter()
router.register('users', AuthView, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products_app.urls')),
    path('', include(router.urls)),
    path('access/', token_obtain_pair, name='token_access'),
    path('refresh/', token_refresh, name='token_refresh'),
]
